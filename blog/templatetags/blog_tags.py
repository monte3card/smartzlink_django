from django import template
from ..models import Post, Category, Tag
from django.db.models.aggregates import Count

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]

@register.simple_tag
def archives():
    return Post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def getx_categorie():
    # 别忘了在顶部引入 Category 类
    return Category.objects.all()

@register.simple_tag
def show_categories():
    category_list = Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    return category_list

@register.simple_tag
def show_tags():
    tag_list = Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)
    return tag_list
