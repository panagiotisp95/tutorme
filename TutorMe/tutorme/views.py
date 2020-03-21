from django.http import HttpResponse
from django.shortcuts import render
from tutorme.forms import CategoryForm
from django.shortcuts import redirect
from django.urls import reverse
from tutorme.forms import UserForm, StudentForm, TeacherForm, TeacherUpdateForm, StudentUpdateForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from tutorme.models import Category, Student, Teacher, User, Review
from datetime import datetime
from django.conf import settings
from .picture_downloader import PictureDownloader
from django.core.files.base import ContentFile
from io import BytesIO
import re
from django.core import serializers


def index(request):
    response = redirect(reverse('tutorme:login'))
    if request.session.get_expiry_age()>0:
        if not request.user.is_anonymous:
            response = redirect(reverse('tutorme:homepage'))

    return response


@login_required
def homepage(request):
    # Query the database for a list of ALL categories currently stored.
    # Order the categories by the number of likes in descending order.
    # Retrieve the top 5 only -- or all if less than 5.
    # Place the list in our context_dict dictionary (with our boldmessage!) # that will be passed to the template engine.
    category_list = Category.objects.order_by('-name')[:5]

    context_dict = dict()
    user = get_user(request.user)
    context_dict['user_obj'] = user
    if user.description == "":
        return dashboard(request)
    context_dict['boldmessage'] = 'Crunchy, creamy, cookie, candy, cupcake!'
    context_dict['categories'] = category_list
    visitor_cookie_handler(request)
    response = render(request, 'tutorme/index.html', context=context_dict)

    return response


def about(request):
    visitor_cookie_handler(request)
    context_dict = dict()
    context_dict['visits'] = request.session['visits']
    response = render(request, 'tutorme/about.html', context=context_dict)
    return response


@login_required
def dashboard(request):
    context_dict = dict()
    user = get_user(request.user)
    context_dict['user_obj'] = user

    if user.description == "":
        context_dict['empty_fields'] = True
        context_dict['message'] = "Your account is not complete. Press Edit Profile below complete your registration"

    if request.method == 'POST':
        print(request.POST)
        if 'delete' in request.POST:
            request.user.delete()
            return user_logout(request)
        else:
            if hasattr(user, 'students'):
                form = TeacherUpdateForm(request.POST, instance=user)
            else:
                form = StudentUpdateForm(request.POST, instance=user)

            if form.is_valid():
                user = form.save(commit=False)
                if 'picture' in request.FILES:
                    user.picture = request.FILES['picture']

                user.save()
                context_dict['user_obj'] = user

    connections = list()
    if hasattr(user, 'students'):
        form = TeacherUpdateForm(instance=user)
        for student in user.students.all() or []:
            connections.append(student)
    else:
        form = StudentUpdateForm(instance=user)
        context_dict['student'] = True
        connections = user.teachers.all()
        has_review = list()
        for connection in connections:
            try:
                review = Review.objects.get(reviewee=connection, reviewer=user)
                has_review.append(review.rating)
            except Review.DoesNotExist:
                has_review.append(None)
        context_dict['has_review'] = has_review

    context_dict['form'] = form
    context_dict['connections'] = connections
    return render(request, 'tutorme/dashboard.html', context=context_dict)


@login_required
def search(request):
    context_dict = dict()

    if request.method == 'POST':
        search_string = request.POST.get('search')
        search_string = re.sub('[^A-Za-z0-9 ]+', '', search_string)

        search_list = search_string.split()

        teachers = list()
        for item in search_list:
            teacher = find_teacher(item)
            if teacher is not None and teacher.active:
                    teachers.append(teacher)
            item = item.capitalize()

            for teacher in find_teachers_by_category(item) or []:
                if teacher.active:
                    teachers.append(teacher)

        context_dict['teachers'] = teachers
        print(teachers)
    else:
        context_dict['teachers'] = Teacher.objects.order_by('-first_name').filter(active=True)[:5]
    response = render(request, 'tutorme/search.html', context=context_dict)
    return response


