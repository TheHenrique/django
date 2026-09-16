from django.shortcuts import render
from django.views import generic

from blog.post import Post


class PostView(generic.View):
    def get(self, request, *args, **kwargs):
        post_list = Post.objects.filter(status=1)
        return render(request, 'index.html', {'post_list': post_list})