from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from .models import Photo, Album, PUBLIC
from .forms import EditProfile, NewPhoto, NewAlbum

# Create your views here.


def temporary_root(request):
    return redirect('images:library')


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
        photo = get_object_or_404(Photo, id=int(photo_id))
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
    if request.method == 'POST':

        form = NewAlbum(request.user, request.POST, request.FILES, instance=Album(owner=request.user))
        if form.is_valid():
            form.owner = request.user
            album = form.save()
            return redirect("images:album_view", album_id=album.id)
    else:
        form = NewAlbum(request.user)

    return render(
        request,
        "images_api/photo.html",
        {
            "form": form,
        }
    )


@login_required
def photo_add(request):
    if request.method == 'POST':
        form = NewPhoto(request.POST, request.FILES)
        if form.is_valid():
            photo = Photo(
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                published=form.cleaned_data['published'],
                photo=form.cleaned_data['photo'],
            )
            photo.owner = request.user
            photo.save()
            return redirect("images:photo_view", photo_id=photo.id)
    else:
        form = NewPhoto()

    return render(
        request,
        "images_api/photo.html",
        {
            "form": form,
        }
    )


@login_required
def profile_view(request, profile_id=None):
    if profile_id is None:
        user = request.user
        return render(
            request,
            "images_api/index.html",
            {
                "title": "{} {} ({})".format(user.first_name, user.last_name, user.username),
                "content": "{} has uploaded {} photos.".format(user.username, len(Photo.objects.filter(owner=user))),
                "images": Photo.objects.filter(owner=user),
            }
        )
    else:
        user = get_object_or_404(User, pk=profile_id)
        return render(
            request,
            "images_api/index.html",
            {
                "title": "{} {} ({})".format(user.first_name, user.last_name, user.username),
                "content": "{} has uploaded {} photos.".format(user.username, len(Photo.objects.filter(owner=user))),
                "images": Photo.objects.filter(owner=user).filter(published=PUBLIC),
            }
        )


@login_required
def profile_edit(request):
    user = request.user
    if request.method == 'POST':
        form = EditProfile(request.POST)
        if form.is_valid():
            message = "You've updated your profile!"
            user.first_name = form.cleaned_data.get('first_name')
            user.last_name = form.cleaned_data.get('last_name')
            user.email = form.cleaned_data.get('email')
            user.save()
        else:
            message = "Whoops!"
    else:
        message = ""
        form = EditProfile(initial={
            'first_name': user.first_name,
            'last_name': user.last_name,
            'email': user.email
        })

    return render(
        request,
        "images_api/edit_profile.html",
        {
            "title": "{} {} ({})".format(user.first_name, user.last_name, user.username),
            "message": message,
            "images": Photo.objects.filter(owner=user),
            "form": form,
        }
    )
