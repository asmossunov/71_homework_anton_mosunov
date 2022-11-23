from rest_framework import serializers

from posts.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.username', max_length=200)

    class Meta:
        model = Post
        fields = ('id', 'description', 'author_id', 'comment_count', 'changed_at',
                  'created_at', 'like_count', 'is_deleted', 'image')
        read_only_fields = ('id', 'author_id', 'created_at', 'updated_at', 'is_deleted')

