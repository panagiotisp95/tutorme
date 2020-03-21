import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tutorme_project.settings')
import django
django.setup()
from tutorme.models import Category, Student, Teacher, User


def populate():

    cats = {
        'Mathematics': {'teachers': []},
        'Algebra': {'teachers': []},
        'Geometry': {'teachers': []},
        'Trigonometry': {'teachers': []},
        'Statistics': {'teachers': []},
        'Calculus': {'teachers': []},
        'Differential': {'teachers': []},
        'Linear': {'teachers': []},
        'Physics': {'teachers': []},
        'Chemistry': {'teachers': []},
        'Organic': {'teachers': []},
        'Biology': {'teachers': []},
        'Health': {'teachers': []},
        'Electrical': {'teachers': []},
        'Cosmology': {'teachers': []},
        'Computing': {'teachers': []},
        'Programming': {'teachers': []},
        'Science': {'teachers': []},
        'History': {'teachers': []},
        'Art': {'teachers': []},
        'Grammar': {'teachers': []},
        'Storytelling': {'teachers': []},
        'Economics': {'teachers': []},
        'Microeconomics': {'teachers': []},
        'Macroeconomics': {'teachers': []},
        'Entrepreneurship': {'teachers': []}
    }

    for cat, cat_data in cats.items():
        add_cat(cat)

    for i in range(10):
        email = "student"+str(i)+"@gmail.com"
        password = "password"+str(i)
        first_name = "student"+str(i)
        last_name = "student"+str(i)
        description = "I'm a student"
        location = "Glasgow"
        add_student(email, password, first_name, last_name, description, location)

    for i in range(10):
        email = "teacher"+str(i)+"@gmail.com"
        password = "password"+str(i)
        first_name = "teacher"+str(i)
        last_name = "teacher"+str(i)
        description = "I'm a student"
        location = "Glasgow"
        rating = i/2;

        if i % 2 == 0:
            add_teacher(email, password, first_name, last_name, description, location, rating, ["Mathematics", ])
        else:
            add_teacher(email, password, first_name, last_name, description, location, rating, ["Chemistry", ])

    for c in Category.objects.all():
        print(f'- {c}')


def add_cat(name):
    c = Category.objects.get_or_create(name=name)[0]
    c.save()
    return c


def add_student(email, password, first_name, last_name, description, location):
    user = User.objects.create_user(email, password)
    user.save()
    student = Student(user=user, first_name=first_name, last_name=last_name, description=description, location=location)
    student.save()
    return student


def add_teacher(email, password, first_name, last_name, description, location, rating, categories):
    user = User.objects.create_user(email, password)
    user.save()
    teacher = Teacher(user=user, first_name=first_name, last_name=last_name, description=description, rating=rating, location=location)
    teacher.save()
    for category in categories:
        teacher.categories.add(Category.objects.get(name=category))
    teacher.save()
    return teacher


# Start execution here!
if __name__ == '__main__':
    print('Starting TutorMe population script...')
    populate()
