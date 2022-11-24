from rest_framework.viewsets import ModelViewSet

from api.serializers import PostSerializer, LikeSerializer, CommentSerializer
from posts.models import Post, Comment, Like


class PostView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create()

    def put(self, request, pk):
        self.update()

    def delete(self, request, pk):
        self.destroy()


class LikeView(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create()

    def delete(self, request, pk):
        print(pk)
        self.destroy()


class CommentView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get(self, request):
        return self.list(request)

    def post(self, request):
        return self.create()

    def put(self, request, pk):
        self.update()

    def delete(self, request, pk):
        self.destroy()
