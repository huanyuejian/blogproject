# python3
# coding:utf-8
"""blog tags"""
from django import template
from ..models import Post, Category

register = template.Library()


@register.simple_tag
def get_recent_posts(num=5):
    """get_recent_posts"""
    return Post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    """archives"""
    return Post.objects.dates('created_time', 'month', order='DESC')


@register.simple_tag
def get_categories():
    """get_categories"""
    return Category.objects.all()
