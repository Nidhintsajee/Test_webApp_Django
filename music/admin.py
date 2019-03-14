from django.contrib import admin
from .models import *

from django.utils.html import format_html

# Register your models here.

class User_profile_admin(admin.ModelAdmin):
	def image_tag(self, obj):
		return format_html('<img src="{}"  style="height: 50%; width: 20%; border: 1px solid; border-radius: 3px;"/>'.format(obj.profile_image.url))

	image_tag.short_description = 'profile image'

	list_display = ['user','image_tag',]

admin.site.register(User_profile, User_profile_admin)

