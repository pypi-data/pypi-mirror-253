# Django Cloud Thumbnails


Django Cloud Thumbnails is a Django app that provides a custom image cropping backend for
[django-image-cropping](https://github.com/jonasundderwolf/django-image-cropping).

It uses custom Django storage backend - 
[django-cloud-storage](https://github.com/sysproxy/django-cloud-storage).

## Installation

* Install this package using pip
```bash
pip install django-cloud-thumbnails

```
*  Add **django_cloud_thumbnails** to your **INSTALLED_APPS** setting like this
```python
INSTALLED_APPS = [
    ...,
    "django_cloud_thumbnails",
]
```
* Set image cropping backend
```python
IMAGE_CROPPING_BACKEND = 'django_cloud_thumbnails.backend.CloudThumbnailsBackend'
IMAGE_CROPPING_BACKEND_PARAMS = {}
```

* Migrate your database
```bash
python manage.py migrate
```