from rest_framework import viewsets
from .serializers import PostSerializer
from .models import Post

# Create your views here.
# serialized view using viewsets

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('description')
    serializer_class = PostSerializer