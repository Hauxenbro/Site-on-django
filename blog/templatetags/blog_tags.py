from django import template
from django.db.models import F
from django.db.models.aggregates import Count
from blog.models import Category

register = template.Library()
@register.inclusion_tag('blog/list_cats.html')
def show_categories():
    categories = Category.objects.annotate(cnt=Count('article', filter=F('article__is_published'))).filter(cnt__gt=0)
    return {'categories':categories}