from django.contrib import admin
from . import models
from .models import Group

# Register your models here.

class GroupMemberInline(admin.TabularInline):
    model = models.GroupMember


admin.site.register(Group)



