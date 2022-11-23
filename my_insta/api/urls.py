from django.urls import path, include
from rest_framework import routers

from api.views import PostView

router = routers.DefaultRouter()
router.register('posts', PostView)
urlpatterns = [
    path('', include(router.urls)),
]
