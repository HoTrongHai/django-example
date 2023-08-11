from django.db import models

# Create your models here.

from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    publish_date = models.DateTimeField('date published')


    def __str__(self):
        return f"{self.question_text}"

class Choice(models.Model):
    """

    Make relationship from question object to choice object:
    question: 1  -> choices N
    question.choice_set
    """
    question = models.ForeignKey(Question, on_delete=models.CASCADE)


    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.choice_text}"

