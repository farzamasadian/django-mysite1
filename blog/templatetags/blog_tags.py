from django import template
from blog.models import Post, Category
from django.utils import timezone

register = template.Library()

@register.simple_tag(name='totalposts')
def func():
    """
    Returns the total number of active (published) posts.
    """
    posts = Post.objects.filter(status=1)
    return posts.count()


@register.simple_tag(name='posts')
def func():
    """
    Returns a queryset of all active (published) posts.
    """
    posts = Post.objects.filter(status=1)
    return posts


@register.filter
def snippet(value, arg=20):
    """
    Truncates the input string to the first 'arg' characters.

    Args:
        value (str): The string to truncate.
        arg (int): Number of characters to return (default is 20).

    Returns:
        str: Truncated string.
    """
    return value[:arg]


@register.inclusion_tag('blog/blog-latest-posts.html')
def latest_posts(arg=3):
    """
    Returns the latest blog posts to be included in a template.

    Args:
        arg (int): Number of posts to return (default is 3).

    Returns:
        dict: A dictionary with the latest posts under the key 'posts'.
    """
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-latest-posts-horizontal.html')
def latest_posts_horizontal(arg=6):
    """
    Returns the latest blog posts for horizontal-style display.

    Args:
        arg (int): Number of posts to return (default is 6).

    Returns:
        dict: A dictionary with the latest posts under the key 'posts'.
    """
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date')[:arg]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-category.html')
def post_category():
    """
    Returns a dictionary of categories with their corresponding active post counts.

    Returns:
        dict: A dictionary with categories as keys and post counts as values.
              Used to display blog categories and their number of posts.
    """
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}

    for cat in categories:
        # Count the number of posts in each category
        cat_dict[cat] = posts.filter(category=cat).count()

    return {'categories': cat_dict}
