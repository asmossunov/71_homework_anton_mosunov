from rest_framework.viewsets import ModelViewSet

from api.serializers import PostSerializer

from posts.models import Post


# class PostView(ModelViewSet):
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer

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

# class PostUpdateView(ModelViewSet):