@login_required
def accept(request):
    if request.method == 'POST':
        user = User.objects.get(email=request.POST.get('teacher_email'))
        teacher = get_user(user)
        student_user = User.objects.get(email=request.POST.get('student_email'))
        student = get_user(student_user)
        teacher.students.add(student)
        return HttpResponse("ok")
    return HttpResponse("Bad request")


def find_teacher(first_name):
    try:
        teacher = Teacher.objects.get(first_name=first_name)
        return teacher
    except Teacher.DoesNotExist:
        return None


def find_teachers_by_category(name):
    try:
        category = Category.objects.get(name=name)
        return category.teachers.all()
    except Category.DoesNotExist:
        return None


def get_all_categories():
    try:
        return Category.objects.all()
    except Category.DoesNotExist:
        return None


def get_user(user):
    response = None
    if not user.is_anonymous:
        try:
            response = Student.objects.get(user=user)
        except Student.DoesNotExist:
            response = Teacher.objects.get(user=user)

    return response


@login_required
def rate(request):
    if request.method == 'POST':
        user = User.objects.get(email=request.POST.get('teacher_email'))
        teacher = get_user(user)
        student_user = User.objects.get(email=request.POST.get('student_email'))
        student = get_user(student_user)
        rating = int(request.POST.get('rating'))
        print(teacher.first_name+student.first_name+request.POST.get('rating'))
        review = Review(reviewee=teacher, reviewer=student, rating=rating)
        review.save()
        return HttpResponse("ok")
    return HttpResponse("Bad request")


def show_category(request, category_name):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = dict()

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # The .get() method returns one model instance or raises an exception.
        category = Category.objects.get(name=category_name)
        teacher_list = category.teachers.all()
        context_dict['category'] = category
        context_dict['teachers'] = teacher_list
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        context_dict['category'] = None

    # Go render the response and return it to the client.
    return render(request, 'tutorme/category.html', context=context_dict)


