# -*- coding: utf-8 -*-

import datetime
#/////////////////////////////////////////////////////////////////
from django import forms
from django.conf import settings
from django.utils.timezone import utc 
#-----------------------------------------------------------------
from lightyblog.models import Article

#/////////////////////////////////////////////////////////////////
class ArticleForm(forms.Form):
    """
        Very basic form that will allow creation of new articles.
    """

    # Article details
    # Captcha is recommended for avoiding muplitple entries being posted.
    title = forms.CharField(max_length=70, min_length=10, required=True)
    message = forms.CharField(widget=forms.Textarea)   
    is_approved = forms.BooleanField(required=False)


#/////////////////////////////////////////////////////////////////
def save_article(us,ti,me,ap):
    """
        Basic method to save a new article. Error handling can be 
        optimized to be more, user friendly. Logging for debugging.
    """

    # Create django date for storing article 
    cr = datetime.datetime.utcnow().replace(tzinfo=utc)
    
    # Advance error handing would be advised here.
    try: 
        msg = Article(owner=us, title=ti, message=me, is_approved=ap, created=cr)
        msg.save()
        return True
    except:
        return False


#/////////////////////////////////////////////////////////////////
# Returns article's existing details
def get_article(articleid):
    """
        Basic method to get data from database for editing an article.
        Error handling can be optimized further. Logging for debugging.
    """
    
    # Initialize 
    form = None

    # Get the article object based on id.
    try:
        article = Article.objects.get(id=articleid)
        
        # Generate form with database data
        form = ArticleForm(initial = {
            'title': article.title,
            'message': article.message,
            'is_approved': article.is_approved, 
        })

    except:
        # Loggin + correct error handling should be added. 
        pass
    
    return form


#/////////////////////////////////////////////////////////////////
# Update the article.
def update_article(article,ti,me,ap):
    """
        Basic method for applying changes / updating an article.
        Error handling can be optimized further. Logging for debugging.
    """

    # Create django date for uddating article 
    up = datetime.datetime.utcnow().replace(tzinfo=utc)
 
    # Apply changes and save 
    try:
        article.title = ti
        article.message = me
        article.is_approved = ap
        article.created = up   
        article.save()
        return True
    except:
        # Loggin + correct error handling should be added. 
        return False


#/////////////////////////////////////////////////////////////////
# Delete the article.
def delete_article(article):
    """
        Basic method for deleting an article.
        Logging for debugging.
    """
    
    try:
        article.delete()
        return True
    except:
        # Loggin + correct error handling should be added. 
        return False

