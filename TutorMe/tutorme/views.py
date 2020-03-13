from django.http import HttpResponse
from django.shortcuts import render
from tutorme.forms import CategoryForm
from django.shortcuts import redirect
from django.urls import reverse
from tutorme.forms import UserForm, StudentForm, TeacherForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from tutorme.models import Category, Student, Teacher, User
from datetime import datetime
from django.conf import settings
from .picture_downloader import PictureDownloader
from django.core.files.base import ContentFile
from io import BytesIO


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
    category_list = Category.objects.order_by('-likes')[:5]

    context_dict = dict()
    if not request.user.is_anonymous:
        try:
            student = Student.objects.get(user=request.user)
            context_dict['username'] = student.first_name
            context_dict['user_type'] = 'student'
        except Student.DoesNotExist:
            teacher = Teacher.objects.get(user=request.user)
            context_dict['username'] = teacher.first_name
            context_dict['user_type'] = 'teacher'

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


def show_category(request, category_name_slug):
    # Create a context dictionary which we can pass
    # to the template rendering engine.
    context_dict = dict()

    try:
        # Can we find a category name slug with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception.
        # The .get() method returns one model instance or raises an exception.
        category = Category.objects.get(slug=category_name_slug)

        context_dict['category'] = category
    except Category.DoesNotExist:
        # We get here if we didn't find the specified category.
        # Don't do anything -
        # the template will display the "no category" message for us.
        context_dict['category'] = None
        context_dict['pages'] = None

    # Go render the response and return it to the client.
    return render(request, 'tutorme/category.html', context=context_dict)


@login_required
def add_category(request):
    form = CategoryForm()

    # A HTTP POST?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)
            # Now that the category is saved, we could confirm this.
            #  For now, just redirect the user back to the index view.
            return redirect('/tutorme/')
        else:
            # The supplied form contained errors -
            # just print them to the terminal.
            print(form.errors)
    # Will handle the bad form, new form, or no form supplied cases.
    # Render the form with error messages (if any).
    return render(request, 'tutorme/add_category.html', {'form': form})


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
                        return HttpResponse("Bad request")
            else:
                return HttpResponse("Bad request")
    else:
        user_form = UserForm()
        teacher_form = TeacherForm()
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
                return HttpResponse("Your account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in. print(f"Invalid login details: {username}, {password}")
            if request.POST.get('fb'):
                return HttpResponse('{"registered" : false}')
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        if not request.user.is_anonymous:
            return redirect(reverse('tutorme:index'))
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render(request, 'tutorme/login.html')


@login_required
def restricted(request):
    return render(request, 'tutorme/restricted.html')


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
