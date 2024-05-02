from django.contrib import admin

# Register your models here.

from .models import *

admin.site.register(Person)
admin.site.register(Phone)
admin.site.register(Address)
admin.site.register(Email)
admin.site.register(SocialMedia)