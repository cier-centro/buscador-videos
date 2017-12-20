from django.conf.urls import url, include

from views import VideoListView

urlpatterns = [
    url('^api/v1/videolist$', VideoListView.as_view()),
]