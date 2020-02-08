from django.db import models

class Questions(models.Model):
    question_text=models.CharField(max_length=100)
    pub_date=models.DateTimeField('DatePublished')

    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text=models.CharField(max_length=100)
    votes=models.IntegerField(default=0)
    question=models.ForeignKey(Questions,on_delete=models.CASCADE)

    def __str__(self):
        return self.choice_text
 
