# -*- coding:utf-8 -*-
# @Time: 2020/10/10 11:14
# @Author: Lj
# @File: forms.py

from django import forms
from django.forms.models import inlineformset_factory
from .models import Course, Module

ModuleFormSet = inlineformset_factory(Course,
                                      Module,
                                      fields=['title', 'description'],
                                      extra=2,
                                      can_delete=True)