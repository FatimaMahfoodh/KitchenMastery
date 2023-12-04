from django.contrib import admin
from .models import Tip
# Register your models here.

class TipAdmin(admin.ModelAdmin):
   list_display = ('user', 'date', 'subject', 'description')

   def save_model(self, request, obj, form, change):
       if not obj.user:
           obj.user = request.user
       obj.save()

admin.site.register(Tip, TipAdmin)
