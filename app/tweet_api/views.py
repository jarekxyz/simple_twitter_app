from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, \
                                       permission_classes

from django.http import JsonResponse, HttpResponseBadRequest

from core.models import Tweet

from tweet_api import serializers


@api_view()
@authentication_classes((TokenAuthentication,))
@permission_classes((IsAuthenticated,))
def tweet_count_view(request):
    """Retrieve tweet count per year for given time frame and tag"""
    start = int(request.query_params.get('from', default=0))
    end = int(request.query_params.get('till', default=0))
    tag = request.query_params.get('tag', default=0)
    if start and end:
        kwargs = {'date_created__year__gte': str(start),
                  'date_created__year__lte': str(end)}
        if tag:
            kwargs['tag'] = tag
        queryset = Tweet.objects.all().filter(**kwargs)
        count = {key: 0 for key in range(start, end + 1)}
        for object in queryset:
            count[object.date_created.year] += 1
        return JsonResponse(count)
    else:
        return HttpResponseBadRequest("Incorrect or missing parameters")


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
