from django.http import HttpResponse
from django.views.generic.base import View
# agregar un template a una vista
from django.shortcuts import render

class HelloWordld(View):
    def get(self, request):
        # agrega contexto a la vista, uso de datos dinamicos
        data = {
            'name': 'Wilfredo Barquero Herrera',
            'age': 31,
            'job': 'Developer',
            'languages': ['Python', 'JavaScript', 'Java', 'PHP', 'DJango',],
        }
        #return HttpResponse(content="Hello, World!")
        return render(request, 'hello_world.html', context=data)