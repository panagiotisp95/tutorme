from django.contrib import admin
from tutorme.models import Category, Student, Teacher, Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('title', 'rating', 'description', 'date_created', 'reviewer', 'reviewee')


# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email','picture','date_joined')


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email','picture','date_joined')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
