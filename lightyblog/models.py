# -*- coding: utf-8 -*-

#/////////////////////////////////////////////////////////////////
from django.db import models
#-----------------------------------------------------------------
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

#/////////////////////////////////////////////////////////////////
# Articles
class Article(models.Model):

    """
        Minimalistic class that models a blogging article post.
        Only very basic fields were added, since it is just PoC. 
    """
  
    # Relate each article with a user     
    owner = models.ForeignKey(User, verbose_name = _(u'User'), related_name='article_owner')
    
    # Article basic information
    title = models.CharField(max_length=70, verbose_name = _(u'Title'))
    message = models.TextField(verbose_name = _(u'Article text'))
    created = models.DateField(verbose_name = _(u'Creation date'), auto_now_add=True)

    # Only approved posts will be visible
    is_approved = models.BooleanField(default=False, verbose_name = _(u'Approve articles'))

    # Some naming
    class Meta:
        verbose_name = _(u'Lightyblog articles')
        verbose_name_plural = _(u'Lightyblog articles')
    
    def __unicode__(self):
        return self.title
