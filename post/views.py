from django.views.generic import DetailView, ListView
from post.models import Post


class PostListView(ListView):
    model = Post


class PostDetailView(DetailView):
    model = Post
