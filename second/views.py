from django.shortcuts import render
from django.views import View
from django.http import HttpResponse

from rest_framework import viewsets
from second.serializers import PostSerializer , CommentSerializer
from second.models import Post, Comment

# Create your views here.

class home_view(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')


class post_viewset(viewsets.ModelViewSet):
	"""
	This viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
	"""
	serializer_class = PostSerializer
	queryset = Post.objects.all()


class comment_viewset(viewsets.ModelViewSet):
	"""
	This viewset automatically provides `list`, `create`, `retrieve`, `update` and `destroy` actions.
	"""
	serializer_class = CommentSerializer
	queryset = Comment.objects.all()