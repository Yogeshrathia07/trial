
from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name='HOME'),
    path('about',views.about,name='about'),
    path('timetable',views.timetable,name='timetable'),
    path('notification',views.notification,name='notification'),
    path('notes',views.notes,name='notification'),
    path('delete/<int:pk>/',views.delete,name='delete'),
    path('nhome',views.nhome,name='home'),
    path("register", views.register, name="register"),
    path("login",views.login, name="login"),
    path("logout",views.logout,name="logout")

]