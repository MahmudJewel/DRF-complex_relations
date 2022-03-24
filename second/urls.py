from django.urls import path, include
from second.views import home_view
from second.views import post_viewset, comment_viewset

# router 
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('/pst', post_viewset, basename='pst')
router.register('/comment', comment_viewset, basename='comment')

urlpatterns = [
    path('', home_view.as_view(), name='home'),
    
    path('api', include(router.urls))
]