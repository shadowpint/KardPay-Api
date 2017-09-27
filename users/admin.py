from django.contrib import admin

# Register your models here.


# Register your models here.
from .models import *
# class NewsAdmin(admin.ModelAdmin):
#     list_display = ('TITLE','PUBLISHER')
#     list_filter = [ 'CATEGORY']
#     search_fields = ['HOSTNAME']


admin.site.register(Profile)

