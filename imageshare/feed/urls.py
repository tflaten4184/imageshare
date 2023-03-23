from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from feed.views import HomeView, PostView, DetailPostView

app_name = 'feed'

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('post', PostView.as_view(template_name="post.html"), name="post"),
    path('detail/<int:pk>/', DetailPostView.as_view(), name="detail"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)