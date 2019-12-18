from django.contrib import admin
from .models import Topic, Question

# Register your models here.

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ['name']
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ['question', 'topic_id', 'mongo_query']