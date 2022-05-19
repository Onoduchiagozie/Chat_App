from . import views
from django.urls import path


urlpatterns = [
        path('', views.index,name='index'),
        path('<str:room_name>/', views.room, name='room'),
        path('login/',views.LoginView.as_view(),name='login')


]
