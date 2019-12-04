from django.shortcuts import render

# This class builds the response object that views are expected to return
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'index.html')

def submit(request, topic):
    return HttpResponse('<p>Topic chosen: {}</p>'.format(topic))

def test(request):
    return HttpResponse('<p>Test Sidd!!!: </p>')
    #return render(request, 'index.html')