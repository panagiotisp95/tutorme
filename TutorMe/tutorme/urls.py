from django.urls import path
from tutorme import views

app_name = 'tutorme'

urlpatterns = [
    path('', views.index, name='index'),
    path('homepage/', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name>/', views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('register_student/', views.register_student, name='register_student'),
    path('register_teacher/', views.register_teacher, name='register_teacher'),
    path('login/', views.user_login, name='login'),
    path('restricted/', views.restricted, name='restricted'),
    path('logout/', views.user_logout, name='logout'),
    path('search/', views.search, name='search'),
    path('teacherDashboard/', views.teacherDashboard, name='teacherDashboard'),
    #url(r'^ratings/', include('star_ratings.urls', namespace='ratings', app_name='ratings')),

]
