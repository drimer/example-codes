from datetime import datetime

from django.shortcuts import render_to_response

from blog.models import BlogPost


def archive(request):
    post = BlogPost(title='Mock title', body='Mock body',
                    timestamp=datetime.now())
    return render_to_response('archive.html',
                              {'posts': [post]})
