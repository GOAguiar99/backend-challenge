from django.views.generic import DetailView, ListView
from topic.models import Topic
from post.views import PostListView


class TopicListView(ListView):
    model = Topic


class TopicDetailView(DetailView):
    model = Topic


