from django.contrib import admin
from .models import Departement, Requrement
# Register your models here.

class detail_page (admin.ModelAdmin):
  readonly_fildes = ('detail_id',)

admin.site.register (Departement)
admin.site.register (Requrement, detail_page)