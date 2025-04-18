from django.urls import path
from blog.views import *

# This namespace is used for reverse URL resolution, e.g. {% url 'blog:index' %}
app_name = 'blog'

urlpatterns = [
    # Blog homepage — shows all published posts (optionally filtered by category/author if used)
    path('', blog_view, name='index'),

    # Single blog post by primary key (pid)
    path('<int:pid>', blog_single, name='single'),

    # Filter posts by category name
    path('category/<str:cat_name>', blog_view, name='category'),

    # Filter posts by author username
    path('author/<str:author_username>', blog_view, name='author'),

    # Search posts using a query string (?s=...)
    path('search/', blog_search, name='search'),

    # Test route for development/debugging template rendering
    path('test', test, name='test'),
]
