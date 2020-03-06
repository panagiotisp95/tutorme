from django.contrib import admin
from tutorme.models import Category, Page
from tutorme.models import User


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email','picture','date_joined')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)
admin.site.register(User, UserAdmin)
