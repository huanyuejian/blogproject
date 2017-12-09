# python3
# coding:utf-8
"""form"""
from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    """CommentForm"""
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
