from django.urls import path, include
from rest_framework import routers
from .views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet


router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register(
    r'posts/(?P<post_id>[\d]+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register('groups', GroupViewSet)
router.register('follow', FollowViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
