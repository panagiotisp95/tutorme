import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'tango_with_django_project.settings')

import django
django.setup()
from tutorme.models import Category


def populate():
    # First, we will create lists of dictionaries containing the pages
    # we want to add into each category.
    # Then we will create a dictionary of dictionaries for our categories. # This might seem a little bit confusing, but it allows us to iterate # through each data structure, and add the data to our models.
    python_pages = [
        {'title': 'Official Python Tutorial', 'url': 'http://docs.python.org/3/tutorial/', 'views': 15},
        {'title': 'How to Think like a Computer Scientist', 'url': 'http://www.greenteapress.com/thinkpython/', 'views': 239},
        {'title': 'Learn Python in 10 Minutes', 'url': 'http://www.korokithakis.net/tutorials/python/', 'views': 98}
    ]
    django_pages = [
        {'title': 'Official Django Tutorial', 'url': 'https://docs.djangoproject.com/en/2.1/intro/tutorial01/', 'views': 67},
        {'title': 'Django Rocks', 'url': 'http://www.djangorocks.com/', 'views': 156},
        {'title': 'How to Tango with Django', 'url': 'http://www.tangowithdjango.com/', 'views': 190}
    ]

    other_pages = [
        {'title': 'Bottle', 'url': 'http://bottlepy.org/docs/dev/', 'views': 154},
        {'title': 'Flask', 'url': 'http://flask.pocoo.org', 'views': 13}
    ]

    cats = {
        'Python': {'pages': python_pages, 'views': 64, 'likes': 12},
        'Django': {'pages': django_pages, 'views': 53, 'likes': 67},
        'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16}
    }

    # If you want to add more categories or pages,
    # add them to the dictionaries above.

    # The code below goes through the cats dictionary, then adds each category,
    #  and then adds all the associated pages for that category.
    for cat, cat_data in cats.items():
        add_cat(cat, cat_data['views'], cat_data['likes'])

    # Print out the categories we have added.
    for c in Category.objects.all():
        print(f'- {c}')


def add_cat(name, views, likes):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c


# Start execution here!
if __name__ == '__main__':
    print('Starting TutorMe population script...')
    populate()
