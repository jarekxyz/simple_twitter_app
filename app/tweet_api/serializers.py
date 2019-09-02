from rest_framework import serializers

from core.models import Tweet


class CreateTweetSerializer(serializers.ModelSerializer):
    """Serialize a tweet for database entry creation"""

    class Meta:
        model = Tweet
        fields = ('id', 'author', 'date_created', 'text', 'tag')
        read_only_fields = ('id',)


class RetrieveTweetSerializer(serializers.ModelSerializer):
    """Serialize a tweet for tag lookup"""

    class Meta:
        model = Tweet
        fields = ('id', 'author', 'date_created', 'text', 'tag')
        read_only_fields = ('id', 'author', 'date_created', 'text', 'tag')
