from django import forms
from django.conf import settings
from .models import Photo, Album


class NewPhoto(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['title', 'description', 'published', 'photo']


class NewAlbum(forms.ModelForm):
    class Meta:
        model = Album
        fields = ['title', 'description', 'published', 'photos', 'photo']

    def __init__(self, profile_=None, *args, **kwargs):
        super(NewAlbum, self).__init__(*args, **kwargs)
        self.fields['photos'].queryset = self.fields['photos'].queryset.filter(owner=profile_)


class EditProfile(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
