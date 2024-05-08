from django.shortcuts import render
from .models import Manufacture, Car


def cars(request):
    data = Car.objects.all()
    return render(request, 'Cars.html', {'data': data})


def manufactures(request):
    data = Manufacture.objects.all()
    return render(request, 'Manufactures.html', {'data': data})
