from rest_framework import serializers
from .models import Photo, Album


class PhotoSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    owner = serializers.CharField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    published = serializers.BooleanField()
    date_uploaded = serializers.DateTimeField(read_only=True)
    photo = serializers.ImageField()

    def create(self, validated_data):
        return Photo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.published = validated_data.get('published', instance.published)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()
        return instance


class AlbumSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    owner = serializers.CharField(read_only=True)
    title = serializers.CharField()
    description = serializers.CharField()
    published = serializers.BooleanField()
    date_uploaded = serializers.DateTimeField(read_only=True)
    photo = serializers.ImageField()

    photos = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='api:photo',
        read_only=True,
    )

    def create(self, validated_data):
        return Album.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.published = validated_data.get('published', instance.published)
        instance.photo = validated_data.get('photo', instance.photo)
        instance.save()
        return instance
