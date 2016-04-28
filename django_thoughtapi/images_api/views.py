from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Photo, Album, PUBLIC

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
    pass

@login_required
def photo_view(request, photo_id=None):
    pass

@login_required
def album_add(request):
    pass

@login_required
def photo_add(request):
    pass
