from django.urls import path
from tutorme import views

app_name = 'tutorme'

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('register_student/', views.register_student, name='register_student'),
    path('register_teacher/', views.register_teacher, name='register_teacher'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('search/', views.search, name='search'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('accept/', views.accept, name='accept'),
    path('rate/', views.rate, name='rate'),
]
