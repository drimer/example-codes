from datetime import datetime

from django.shortcuts import render_to_response

from blog.models import BlogPost


def archive(request):
    posts = BlogPost.objects.all().order_by('-timestamp')
    return render_to_response('archive.html',
                              {'posts': posts})
