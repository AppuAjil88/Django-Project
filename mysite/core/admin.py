from django.contrib import admin

# Register your models here.
from .models import Pdfs


@admin.register(Pdfs)
class PostAdmin(admin.ModelAdmin):
    list_display = ('university', 'branch', 'subject', 'pdf')

    search_fields = ('subject', 'pdf')

