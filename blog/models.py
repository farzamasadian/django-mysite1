from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Category(models.Model):
    """
    Represents a blog post category.
    Each post can be assigned to one or more categories.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Represents a blog post with fields for title, content, image, author, categories, and metadata.
    """
    title = models.CharField(max_length=255)  # Title of the post
    content = models.TextField()  # Main body of the post
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')  # Cover image for the post
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)  # Author of the post (User)
    category = models.ManyToManyField(Category)  # Many-to-many relationship with Category

    counted_views = models.IntegerField(default=0)  # Number of times the post has been viewed
    status = models.BooleanField(default=False)  # Published status (True = published)
    created_date = models.DateTimeField(auto_now_add=True)  # Automatically set when the post is created
    updated_date = models.DateTimeField(auto_now=True)  # Automatically set when the post is updated
    published_date = models.DateTimeField(null=True)  # Date and time when the post is published

    class Meta:
        ordering = ['created_date']  # Default ordering: oldest first

    def __str__(self):
        return f"{self.id} - {self.title}"  # Readable string representation for admin panel, etc.

    # Optional helper method for previewing a post snippet
    # def snippets(self):
    #     return self.content[:100] + ' ...'

    def get_absolute_url(self):
        return reverse('blog:single', kwargs={'pid':self.id})