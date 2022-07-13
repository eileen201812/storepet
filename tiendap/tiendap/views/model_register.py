from django.contrib import admin
from tiendap.persistence import models
from django.contrib.auth.models import Permission, ContentType




def load():
    admin.site.register(models.Country)
    admin.site.register(models.Category)
    admin.site.register(models.Product) 
    admin.site.register(Permission)
    admin.site.register( ContentType)
    
   
   