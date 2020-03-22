from django import template
from tutorme.models import Category

register = template.Library()


@register.inclusion_tag('tutorme/categories.html')
def get_category_list(current_category=None):
    return {'categories': Category.objects.order_by('-name')[:5], 'current_category': current_category}


# Function that returns the value stored in the list given an index
# Used to get the rating of a teacher in the dashboard inside a for loop
@register.simple_tag
def get_at_index(my_list, index):
    return my_list[index]
