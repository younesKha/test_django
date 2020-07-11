from django.shortcuts import render
from django.http import HttpResponse
def hi(request):
    #return HttpResponse("<h1>Good 0110 Morning</h1>")
    return render(request,'app1/hi.html')
