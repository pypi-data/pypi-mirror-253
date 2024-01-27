import os
from uuid import uuid4

from django.conf import settings
from django.db import models


# Create your models here.
def _choose_upload_media_to(instance, filename, dir_prefix):
    """choose directory to upload files"""
    if len(filename) > 5:
        filepath = "{}/{}/{}".format(filename[:2], filename[:4], filename)
    else:
        filepath = filename
    name = dir_prefix + filepath
    return name


def get_a_name(old_name: str):
    """generate a new random name with the same old extension
    :param old_name: the old name, where we get the extension.
    :type old_name: str
    """
    base, ext = os.path.splitext(old_name)
    return f"{uuid4().hex}.{ext}"


def choose_upload_media_to(instance, filename):
    """where to upload the main file.
    Generates a new random name.
    """
    prefix_dir = getattr(settings, "SOCIAL_LAYER_DIRPREFIX", "sl/")
    newname = get_a_name(filename)
    return _choose_upload_media_to(instance, newname, prefix_dir)


def choose_upload_media_thumb_to(instance, filename):
    """where to upload the thumbnail file
    Uses the same Generates a new random name.
    """
    prefix_dir = getattr(settings, "SOCIAL_LAYER_DIRPREFIX", "sl/")
    if instance.media_file:
        newname = os.path.basename(instance.media_file.name)
    else:
        newname = get_a_name(filename)
    return _choose_upload_media_to(instance, newname, f"{prefix_dir}thumbs/")


class Media(models.Model):
    """abstract class for media objects"""

    media_file = models.FileField(upload_to=choose_upload_media_to, max_length=10485760)
    media_thumbnail = models.FileField(
        upload_to=choose_upload_media_thumb_to,
        max_length=10485760,
        null=True,
        blank=True,
    )
    content_type = models.CharField(
        max_length=127, null=True, blank=True, default="application/octet-stream"
    )
    orientation = models.CharField(max_length=10, default="portrait")

    format_tries = models.IntegerField(default=0)
    formated = models.BooleanField(default=False)
    md5_hash = models.CharField(max_length=32, null=True, blank=True)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        from social_layer.mediautils.utils import get_img_orientation

        super(Media, self).save(*args, **kwargs)
        # Try to guess image orientation
        if self.content_type and "image/" in self.content_type:
            self.orientation = get_img_orientation(self.media_file.path)
        elif self.media_thumbnail:
            self.orientation = get_img_orientation(self.media_thumbnail.path)
        super(Media, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        attr_list = ["media_file", "media_thumbnail"]
        for attr in attr_list:
            arquivo = getattr(self, attr, None)
            if arquivo and os.path.isfile(arquivo.path):
                os.remove(arquivo.path)
        super(Media, self).delete(*args, **kwargs)
