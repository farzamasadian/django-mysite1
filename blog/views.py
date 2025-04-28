from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage, InvalidPage
from blog.models import Post


def blog_view(request, **kwargs):
    """
    Renders the blog homepage with optional category or author filters, and paginates the posts.

    Keyword Args:
        cat_name (str): Filter posts by category name.
        author_username (str): Filter posts by author's username.

    Template:
        blog/blog-home.html

    Context:
        posts (Page): A paginated list of filtered blog posts.
    """
    # Get all published and active posts up to now
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date')

    # Filter by category if provided
    if kwargs.get('cat_name') is not None:
        posts = posts.filter(category__name=kwargs['cat_name'])

    # Filter by tag if provided
    if kwargs.get('tag_name') is not None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])

    # Filter by author if provided
    if kwargs.get('author_username') is not None:
        posts = posts.filter(author__username=kwargs['author_username'])

    # Paginate posts (3 per page)
    posts = Paginator(posts, 3)
    page_number = request.GET.get('page')

    try:
        posts = posts.page(page_number)
    except (PageNotAnInteger, EmptyPage, InvalidPage):
        # Default to first page if error occurs
        posts = posts.page(1)

    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_single(request, pid):
    """
    Displays a single blog post by its primary key (pid), updates view count,
    and determines the previous and next posts for navigation.

    Args:
        pid (int): Primary key of the blog post.

    Template:
        blog/blog-single.html

    Context:
        post (Post): The current blog post.
        prev_post (Post | None): The previous blog post, if it exists.
        next_post (Post | None): The next blog post, if it exists.
    """
    # Retrieve the post or return 404 if not found or unpublished
    post = get_object_or_404(Post, pk=pid, status=1, published_date__lte=timezone.now())

    # Increment view count
    post.counted_views += 1
    post.save(update_fields=['counted_views'])

    # Get list of all published posts for prev/next logic
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date')
    post_list = list(posts)
    current_index = post_list.index(post)

    # Determine previous and next posts
    prev_post = post_list[current_index - 1] if current_index > 0 else None
    next_post = post_list[current_index + 1] if current_index < len(post_list) - 1 else None

    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post
    }
    return render(request, 'blog/blog-single.html', context)


def blog_search(request):
    """
    Filters blog posts by a search term in the content.

    GET Params:
        s (str): The search term to filter posts by content.

    Template:
        blog/blog-home.html

    Context:
        posts (QuerySet): List of posts matching the search criteria.
    """
    # Base queryset of published posts
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())

    if request.method == 'GET':
        if s := request.GET.get('s'):  # Walrus operator for cleaner assignment
            posts = posts.filter(content__icontains=s)

    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def test(request):
    """
    Renders a test template (used for development/testing purposes).

    Template:
        test.html
    """
    return render(request, 'test.html')
