from django.core.exceptions import ValidationError
from Users.models import *
import os

def validate_reset_code(restCode,user_id):
    user = MyUser.objects.get(id = user_id)
    user_resetCode = user.reset_code
    entered_resetCode_size = len(restCode)
    if entered_resetCode_size != 7:
        raise ValidationError("تعداد کاراکتر نامعتبر است.")
    elif user_resetCode != restCode:
        raise ValidationError("کد دو مرحله ای نامعتبر.")
    else:
        return True

def validate_password_size(password):
    password_len = len(password)
    if password_len < 8:
        raise  ValidationError("پسورد حداقل 8 کارکتر است.")
    else:
        return password

def validate_image_size(image):
    imagesize = image.size
    if imagesize > 2621440:
        raise ValidationError("حجم عکس حداکثر می‌تواند 2.5 مگابایت باشد.")
    else:
        return image

def validate_file_size (file):
    file_size = file.size
    if file_size > 10485760 :
        raise validate_file_size("حداکثر حجم فایل شما 10 مگابایت می تواند باشد!")
    else:
        return file

def validate_format_file(file) :
    ext = os.path.splitext(file.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.doc', '.docx', '.dotx','.html', '.png', '.xlsx', '.xls']
    if not ext.lower() in valid_extensions :
        raise ValidationError('فایل با این پسوند پشتیبانی نمیشود.')
