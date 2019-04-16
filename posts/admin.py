
# Django
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Models
from posts.models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Posts Admin model"""

    list_display = ('pk', 'user', 'photo')
    list_display_links = ('pk', 'user')
    list_editable = ('photo',)
    list_filter = (
                'created',
                'modified'
    )