from turtle import title
from django.db import models
from members.models import Profile

class Choice(models.Model):
    text = models.CharField(max_length=200, blank=False, null=False)
    statment = models.BooleanField(default=False)
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='choices')
    def __str__(self) -> str:
        return self.text+ ' on ' + self.question.text

class Question(models.Model):

    text = models.TextField(max_length=2000,blank=False, null=False)
    author = models.ForeignKey(Profile, on_delete = models.CASCADE)
    contest = models.ForeignKey('Contest', on_delete=models.CASCADE , related_name='questions')
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.text + ' on ' + self.contest.title

class Contest(models.Model):
    title = models.CharField(max_length=200, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    duration = models.DurationField(null=True)
    start = models.DateTimeField()
    available = models.BooleanField(default=False)
    password = models.CharField(max_length=200 ,null=True, blank=True)
    def __str__(self) -> str:
        return self.title

class Result(models.Model):
    participant = models.ForeignKey(Profile, blank=True, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)
    contest = models.ForeignKey(Contest, on_delete=models.CASCADE, blank=True ,null = True, related_name='result')
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.contest.title + ' ' + self.participant.user.username
