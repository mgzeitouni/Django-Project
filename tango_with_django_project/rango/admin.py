from django.contrib import admin
from rango.models import Category, Page, UserProfile

#admin.site.register(Category)
#admin.site.register(Page)  #This is the default style

class PageAdmin(admin.ModelAdmin):
    list_display = ('category','title','views','url')
    list_filter = ['category','views']

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(UserProfile)
