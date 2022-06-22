from django.shortcuts import render
from tiendap.models import Contacto

def load_contacto(request):
    print('mantenedorcontacto.py -> load_contacto')    
    print('method -> ', request.method)
    if request.method == 'GET':
        try:
            codigo = request.GET['codigo']
            print('codigo -> ', codigo)
            contacto = Contacto.objects.get(pk=codigo)
            contacto.delete()
        except Exception as e:
            print(e)
    if request.method == 'POST':
        try:
            #Lectura Formulario
            id = request.POST['codigo']
            nombres = request.POST['nombres']
            apellido_paterno = request.POST['apellido_paterno']
            apellido_materno = request.POST['apellido_materno']
            email = request.POST['email']
            telefono = request.POST['telefono']            
            asunto = request.POST['asunto']
            #Busqueda de objecto en la base de datos
            contacto = Contacto.objects.get(pk=id)
            #Actualizando objeto en memoria volatil
            contacto.nombres = nombres
            contacto.apellido_paterno = apellido_paterno
            contacto.apellido_materno = apellido_materno            
            contacto.email = email            
            contacto.telefono = telefono            
            contacto.asunto = asunto  
            #Actualizando en la base de datos                      
            contacto.save(force_update=True)
        except Exception as e:
            print(e)
    contactos = Contacto.objects.all
    return render(request, 'mantenedor-contacto.html', {'contactos': contactos})            
        

