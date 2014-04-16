from datetime import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response

from blog.models import BlogPost


def archive(request):
    posts = BlogPost.objects.all()
    return render_to_response('archive.html',
                              {'posts': posts})


def create_blogpost(request):
    if request.method == 'POST':
        post = BlogPost(title=request.POST.get('title'),
                        body=request.POST.get('body'),
                        timestamp=datetime.now())
        post.save()

    return HttpResponseRedirect('/blog/')
