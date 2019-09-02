from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tweet

from tweet_api import serializers


class CreateTweetView(viewsets.ModelViewSet):
    """Create new tweet"""
    serializer_class = serializers.CreateTweetSerializer
    queryset = Tweet.objects.all().order_by('-date_created')
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class RetrieveTweetView(viewsets.ModelViewSet):
    """Retrieve tweets with given tag"""
    serializer_class = serializers.RetrieveTweetSerializer
    queryset = Tweet.objects.all().order_by('-date_created')
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """Return objects for the current authenticated user only"""
        tag = self.request.query_params.get('tag')
        queryset = self.queryset
        if tag:
            return queryset.filter(tag=tag).order_by('-date_created')
        else:
            return queryset.filter(tag=None)
