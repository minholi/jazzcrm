from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.admin import GroupAdmin as BaseGroupAdmin
from django.contrib.auth.models import User, Group
from eav.admin import AttributeAdmin as BaseAttributeAdmin
from eav.models import Attribute, EnumGroup, EnumValue, Value

from unfold.admin import ModelAdmin


admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.unregister(Attribute)
admin.site.unregister(EnumGroup)
admin.site.unregister(EnumValue)
admin.site.unregister(Value)

@admin.register(User)
class UserAdmin(BaseUserAdmin, ModelAdmin):
    pass

@admin.register(Group)
class GroupAdmin(BaseGroupAdmin, ModelAdmin):
    pass

@admin.register(Attribute)
class AttributeAdmin(BaseAttributeAdmin, ModelAdmin):
    pass

@admin.register(EnumGroup)
class EnumGroupAdmin(ModelAdmin):
    pass

@admin.register(EnumValue)
class EnumValueAdmin(ModelAdmin):
    pass

@admin.register(Value)
class ValueAdmin(ModelAdmin):
    pass

