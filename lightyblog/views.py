# -*- coding: UTF-8 -*-

#///////////////////////////////////////////////////
from django.shortcuts import render
from django.http import Http404
from django.conf import settings
from django.contrib.auth.decorators import login_required
#---------------------------------------------------
from lightyblog.models import Article
from lightyblog.forms import ArticleForm
from lightyblog.forms import save_article, get_article
from lightyblog.forms import delete_article, update_article


#///////////////////////////////////////////////////
# The presentation link template
def index(request):
    """
        A view that was added only for presentation context, that aims
        to help the developers to understand the reason of creating the 
        Lightyblog demo-app.
    """

    return render(request, 'core/index.html')


#///////////////////////////////////////////////////
# Preview of articles based on id, sidebar indexing
def article(request, articleid):
    """
        Articles view that returns the 10 latest articles.
        If an exception is raised, then it returns a 404 error (for now).
        Logging should be added in order to catch the exception errors.
        Preview item becomes, the chosen id.
    """
    try:
        # Logic can be optimized, if it was production code (TODOs - use get(id) instead).
        articles = Article.objects.all().filter(is_approved=True).order_by('-created')[:10]
        preview = Article.objects.all().filter(id=articleid)[:1]
        return render(request, 'core/articles.html', { 'preview':preview, 'articles':articles },) 
    except:
        raise Http404


#///////////////////////////////////////////////////
# Preview the latest article
def latest(request):
    """
        Articles view that returns the 10 latest articles.
        If an exception is raised, then it returns a 404 error (for now).
        Logging should be added in order to catch the exception errors.
        Preview item becomes, the 3 latest articles.
    """

    try:
        articles = Article.objects.all().filter(is_approved=True).order_by('-created')[:10]
        preview = Article.objects.all().filter(is_approved=True).order_by('-created')[:6]
        return render(request, 'core/articles.html', { 'preview':preview, 'articles':articles },) 
    except:
        # It should be logging instead (404 debugging reasons)
        raise Http404


#/////////////////////////////////////////////////////////////////
@login_required
def create(request):
    """
        Custom view that create a new article.
    """

    # Initialize
    title = message = ''
    is_approved = False 

    # Create the article form
    form = ArticleForm()
    
    # Check for post request
    if request.method == 'POST': 
            
        form = ArticleForm(request.POST)
        if form.is_valid(): 
            
            # Getting User's Input           
            title = form.cleaned_data['title']
            message = form.cleaned_data['message']
            is_approved = form.cleaned_data['is_approved']
            
            # Save article
            success = save_article(request.user,title,message,is_approved)   
  
            if success:
                return render(request, 'adminpanel/create.html', { 'form':form, 'success':success},)
    
    # Return initial form
    return render(request, 'adminpanel/create.html', {'form': form, })


#/////////////////////////////////////////////////////////////////
@login_required
def edit(request, articleid):
    """
        Custom view that edits the article based on id.
    """

    # Initialize 
    post = form = None 
 
    try:
        post = Article.objects.get(id=articleid)
        form = get_article(articleid)
    except:
        # It should be logging instead (debugging reasons)
        pass

    # The concept of restricting someone to edit, it not the owner
    # but get the article id by viewing the source.
    # Obviously, that's a fast way to do it
    if request.user.id != post.owner.id:
        raise Http404
    
    # Check for post request
    if request.method == 'POST': 
            
        form = ArticleForm(request.POST)

        if form.is_valid(): 
            
            # Getting User's Input           
            title = form.cleaned_data['title']
            message = form.cleaned_data['message']
            is_approved = form.cleaned_data['is_approved']
            
            # Update article
            success = update_article(post,title,message,is_approved)   
  
            if success:
                return render(request, 'adminpanel/edit.html', { 'form':form, 'post':post, 'success':success},)

    return render(request, 'adminpanel/edit.html', { 'form':form, 'post':post, })


#/////////////////////////////////////////////////////////////////
@login_required
def delete(request, articleid):
    """
        Custom view that deletes the article based on id.
        Could add confirmation before deleting, but I just decided 
        to keep it simple.
    """
    
    # Initialize 
    post = None 
    success = False 

    try:
        post = Article.objects.get(id=articleid)
    except:
        # It should be logging (debugging reasons)
        pass
  
    # The idea of restricting someone to edit, it not the owner
    # but get the article id by viewing the source.
    # Obviously, that's a fast way to do it.
    if request.user.id != post.owner.id:
        raise Http404
    else:
        success = delete_article(post)

    return render(request,'adminpanel/delete.html', { 'post':post, 'success':success, })


#/////////////////////////////////////////////////////////////////
@login_required
def list(request):
    """
        Custom view that lists all user's articles.
    """

    try:
        posts = Article.objects.all().filter(owner__id=request.user.id)
    except:
        # It should be logging instead (404 debugging reasons)
        raise Http404
    
    return render(request,'adminpanel/list.html', { 'posts':posts, })
