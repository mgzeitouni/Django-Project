from django import template

from tango_with_django_project.templates.rango.rango import Category

register = template.Library()

@register.inclusion_tag('rango/cats.html')
def get_category_list():
    return {'cats': Category.objects.all()}