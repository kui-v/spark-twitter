from django.shortcuts import render

# This class builds the response object that views are expected to return
from django.http import HttpResponse
import json
from data_application.models import Topic, Question
from django.core import serializers
from .pyScripts.getTrendyPres import getTrendyPres

# Create your views here.

def home(request):
    #pass
    topics = Topic.objects.all()
    #questions = serializers.serialize("json", Question.objects.select_related('topic_id'))    #<>
    #print(type(topics),type(questions))
    d = {"politics":["Who is the cringiest politician?", "Who is currently the most trended American polician"]}
    #questions = serializers.serialize('json', Question.objects.select_related('topic_id'))
    questions = json.dumps(d)#.encode(encoding='UTF-8',errors='strict')
    #print(json.loads())
    #questions = json.loads(questions)
    #questions = serializers.serialize('json', questions)
    #print(type(questions))
    #print(questions)
    
    return render(request, 'index.html', {'topics':topics, 'questions':questions})
'''
def test(topic,question):
    print("Its out Function")
    print(topic,question)
'''
def submit(request):
    topic = request.POST.get('topics')
    question = request.POST.get('questions')
    #source = request.POST.get('sources')
    presName = getTrendyPres()
    #return HttpResponse('<p>Topic: {}, Question: {}, Data Source: tw</p>'.format(topic, question))
    return HttpResponse('<p>Trendiest president: {}</p>'.format(presName))

def test(request,topic,question):
    print(topic,type(question))
    #return HttpResponse('<p>Test Sidd!!!: {}</p>'.format(1))
    #return render(request, 'index.html')
