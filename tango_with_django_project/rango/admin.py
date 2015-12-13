from django.contrib import admin
from rango.models import Category, Page

admin.site.register(Category)
#admin.site.register(Page)  #This is the default style

class PageAdmin(admin.ModelAdmin):
    list_display = ('category','title','url')
    list_filter = ['category']

admin.site.register(Page, PageAdmin)

#trsting