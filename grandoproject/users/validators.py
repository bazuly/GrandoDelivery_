from django.core.exceptions import ValidationError
from django.core.validators import EmailValidator


def corp_email_validator(value):
    allowed_domain = ['grando.pro']
    email_validator = EmailValidator(message='Проверьте правильность ввода почты')
    
    try:
        email_validator(value)
    except:
        raise ValidationError('В доступе отказано')
    
    domain = value.split('@')[1]
    if domain not in allowed_domain:
        raise ValidationError('В доступе отказно')