from django.urls import path, include
from rest_framework.routers import DefaultRouter

from tweet_api import views

router = DefaultRouter()
router.register('create', views.CreateTweetView)
router.register('retrieve', views.RetrieveTweetView)

app_name = 'tweet_api'

urlpatterns = [
    path('', include(router.urls)),
    path('count/', views.tweet_count_view, name='count'),
]
