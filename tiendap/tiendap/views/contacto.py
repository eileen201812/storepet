from django.shortcuts import render
from tiendap.models import Contacto

def contacto_index(request):
    print('contacto_index')
    return render(request, 'contacto.html')

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
        run = request.POST.get('run')
        dv = request.POST.get('dv')
        nombres = request.POST.get('nombres')
        apellido_paterno = request.POST.get('apellido-paterno')
        apellido_materno = request.POST.get('apellido-materno')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        asunto = request.POST.get('asunto')
        #Crear un objecto Contacto
        #que posee relación con la tabla contacto
        contacto = Contacto()
        contacto.run = run
        contacto.dv = dv
        contacto.nombres = nombres
        contacto.apellido_paterno = apellido_paterno
        contacto.apellido_materno = apellido_materno
        contacto.email = email
        contacto.telefono = telefono
        contacto.asunto = asunto
        contacto.save()
    return render(request, 'contacto.html')