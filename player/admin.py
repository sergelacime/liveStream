from django.contrib import admin
from .models import Video, Folder

admin.site.register(Folder)

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'file')
