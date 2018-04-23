from django.contrib import admin
from .models import Mechanic, Month, TimeTable

# Register your models here.

admin.site.register(Mechanic)
admin.site.register(Month)
admin.site.register(TimeTable)
