from django.shortcuts import render, get_object_or_404
from django.views import generic

from blog.post import Post


class PostDetailView(generic.View):
    def get(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug, status=1)
        return render(request, 'post_detail.html', {'post': post})