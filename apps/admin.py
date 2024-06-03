
from django.contrib import admin

from .models import myprojects
from .models import Contact
from .models import skills
from .models import certification

admin.site.register(myprojects)
admin.site.register(Contact)
admin.site.register(skills)
admin.site.register(certification)