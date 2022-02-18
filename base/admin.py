from django.contrib import admin

# Register your models here.

from .models import *


admin.site.register(Category)
admin.site.register(Photo)
admin.site.register(Video)
admin.site.register(DoodleDesign)
admin.site.register(DoodleBites)