from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post, Category, Comment


class PostAdmin(SummernoteModelAdmin):
    date_hierarchy =  'created_date'
    empty_value_display = '-empty-'
    list_display = ('title' ,'author', 'counted_views','login_required', 'status','published_date','created_date')
    list_filter = ('status','author')
    search_fields = ['title','content']
    summernote_fields = ('content',)

class CommentAdmin(admin.ModelAdmin):
    date_hierarchy =  'created_date'
    empty_value_display = '-empty-'
    list_display = ('name' ,'post' ,'approved','updated_date','created_date')
    list_filter = ('approved','post')
    search_fields = ['name','post']

admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
admin.site.register(Post, PostAdmin)
