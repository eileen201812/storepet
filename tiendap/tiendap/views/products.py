from itertools import product
from django.shortcuts import render
from pathlib import Path
import glob, os
from tiendap.persistence.models import Product
from tiendap.persistence.models import Product_Stock



def load(request): 
    return render(request, 'product.html', {'products' : load_product()})

def load_product():
    return Product_Stock.objects.all()




