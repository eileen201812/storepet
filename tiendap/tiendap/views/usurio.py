from django.shortcuts import render
from tiendap.models import Registrodeusuario

def usuario_index(request):
    print('usuario_index')
    return render(request, 'usuario.html')

def formulario_usuario(request):
    print('formulario_usuario')

    if request.method == 'GET':
        print('invocación por método GET')
        run = request.GET.get('run')
        print('run {0}'.format(run))
        
    elif request.method == 'POST':
        print('invocación por método POST')
        #obtener información formulario
        #almacenandola en variables
        run = request.POST.get('run')
        dv = request.POST.get('dv')
        nombres = request.POST.get('nombres')
        apellido_paterno = request.POST.get('apellido-paterno')
        apellido_materno = request.POST.get('apellido-materno')
        email = request.POST.get('email')
        #Crear un objecto Contacto
        #que posee relación con la tabla contacto
        registrodeusuario = Registrodeusuario()
        registrodeusuario.run = run
        registrodeusuario.dv = dv
        registrodeusuario.nombres = nombres
        registrodeusuario.apellido_paterno = apellido_paterno
        registrodeusuario.apellido_materno = apellido_materno
        registrodeusuario.email = email
        registrodeusuario.save()
    return render(request, 'usuario.html')