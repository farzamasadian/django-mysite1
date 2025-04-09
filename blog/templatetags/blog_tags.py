from django import template
from blog.models import Post

register = template.Library()


@register.simple_tag(name='totalposts')
def func():
    posts = Post.objects.filter(status=1)
    return posts.count()

@register.simple_tag(name='posts')
def func():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter
def snippet(value, arg=20):
    return value[:arg]

@register.inclusion_tag('blog/blog-latest-posts.html')
def latest_posts(arg=3):
    posts = Post.objects.filter(status=1).order_by('-published_date')[:arg]
    return {'posts': posts}