from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view

from django.http import JsonResponse

from core.models import Tweet

from tweet_api import serializers


@api_view()
def tweet_count_view(request):
    """Retrieve per year tweet count for given time frame and tag"""
    start = int(request.query_params.get('from'))
    end = int(request.query_params.get('till'))
    tag = request.query_params.get('tag', default=0)
    if start and end:
        queryset = Tweet.objects.all().filter(
            date_created__year__gte=str(start),
            date_created__year__lte=str(end))
        count = dict()
        for i in range(start, end + 1):
            if tag:
                count[i] = queryset.filter(date_created__year=i,
                                           tag=str(tag)).count()
            else:
                count[i] = queryset.filter(date_created__year=i).count()
        return JsonResponse(count)


class CreateTweetView(viewsets.ModelViewSet):
    """Create new tweet"""
    serializer_class = serializers.CreateTweetSerializer
    queryset = Tweet.objects.all().order_by('-date_created')
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)


class RetrieveTweetView(viewsets.ModelViewSet):
    """Retrieve tweets with given tag"""
    # serializer_class = serializers.BaseSerializer
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
