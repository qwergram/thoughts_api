from .models import Photo, Album, PUBLIC
from .forms import NewPhoto, NewAlbum
from rest_framework import permissions
from .serializers import PhotoSerializer, AlbumSerializer
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
import json
from django.views.decorators.csrf import csrf_exempt


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = json.dumps(data, indent=2)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


@csrf_exempt
def root(request):
    if request.user.is_authenticated():
        if request.method == 'GET':
            photos = Photo.objects.filter(published=PUBLIC).order_by("-date_uploaded")
            serializer = PhotoSerializer(photos, many=True)
            return JSONResponse(serializer.data)
        elif request.method == 'POST':
            photo = NewPhoto(request.POST, request.FILES)
    return JSONResponse({'error': 'please login'}, status=403)

@csrf_exempt
def photo(request):
    if request.user.is_authenticated():
        if request.method == 'GET':
            photos = Photo.objects.filter(published=PUBLIC).order_by("-date_uploaded")
            serializer = PhotoSerializer(photos, many=True)
            return JSONResponse(serializer.data)
    return JSONResponse({'error': 'please login'}, status=403)


@csrf_exempt
def album(request):
    if request.user.is_authenticated():
        if request.method == 'GET':
            albums = Album.objects.filter(published=PUBLIC).order_by("-date_uploaded")
            serializer = AlbumSerializer(albums, many=True, context={'request': request})
            return JSONResponse(serializer.data)
    return JSONResponse({'error': 'please login'}, status=403)
