from django.core.exceptions import ValidationError
import os
from .validators import validate_file_extension

def validate_image_size(image):
    imagesize = image.size
    if imagesize > 2621440:
        raise ValidationError("حجم عکس حداکثر می‌تواند 2.5 مگابایت باشد.")
    else:
        return value

def validate_file_size (file):
    file_size = file.size
    if file_size > 10485760 :
        raise validate_file_size("حداکثر حجم فایل شما 10 مگابایت می تواند باشد!")
    else:
        return value

def format_file(file) :
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx', '.dotx','.html', '.png', '.xlsx', '.xls']
    if not ext.lower() in valid_extensions
        raise ValidationError('Unsupported file extension.')