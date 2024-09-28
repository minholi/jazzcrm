from django.contrib import admin
from unfold.admin import ModelAdmin
from contacts.models import Contact
from eav.forms import BaseDynamicEntityForm
from eav.admin import BaseEntityAdmin

class ContactAdminForm(BaseDynamicEntityForm):
    model = Contact

@admin.register(Contact)
class ContactAdmin(ModelAdmin, BaseEntityAdmin):
    form = ContactAdminForm
