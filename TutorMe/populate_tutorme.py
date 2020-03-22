
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

    # "photo": "/profile_images/name",
    students = [
        {'email': 'conorthatcher@gmail.com', 'password': 'conorthatcher0', 'first_name': 'Conor',
         'last_name': 'Thatcher', 'description': 'Want to learn algebra.', 'location': 'Glasgow'},
        {'email': 'crystaladams@gmail.com', 'password': 'crystaladams0', 'first_name': 'Crystal',
         'last_name': 'Adams', 'description': 'Looking to learn more about Economics from an expert in the field.', 'location': 'Glasgow'},
        {'email': 'williamsmith@gmail.com', 'password': 'williamsmith0', 'first_name': 'William',
         'last_name': 'Smith', 'description': 'Just want to learn something exciting.', 'location': 'Glasgow'},
        {'email': 'zaynahcash@gmail.com', 'password': 'zaynahcash0', 'first_name': 'Zaynah',
         'last_name': 'Cash', 'description': 'Looking for a history teacher, preferably specialized in the Ancient period.', 'location': 'Glasgow'},
        {'email': 'albyglenn@gmail.com', 'password': 'albyglenn0', 'first_name': 'Alby',
         'last_name': 'Glenn', 'description': 'Have a passion for painting. Looking for a real mentor to help me improve.', 'location': 'Glasgow'},
        {'email': 'nuhabrittonr@gmail.com', 'password': 'nuhabritton0', 'first_name': 'Nuha',
         'last_name': 'Britton', 'description': 'Wanting to launch my own business but don\'t know where to start.', 'location': 'Glasgow'},
        {'email': 'ariellamackier@gmail.com', 'password': 'ariellamackie0', 'first_name': 'Ariella',
         'last_name': 'Mackie', 'description': 'Wannabe singer, could use some lessons.', 'location': 'Glasgow'},
        {'email': 'bjornwilks@gmail.com', 'password': 'bjornwilks0', 'first_name': 'Bjorn',
         'last_name': 'Wilks', 'description': 'Embarrassed to admit I never paid much attention to school. Want to stop looking bad because of my grammar. Any help?', 'location': 'Glasgow'},
        {'email': 'sosarodriguez@gmail.com', 'password': 'sosarodriguez0', 'first_name': 'Sosa',
         'last_name': 'Rodriguez', 'description': 'New to the site, just looking for now.', 'location': 'Glasgow'},
        {'email': 'floramcgill@gmail.com', 'password': 'floramcgill0', 'first_name': 'Flora',
         'last_name': 'McGill', 'description': 'Know more than anyone in physics. Prove me wrong', 'location': 'Glasgow'},
    ]

    for i in students:
        add_student(i['email'], i['password'], i['first_name'], i['last_name'], i['description'], i['location'],)

    teachers = [
        {'email': 'jarrodmoon@gmail.com', 'password': 'jarrodmoon0', 'first_name': 'Jarrod',
         'last_name': 'Moon', 'description': 'Teaching geometry and trigonometry for 23 years now at a high school. Love my job so much, I want to do it in my free time too!', 'location': 'Glasgow', 'rating': 0,
         'categories': ["Geometry", "Trigonometry"]},
        {'email': 'malakaireader@gmail.com', 'password': 'malakaireader0', 'first_name': 'Malakai',
         'last_name': 'Reader', 'description': 'Yes, I won the national poetry competition in 2004, 2007 and 2016. No, you will probably never be half as good as me. But maybe, if you pay attention, you can still learn something.', 'location': 'Glasgow', 'rating': 0,
         'categories': ["Art", ]},
        {'email': 'shivamallman@gmail.com', 'password': 'shivamallman0', 'first_name': 'Shivam',
         'last_name': 'Allman', 'description': 'Borges said there are only four stories to tell: a love story between two people, a love story between three people, the struggle for power and the voyage. All of us writers rewrite these same stories ad infinitum.', 'location': 'Glasgow', 'rating': 0,
         'categories': ["Storytelling", ]},
        {'email': 'danielatran@gmail.com', 'password': 'danielatran0', 'first_name': 'Daniela',
         'last_name': 'Tran', 'description': 'Phd Biologist, mother and writer of "An illustrated story of biology."', 'location': 'Glasgow', 'rating': 0,
         'categories': ["Biology", ]},
        {'email': 'francescosullivan@gmail.com', 'password': 'francescosullivan0', 'first_name': 'Francesco ',
         'last_name': 'Sullivan', 'description': 'Owner of Francesco\'s, self-made millionaire, philanthropist, visionary...and willing to share my experience and knowledge.', 'location': 'Glasgow', 'rating': 0,
         'categories': ["Entrepreneurship", ]},
        {'email': 'weronikaconolly@gmail.com', 'password': 'weronikaconolly0', 'first_name': 'Weronika',
         'last_name': 'Conolly', 'description': 'You hated algebra as a kid. Maybe now is the time to change your mind? I have been teaching algebra for 14 years and am willing to help both newcomers and more experienced students improve their skills.', 'location': 'Glasgow', 'rating': 0,
         'categories': ["Mathematics", ]},
        {'email': 'ericclark@gmail.com', 'password': 'ericclark0', 'first_name': 'Eric',
         'last_name': 'Clark', 'description': 'Former employee of GoldmanSachs. Expert at macroeconomics.', 'location': 'Glasgow', 'rating': 0,
         'categories': ["Macroeconomics", "Economics", "Microeconomics"]},
        {'email': 'anissabrettr@gmail.com', 'password': 'anissabrett0', 'first_name': 'Anissa',
         'last_name': 'Brett', 'description': 'Painter, artist, free-thinker. Want to help like-minded people achieve their potential and have fun while creating art. “I dream my painting and I paint my dream.” ― Vincent Willem van Gogh ', 'location': 'Glasgow', 'rating': 0,
         'categories': ["Art", ]},
        {'email': 'munalindsey@gmail.com', 'password': 'munalindsey0', 'first_name': 'Muna',
         'last_name': 'Lindsey', 'description': 'History teacher, author of "Ruins and Stories". Apologies if I do not get back to you immediately. “Study the past if you would define the future.”― Confucius ', 'location': 'Glasgow', 'rating': 0,
         'categories': ["History", ]},
        {'email': 'kamilestrada@gmail.com', 'password': 'kamilestrada0', 'first_name': 'Kamil',
         'last_name': 'Estrada', 'description': 'Multilingual: I speak Java, Python, Scala, C++ and Swift. Yes bad jokes come with the teaching I\'m afraid. But I vouch they\'re worth it!', 'location': 'Glasgow', 'rating': 0,
         'categories': ["Programming", ]},
    ]

    for i in teachers:
        add_teacher(i['email'], i['password'], i['first_name'], i['last_name'], i['description'], i['location'], i['rating'], i['categories'])



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
