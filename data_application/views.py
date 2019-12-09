from django.shortcuts import render

# This class builds the response object that views are expected to return
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'index.html')

def submit(request):
    topic = request.POST.get('topics')
    question = request.POST.get('questions')
    #source = request.POST.get('sources')

    return HttpResponse('<p>Topic: {}, Question: {}, Data Source: tw</p>'.format(topic, question))

def test(request):
    return HttpResponse('<p>Test Sidd!!!: {}</p>'.format(1))
    #return render(request, 'index.html')