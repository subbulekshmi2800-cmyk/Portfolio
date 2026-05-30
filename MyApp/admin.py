from django.contrib import admin
from .models import *


admin.site.register(Skill)
admin.site.register(Technology)
admin.site.register(Project)

admin.site.register(Resume)

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ['name', 'email', 'subject', 'created_at' , 'message']

    search_fields = ['name', 'email', 'subject']

    list_filter = ['created_at']




