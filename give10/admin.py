from django.contrib import admin
from .models import Tiptype, Tip
# Register your models here.

admin.site.register(Tip)
admin.site.register(Tiptype)
