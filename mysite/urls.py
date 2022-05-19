from django.contrib import admin
from django.urls import include, path
from chat import views
urlpatterns = [
    path('admin/', admin.site.urls),
        path('chat/', include('chat.urls')),
        path('', views.SignUpView.as_view(), name='register'),
            path('login/',views.CustomLoginView.as_view(),name='login'),






]
