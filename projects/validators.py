from django.core.exceptions import ValidationError

def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            '%(value)s is not an even number',
            params={'value': value},
         )       

def validate_name(value):
    name = value
    if name == "":
        raise ValidationError("masukkan nama yang valid")
        
CATEGORIES = {'Multimedia', 'Programming', 'Computing & Networking'}

def validate_category(value):
    cat = value.capitalize()
    if not value in CATEGORIES and not cat in CATEGORIES:
        raise ValidationError(f"{value} bukan kategori yang valid")