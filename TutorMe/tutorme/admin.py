from django.contrib import admin
from tutorme.models import Category, Student, Teacher, Review, User


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating', 'description', 'date_created', 'reviewee')


# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class StudentAdmin(admin.ModelAdmin):
    pass


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'picture', 'categories_list', 'categories',)


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'date_joined')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(User, UserAdmin)
