from django.conf import settings
from django.db import models

# Create your models here.

PRIVATE = 'CLOSED'
UNLISTED = 'UNLISTED'
PUBLIC = 'OPEN'
PRIVACY_CHOICES = (
    (PRIVATE, 'Private'),
    (UNLISTED, 'Shared'),
    (PUBLIC, 'Public')
)


def image_path(instance, file_name):
    return 'media/{0}/{1}'.format(instance.owner.id, file_name)


class Photo(models.Model):
    """A single photo that can be uploaded by a user."""

    def __str__(self):
        return self.title

    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1024)
    published = models.CharField(choices=PRIVACY_CHOICES, max_length=255, default=PUBLIC)

    date_uploaded = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to=image_path)


class Album(models.Model):
    """A collection of photos that be uploaded by a user."""
    def __str__(self):
        return self.title

    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=255)
    description = models.TextField()
    published = models.CharField(choices=PRIVACY_CHOICES, max_length=255)
    date_uploaded = models.DateTimeField(auto_now_add=True)

    photos = models.ManyToManyField('Photo', related_name='starred_in')
    photo = models.ForeignKey(Photo, blank=True, null=True)
