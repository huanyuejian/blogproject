# python3
# coding:utf-8
"""feed"""
from django.contrib.syndication.views import Feed

from .models import Post


class AllPostsRssFeed(Feed):
    title = "huanyuejian's blog"

    link = "/"

    description = "blogs"

    def item(self):
        return Post.objects.all()

    def item_title(self, item):
        return '[%s] %s' % (item.category, item.title)

    def item_description(self, item):
        return item.body
