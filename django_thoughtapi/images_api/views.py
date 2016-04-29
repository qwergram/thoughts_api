from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Photo, Album, PUBLIC
from .forms import EditProfile

# Create your views here.


@login_required
def library_view(request):
    return render(
        request,
        "images_api/index.html",
        {
            "title": "{} - Library View".format(request.user.first_name),
            "content": "There are currently {} photos.".format(len(Photo.objects.all())),
            "images": Photo.objects.filter(published=PUBLIC).order_by("-date_uploaded")[:10],
        }
    )


@login_required
def album_view(request, album_id=None):
    if album_id:
        album = get_object_or_404(Album, id=int(album_id))
        return render(
            request,
            "images_api/index.html",
            {
                "title": album.title,
                "content": "Album by {}<br/>{} ".format(album.owner.username, album.description),
                "images": album.photos.all(),
            }
        )
    else:
        return render(
            request,
            "images_api/index.html",
            {
                "title": "Albums",
                "content": "There are currently {} Albums.".format(len(Album.objects.all())),
                "images": Album.objects.filter(published=PUBLIC),
            }
        )


@login_required
def photo_view(request, photo_id=None):
    if photo_id:
        photo = get_object_or_404(Album, id=int(photo_id))
        return render(
            request,
            "images_api/index.html",
            {
                "title": photo.title,
                "content": "Photo by {}<br/>{} ".format(photo.owner.username, photo.description),
                "images": [photo]
            }
        )
    else:
        return render(
            request,
            "images_api/index.html",
            {
                "title": "Photos".format(request.user.first_name),
                "content": "There are currently {} photos.".format(len(Photo.objects.all())),
                "images": Photo.objects.filter(owner=request.user).order_by("-date_uploaded"),
            }
        )


@login_required
def album_add(request):
    raise Http404


@login_required
def photo_add(request):
    raise Http404


@login_required
def profile_view(request, profile_id=None):
    if profile_id is None:
        user = request.user
        return render(
            request,
            "images_api/index.html",
            {
                "title": "{} {} ({})".format(user.first_name, user.last_name, user.username),
                "content": "Titan has uploaded {} photos.".format(len(Photo.objects.filter(owner=user))),
                "images": Photo.objects.filter(owner=user),
            }
        )
    else:
        user = get_object_or_404(settings.AUTH_USER_MODEL, pk=profile_id)
        return render(
            request,
            "images_api/index.html",
            {
                "title": "{} {} ({})".format(user.first_name, user.last_name, user.username),
                "content": "Titan has uploaded {} photos.".format(len(Photo.objects.filter(owner=user))),
                "images": Photo.objects.filter(owner=user).filter(published=PUBLIC),
            }
        )
