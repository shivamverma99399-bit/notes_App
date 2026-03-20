"""
URL configuration for notes_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from notes.views import delete_note, edit_note, home, login_user, logout_user, signup_user
    
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('delete/<int:id>/', delete_note),
    path('edit/<int:id>/', edit_note),
    path('login/', login_user),
    path('signup/', signup_user),
path('logout/', logout_user),
]
