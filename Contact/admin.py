from django.contrib import admin
from .models import Contacts


@admin.register(Contacts)
class AdminContacts(admin.ModelAdmin):
    pass
