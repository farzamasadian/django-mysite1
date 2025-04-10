from django import template
from blog.models import Post, Category

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

@register.inclusion_tag('blog/blog-category.html')
def post_category():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict={}
    for cat in categories:
        cat_dict[cat] = posts.filter(category = cat).count()

    return {'categories': cat_dict}