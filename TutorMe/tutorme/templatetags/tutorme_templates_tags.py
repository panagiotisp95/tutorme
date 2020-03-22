from django import template
from tutorme.models import Category

register = template.Library()


@register.inclusion_tag('tutorme/categories.html')
def get_category_list(current_category=None):
    return {'categories': Category.objects.order_by('-name')[:5], 'current_category': current_category}


@register.simple_tag
def get_at_index(my_list, index):
    return my_list[index]
