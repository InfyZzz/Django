from django.shortcuts import render
from django.views.generic import View
from .models import Post, Tag
from django.shortcuts import get_object_or_404
from .forms import TagForm
from django.shortcuts import redirect

def posts_list(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', context={'posts': posts})


def tags_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tags_list.html', context={'tags': tags})


#def post_detail(request, slug):
 #   post = Post.objects.get(slug__iexact=slug)
  #  return render(request, 'blog/post_detail.html', context={'post': post})


class PostDetail(View):
    def get(self, request, slug):
        # post = Post.objects.get(slug__iexact=slug)
        post = get_object_or_404(Post, slug__iexact=slug)
        return render(request, 'blog/post_detail.html', context={'post': post})


class TagDetail(View):
    def get(self, request, slug):
        # tag = Tag.objects.get(slug__iexact=slug)
        tag = get_object_or_404(Tag, slug__iexact=slug)
        return render(request, 'blog/tag_detail.html', context={'tag': tag})


#def tag_detail(request, slug):
 #   tag = Tag.objects.get(slug__iexact=slug)
  #  return render(request, 'blog/tag_detail.html', context={'tag': tag})


class TagCreate(View):

    def get(self, request):
        form = TagForm()
        return render(request, 'blog/tag_create.html', context={'form': form})

    def post(self, request):
        bound_form = TagForm(request.POST)

        if bound_form.is_valid():
            new_tag = bound_form.save()
            return redirect(new_tag)
        return render(request, 'blog/tag_create.html', context={'form': bound_form})






















