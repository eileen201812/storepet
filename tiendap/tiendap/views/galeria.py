from django.shortcuts import render


def galeria_index(request):
    print('galeria')
    return render(request, 'galeria.html')