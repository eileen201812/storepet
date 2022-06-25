from django.shortcuts import render
from tiendap.models import Registrodeusuario


def load_usuario(request):
    print('mantenedoruser.py-> load_usuario')
    print('method -> ', request.method) 
    if request.method == 'GET':
        try:
            codigo = request.GET['codigo']
            print('codigo -> ', codigo)
            registrodeusuario = Registrodeusuario.objects.get(pk=codigo)
            registrodeusuario.delete()
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
            #Busqueda de objecto en la base de datos
            registrodeusuario = Registrodeusuario.objects.get(pk=id)
            #Actualizando objeto en memoria volatil
            registrodeusuario.nombres = nombres
            registrodeusuario.apellido_paterno = apellido_paterno
            registrodeusuario.apellido_materno = apellido_materno            
            registrodeusuario.email = email            
            #Actualizando en la base de datos                      
            registrodeusuario.save(force_update=True)
        except Exception as e:
            print(e)
    registrodeusuarios = Registrodeusuario.objects.all
    return render(request, 'mantenedoruser.html', {'registrodeusuarios': registrodeusuarios}) 
    