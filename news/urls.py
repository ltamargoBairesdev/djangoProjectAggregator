# news/urls.py

from django.urls import path

from .views import *

urlpatterns = [
    path("", SourceFormView.as_view(), name='homepage'),
    path("news/", NewsPageView.as_view(), name="news"),
    path("views/", ViewsPageView.as_view(), name="views"),
    path("incrementViews/<int:news_id>/", IncrementViewsRedirectView.as_view(), name='increment-views'),
]