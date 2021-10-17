from django.contrib import admin
from .models import *
# Register your models here.
#admin.site.register(Blog)
admin.site.register(Author)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('heading','author','date')
    class Meta:
        ordering = ('heading','date','author')