# -*- coding: utf-8 -*-

#/////////////////////////////////////////////////////////////////
from django.contrib import admin
#-----------------------------------------------------------------
from lightyblog.models import Article

#/////////////////////////////////////////////////////////////////
# Enalbed for easy debugging, while coding 
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'message', 'is_approved', 'created')
    ordering = ('-created',)
admin.site.register(Article, ArticleAdmin)

