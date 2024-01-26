from image_cropping.backends.base import ImageBackend

from django_cloud_thumbnails.utils import find_or_create_source, check_old_crops, find_or_create_thumbnail, pil_image, \
    thumbnail_url


class CloudThumbnailsBackend(ImageBackend):
    exceptions_to_catch = (IOError,)

    def get_thumbnail_url(self, image, thumbnail_options):
        source = find_or_create_source(str(image))

        box = thumbnail_options.get('box')
        check_old_crops(source, box)

        width = thumbnail_options['size'][0]
        height = thumbnail_options['size'][1]
        thumbnail = find_or_create_thumbnail(source, width, height)

        return thumbnail_url(thumbnail)

    def get_size(self, image):
        return pil_image(image).size
