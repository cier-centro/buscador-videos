from rest_framework import serializers

from models import Video, Tag, Subject


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag',)

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subject
        fields = ('subject', 'time',)

class VideoSerializer(serializers.ModelSerializer):
    tags =TagSerializer(many=True, read_only=True)
    subjects = SubjectSerializer(many=True, read_only=True)
    class Meta:
        model = Video
        fields = ('id', 'title', 'url', 'date', 'lenght', "tags", "subjects")