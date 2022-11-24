from django.urls import path, include
from rest_framework import routers

from api.views import PostView, LikeView, CommentView
from rest_framework.authtoken.views import obtain_auth_token

router = routers.DefaultRouter()
router.register('posts', PostView)
router.register('likes', LikeView)
router.register('comments', CommentView)
urlpatterns = [
    path('', include(router.urls)),
]
