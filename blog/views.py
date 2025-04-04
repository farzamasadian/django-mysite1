from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post

# Create your views here.
def blog_view(request):
    posts = Post.objects.filter(published_date__lte = timezone.now()).order_by('published_date')

    # Update status of posts that have been published
    for post in posts:
        if post.published_date <= timezone.now() and post.status != 1:  
            post.status = 1 
            post.save(update_fields=['status'])
    context = {'posts' : posts}
    return render(request, 'blog/blog-home.html', context)

def blog_single(request, pid):
    post = get_object_or_404(Post, pk=pid, status=1, published_date__lte=timezone.now())

    # Increase counted_view
    post.counted_views += 1
    post.save(update_fields=['counted_views'])

    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)

def test(request, pid):
    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post, pk = pid)
    context = {'post' : post}
    return render(request, 'test.html', context)