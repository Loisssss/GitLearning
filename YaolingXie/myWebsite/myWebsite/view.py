from django.http import HttpResponse

from django.shortcuts import render

def hello(request):
    context          = {}
    context['Lois'] = 'Loisssss!'
    return render(request, 'hello.html', context)