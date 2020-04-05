from django.contrib import admin

# Register your models here.

from .models import split_pdf, merge_pdfs


admin.site.register(split_pdf)
admin.site.register(merge_pdfs)
