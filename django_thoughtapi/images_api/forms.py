from django import forms
from .models import Photo, Album


class NewPhoto(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'published', 'photo']


class NewAlbum(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'description', 'published', 'photos', 'cover_photo']

    def __init__(self, profile_=None, *args, **kwargs):
        super(NewAlbum, self).__init__(*args, **kwargs)
        self.fields['photos'].queryset = self.fields['photos'].queryset.filter(owner=profile_)
