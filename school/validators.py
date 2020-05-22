from django.core.exceptions import ValidationError


def validate_image_size(image):
    imagesize = image.size
    if imagesize > 2621440:
        raise ValidationError("حجم عکس حداکثر می‌تواند 2.5 مگابایت باشد.")
    else:
        return image
