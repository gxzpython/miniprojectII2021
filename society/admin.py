from django.contrib import admin

# Register your models here.

# Register your models here.
from society.models import Group, Event, People

admin.site.register(Group)
admin.site.register(Event)
admin.site.register(People)