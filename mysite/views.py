from django.shortcuts import render
from mysite.models import Post
from django.http import HttpResponse

def homepage(request):
    posts = Post.objects.all()
    post_lists = list()
    for count, post in enumerate(posts):
        post_lists.append(f"No... {count}: {post} <br>")
        #         post_lists.append("No. {}:".format(str(count)) + str(post) + "<br>")
    return HttpResponse(post_lists)

# Create your views here.
