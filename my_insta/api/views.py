from rest_framework.viewsets import ModelViewSet

from api.serializers import PostSerializer

from posts.models import Post


class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
