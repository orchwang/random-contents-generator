import os
import uuid
from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError


def file_path(instance):
    return 'uploaded/{}/{}'.format(instance.id, instance.filename)


class Content(models.Model):
    """Contents Data

    COLUMNS:
        writer_name: Writer's name of contents
        title: Title of contents
        content: Content of contents
        modified_date: Modifed datetime data of contents
        created_date: Created datetime data of contents
    """
    writer_name = models.CharField(max_length=100, null=True, blank=True)
    title = models.CharField(max_length=500, null=True)
    content = models.TextField(null=False, blank=True)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)


def unique_attach_file_name(instance, filename):
    unique_file_name = uuid.uuid4()
    name, extension = os.path.splitext(filename)

    if extension.lower().replace('.', '') not in settings.ATTACH_EXTENSIONS:
        raise ValidationError(u'This file is not supported!')

    return "attach/{}{}".format(unique_file_name, extension)


class Attach(models.Model):
    """Attaches of Contents

    COLUMNS:
        content_id: Id value of content
        file_name: File name
        file_ext: extension of file
        file: Django Filefiled. Contains file path
        modified_date: Modifed datetime data of contents
        created_date: Created datetime data of contents
    """

    content = models.ForeignKey(
        Content,
        on_delete=models.CASCADE,
    )
    file_original_name = models.CharField(max_length=500, null=True)
    file_path = models.TextField(null=False, blank=True)
    created_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)
