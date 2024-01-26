from io import BytesIO
from os.path import splitext

from PIL import Image, ImageFile
from django.core.files.base import ContentFile
from django_cloud_storage.storage import CloudStorage, CloudStorageException
from django_cloud_thumbnails.models import Source, Thumbnail

storage = CloudStorage()


def pil_image(source):
    if not source:
        return

    source = BytesIO(source.read())

    image = Image.open(source)

    try:
        ImageFile.LOAD_TRUNCATED_IMAGES = True
        image.load()
    finally:
        ImageFile.LOAD_TRUNCATED_IMAGES = False

    return image


def find_or_create_source(name: str) -> Source:
    source = Source.objects.filter(name=name).first()

    if not source:
        source = Source.objects.create(name=name)

    return source


def find_or_create_thumbnail(source: Source, width: int, height: int) -> Thumbnail:
    thumbnail = Thumbnail.objects.filter(source=source, width=width, height=height).first()

    if not thumbnail:
        name = generate_thumbnail(source, width, height)
        thumbnail = Thumbnail.objects.create(source=source, name=name, width=width, height=height)

    return thumbnail


def generate_thumbnail(source: Source, width: int, height: int) -> str:
    file = storage.open(source.name)

    image = pil_image(file)

    if source.box:
        box = [int(x) for x in source.box.split(',')]
        image = image.crop((box[0], box[1], box[2], box[3]))

    image = image.resize((width, height))

    image_bytes = BytesIO()
    image.save(image_bytes, format='JPEG', quality=85)

    base, extension = splitext(source.name)

    return storage.save(f'{base}_{width}x{height}{extension}', ContentFile(image_bytes.getvalue()))


def thumbnail_url(thumbnail: Thumbnail) -> str:
    return storage.url(thumbnail.name)


def delete_thumbnails(source: Source) -> None:
    for thumb in Thumbnail.objects.filter(source=source).all():
        try:
            storage.delete(thumb.name)
        except CloudStorageException:
            ...

        thumb.delete()


def check_old_crops(source: Source, box: str = None) -> bool:
    if not box:
        return False

    if source.box != box:
        delete_thumbnails(source)

        source.box = box
        source.save()


def delete_source(name: str) -> None:
    source = Source.objects.filter(name=name).first()

    if not source:
        return

    delete_thumbnails(source)

    try:
        storage.delete(source.name)
    except CloudStorageException:
        ...

    source.delete()
