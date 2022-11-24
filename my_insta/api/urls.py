from django.urls import path, include
from rest_framework import routers

from api.views import PostView, LikeView

router = routers.DefaultRouter()
router.register('posts', PostView)
router.register('likes', LikeView)
urlpatterns = [
    path('', include(router.urls)),
]
