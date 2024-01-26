from django.db import models
from django.utils import timezone


class Source(models.Model):
    name = models.CharField(max_length=255, unique=True)
    box = models.CharField(max_length=255)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Thumbnail(models.Model):
    source = models.ForeignKey(Source, related_name='thumbnails', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, unique=True)
    width = models.PositiveIntegerField(null=True)
    height = models.PositiveIntegerField(null=True)
    modified = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.width}x{self.height}'

    @property
    def size(self):
        return self.width, self.height
