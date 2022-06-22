from django.shortcuts import render
from tiendap.models import Registrodeusuario

def usuario_index(request):
    print('contacto_index')
    return render(request, 'usuario.html')

def formulario_contacto(request):
    print('formulario_contacto')

    if request.method == 'GET':
        print('invocación por método GET')
        run = request.GET.get('run')
        print('run {0}'.format(run))

    elif request.method == 'POST':
        print('invocación por método POST')
        #obtener información formulario
        #almacenandola en variables
        nombres = request.POST.get('nombres')
        apellido_paterno = request.POST.get('apellido-paterno')
        apellido_materno = request.POST.get('apellido-materno')
        email = request.POST.get('email')
        
        #Crear un objecto Contacto
        #que posee relación con la tabla contacto
        registrodeusuario = Registrodeusuario()
        registrodeusuario.nombres = nombres
        registrodeusuario.apellido_paterno = apellido_paterno
        registrodeusuario.apellido_materno = apellido_materno
        registrodeusuario.email = email
        registrodeusuario.save()
    return render(request, 'usuario.html')