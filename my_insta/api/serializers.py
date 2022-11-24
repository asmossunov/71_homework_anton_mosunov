from rest_framework import serializers

from posts.models import Post

from accounts.models import Account

from posts.models import Like


class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = Account
        fields = ('id', 'password', 'last_login', 'is_superuser', 'username', 'first_name',
                  'last_name', 'is_staff', 'is_active', 'date_joined', 'email', 'birthday', 'about_user',
                  'changed_at', 'phone', 'created_at', 'is_deleted', 'avatar', 'gender')
        read_only_fields = ('id', 'gender', 'password', 'created_at', 'updated_at', 'is_deleted')


class LikeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Like
        fields = ('id', 'is_like', 'author', 'changed_at', 'posts', 'created_at',)
        read_only_fields = ('id', 'created_at', 'updated_at', 'is_deleted')


class PostSerializer(serializers.ModelSerializer):
    # posts_likes = LikeSerializer(read_only=True)
    # author = serializers.IntegerField(source='author.id', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'description', 'author', 'comment_count', 'changed_at',
                  'created_at', 'like_count', 'is_deleted', 'image')
        read_only_fields = ('id', 'created_at', 'updated_at', 'posts_likes', 'is_deleted')




