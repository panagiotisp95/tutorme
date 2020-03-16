from django.contrib import admin
from tutorme.models import Category, Student, Teacher, Review, User


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('rating', 'date_created', 'reviewee')


class StudentAdmin(admin.ModelAdmin):
    pass


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'picture', )


class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'password', 'date_joined')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Teacher, TeacherAdmin)
admin.site.register(User, UserAdmin)
