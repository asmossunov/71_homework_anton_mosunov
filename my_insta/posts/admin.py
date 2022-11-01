from django.contrib import admin

from posts.models import Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'description', 'comment_count', 'like_count', 'created_at', 'changed_at')
    list_filter = ('id', 'author', 'description', 'comment_count', 'like_count', 'created_at', 'changed_at')
    search_fields = ('id', 'author', 'description', 'comment_count', 'like_count', 'created_at', 'changed_at')
    fields = ('author', 'description', 'comment_count', 'like_count')
    readonly_fields = ('id',)


class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'author', 'post', 'text', 'created_at', 'changed_at')
    list_filter = ('id', 'author', 'post', 'text', 'created_at', 'changed_at')
    search_fields = ('id', 'author', 'post', 'text', 'created_at', 'changed_at')
    fields = ('id', 'author', 'post', 'text')
    readonly_fields = ('id',)


admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
