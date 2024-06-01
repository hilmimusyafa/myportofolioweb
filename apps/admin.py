
from django.contrib import admin

from .models import myprojects
from .models import Contact

admin.site.register(myprojects)
admin.site.register(Contact)