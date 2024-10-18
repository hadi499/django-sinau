from django.db import models
from django.contrib.auth.models import User

class Tes(models.Model):
    name = models.CharField(max_length=100)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField()
    time = models.IntegerField(help_text="time in second")
    required_score_to_pass = models.FloatField()

    def get_questions(self):
      questions = self.questionsains_set.all()     
      return questions

    def __str__(self):
        return self.name
    
    class Meta:
      verbose_name_plural = "Tes"

class QuestionSains(models.Model):
    tes = models.ForeignKey(Tes, on_delete=models.CASCADE)
    title = models.TextField()
    option_a = models.CharField(max_length=255)
    option_b = models.CharField(max_length=255)
    option_c = models.CharField(max_length=255)
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.title
    
class ResultSains(models.Model):
  tes = models.ForeignKey(Tes, on_delete=models.CASCADE)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  score = models.FloatField()
  created = models.DateTimeField(auto_now_add=True)

  class Meta:
      verbose_name_plural = "Sains Result"

  def __str__(self):
    return str(self.pk)
