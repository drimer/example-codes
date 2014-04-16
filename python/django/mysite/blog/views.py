from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from blog.models import BlogPost, BlogPostForm


def archive(request):
    posts = BlogPost.objects.all()
    return render_to_response('archive.html',
                              {'posts': posts, 'form' : BlogPostForm()},
                              RequestContext(request))


def create_blogpost(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.timestamp = datetime.now()
            post.save()

    return HttpResponseRedirect('/blog/')
