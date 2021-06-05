from django.db import models

from django.core.validators import (
    get_available_image_extensions,
    FileExtensionValidator,
)


def validate_image_and_svg_file_extension(value):
    allowed_extensions = get_available_image_extensions() + ["svg"]
    return FileExtensionValidator(allowed_extensions=allowed_extensions)(value)


class SVGAndImageField(models.ImageField):
    default_validators = [validate_image_and_svg_file_extension]