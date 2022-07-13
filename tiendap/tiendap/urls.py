"""tiendap URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unicodedata import category
from turtle import home
from django.contrib import admin
from django.urls import path
from tiendap.views.home  import index
from tiendap.views.galeria  import galeria_index
from tiendap.views.contacto import contacto_index,formulario_contacto
from tiendap.views.mantenedorcontacto import load_contacto
from tiendap.views import login
from tiendap.views import logout
from tiendap.views import user
from tiendap.views import model_register
from tiendap.views import verification_recovery
from tiendap.views import recovery
from tiendap.api   import authentication
from tiendap.views  import products
from django.conf.urls import handler403, handler404
from tiendap.views.errorpage import error_404

model_register.load()
from django.conf.urls.static import static





urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('index/', index),
    path('galeria/', galeria_index),
    path('product/',products.load),
    path('contacto/', contacto_index),
    path('contacto/formulario', formulario_contacto), 
    path('mantenedor-contacto/', load_contacto),
    path('login', login.authentication),
    path('verification-recovery/', verification_recovery.load),
    path('recovery/', recovery.load),
    path('logout', logout.logout_user),
    path('edit-user/', user.load),
    path('api/v1/token', authentication.token),
   

] 



    

    
    