def register_student(request):
    registered = False
    registered_message = 'Thank you for registering!'
    if request.method == 'GET':
        if 'registered' in request.GET:
            if 'registered_message' in request.GET:
                registered_message = request.GET['registered_message']
            return render(request, 'tutorme/register.html', context={'registered': request.GET['registered'], 'registered_message': registered_message})

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        student_form = StudentForm(request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and student_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            student = student_form.save(commit=False)
            student.user = user

            if 'picture' in request.FILES:
                student.picture = request.FILES['picture']

            student.save()
            registered = True
        else:
            email = request.POST.get('email')
            if email:
                try:
                    User.objects.get(email=email)
                    registered = True
                    registered_message = "Account already exists with email '" + email + "'"
                    url = "/tutorme/register_student/?registered=True&registered_message="+registered_message
                    if request.POST.get('fb'):
                        return HttpResponse('{"url" : "'+url+'"}')
                except User.DoesNotExist:
                    if request.POST.get('fb'):
                        return register_with_fb(request, False)
                    else:
                        return HttpResponse("Bad request")
            else:
                return HttpResponse("Bad request")
    else:
        user_form = UserForm()
        student_form = StudentForm()
    return render(request, 'tutorme/register.html', context={'student': True, 'student_form': student_form, 'user_form': user_form, 'registered': registered, 'registered_message': registered_message})


def register_teacher(request):
    registered = False
    registered_message = 'Thank you for registering!'
    if request.method == 'GET':
        if 'registered' in request.GET:
            if 'registered_message' in request.GET:
                registered_message = request.GET['registered_message']
            return render(request, 'tutorme/register.html', context={'registered': request.GET['registered'], 'registered_message': registered_message})

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        teacher_form = TeacherForm(request.POST)

        if user_form.is_valid() and teacher_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            teacher = teacher_form.save(commit=False)
            teacher.user = user

            if 'picture' in request.FILES:
                teacher.picture = request.FILES['picture']

            teacher.save()
            teacher_form.save_m2m()
            registered = True
        else:
            email = request.POST.get('email')
            if email:
                try:
                    User.objects.get(email=email)
                    registered = True
                    registered_message = "Account already exists with email '" + email + "'"
                    url = "/tutorme/register_student/?registered=True&registered_message="+registered_message
                    if request.POST.get('fb'):
                        return HttpResponse('{"url" : "'+url+'"}')
                except User.DoesNotExist:
                    if request.POST.get('fb'):
                        return register_with_fb(request, True)
                    else:
                        print(user_form.errors)
                        print(teacher_form.errors)
                        return HttpResponse(teacher_form.errors)
            else:
                return HttpResponse("popo")
    else:
        user_form = UserForm()
        teacher_form = TeacherForm()
        print(teacher_form)
    return render(request, 'tutorme/register.html', context={'student': False, 'teacher_form': teacher_form, 'user_form': user_form, 'registered': registered})


def register_with_fb(request, teacher_student_flag):
    email = request.POST.get('email')
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    picture_url = request.POST.get('picture_url')
    img = PictureDownloader().get_image_from_url(picture_url)
    image_io = BytesIO()
    img.save(image_io, img.format, quality=60)

    filename = first_name.lower()+".jpeg"
    user = User.objects.create_user(email, email)
    user.save()

    if teacher_student_flag:
        teacher = Teacher(user=user, first_name=first_name, last_name=last_name)
        teacher.picture.save(filename, ContentFile(image_io.getvalue()))
        teacher.save()
    else:
        student = Student(user=user, first_name=first_name, last_name=last_name)
        student.picture.save(filename, ContentFile(image_io.getvalue()))
        student.save()

    return HttpResponse('{"url" : "/tutorme/register_student/?registered=True"}')


def user_login(request):
    # If the request is a HTTP POST, try to pull out the relevant information.
    context_dict = dict()
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not password:
            if request.POST.get('fb'):
                password = request.POST.get('email')

        user = authenticate(email=email, password=password)
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:

                if request.POST.get('remember_me', None) == "on":
                    # the session will expire after 2 weeks
                    request.session['user'] = email
                    request.session.set_expiry(settings.SESSION_EXPIRY)
                else:
                    # sets the global session expiry policy
                    request.session.set_expiry(0)
                # If the account is valid and active, we can log the user in. # We'll send the user back to the homepage.

                login(request, user)
                if request.POST.get('fb'):
                    return HttpResponse('{"url" : "/tutorme/homepage/"}')
                return redirect(reverse('tutorme:index'))
            else:
                # An inactive account was used - no logging in!
                context_dict['message'] = "Your account is disabled."
        else:
            # Bad login details were provided. So we can't log the user in. print(f"Invalid login details: {username}, {password}")
            if request.POST.get('fb'):
                return HttpResponse('{"registered" : false}')
            context_dict['message'] = "Invalid login details supplied."

        return render(request, 'tutorme/login.html', context=context_dict)

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        if not request.user.is_anonymous:
            return redirect(reverse('tutorme:index'))
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'tutorme/login.html', context=context_dict)


# Use the login_required() decorator to ensure only those logged in can # access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    # Take the user back to the homepage.
    return redirect(reverse('tutorme:login'))


# A helper method
def get_server_side_cookie(request, cookie, default_val=None):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val


def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))
    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7], '%Y-%m-%d %H:%M:%S')
    # If it's been more than a day since the last visit...
    if (datetime.now() - last_visit_time).days > 0:
        visits = visits + 1
        # Update the last visit cookie now that we have updated the count
        request.session['last_visit'] = str(datetime.now())
    else:
        # Set the last visit cookie
        request.session['last_visit'] = last_visit_cookie
    # Update/set the visits cookie
    request.session['visits'] = visits
