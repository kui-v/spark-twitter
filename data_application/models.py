from django.db import models

# Create your models here.
class Topic(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
class Question(models.Model):
    id = models.AutoField(primary_key=True)
    question = models.CharField(max_length=120)
    topic_id = models.ForeignKey(Topic, on_delete=models.CASCADE, default=0)
    mongo_query = models.CharField(max_length=250, null=True, blank=False)
    