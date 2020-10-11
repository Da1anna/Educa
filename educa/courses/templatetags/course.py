# -*- coding:utf-8 -*-
# @Time: 2020/10/10 22:47
# @Author: Lj
# @File: course.py.py

from django import template

register = template.Library()

@register.filter
def model_name(obj):
    try:
        return obj._meta.model_name
    except AttributeError:
        return None