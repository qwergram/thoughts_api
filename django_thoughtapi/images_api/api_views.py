from .models import Photo, Album, PUBLIC
from .forms import NewPhoto, NewAlbum
from .serializers import PhotoSerializer, AlbumSerializer
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout


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
    return JSONResponse({'error': 'please login @ /api/v1/login/'}, status=403)

@csrf_exempt
def photo(request):
    if request.user.is_authenticated():
        if request.method == 'GET':
            photos = Photo.objects.filter(published=PUBLIC).order_by("-date_uploaded")
            serializer = PhotoSerializer(photos, many=True)
            return JSONResponse(serializer.data)
    return JSONResponse({'error': 'please login @ /api/v1/login/'}, status=403)


@csrf_exempt
def album(request):
    if request.user.is_authenticated():
        if request.method == 'GET':
            albums = Album.objects.filter(published=PUBLIC).order_by("-date_uploaded")
            serializer = AlbumSerializer(albums, many=True, context={'request': request})
            return JSONResponse(serializer.data)
    return JSONResponse({'error': 'please login @ /api/v1/login/'}, status=403)


@csrf_exempt
def login(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            return JSONResponse({'status': 'success'})
        else:
            return JSONResponse({'status': 'account is no longer active'})
    else:
        return JSONResponse({'status': 'invalid login'})


@csrf_exempt
def logout(request):
    logout(request)
    return JSONResponse({'status': 'success'})
