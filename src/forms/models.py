from django.db import models
from user.models import *
from django.utils import timezone

class Question_type(models.Model):
    type_title = models.CharField(max_length=255, blank=False)
    type_description = models.TextField(blank=True)

    def __str__(self):
        return self.type_title

class Form(models.Model):
    user_cnpj = models.ForeignKey(User_cnpj, on_delete=models.CASCADE)
    form_title = models.CharField(max_length=255, blank=False)
    form_description = models.CharField(max_length=255, blank=True)
    date_creation = models.DateField(default=timezone.now)
    form_active = models.BooleanField(default=True)

    def __str__(self):
        return self.form_title

class Question(models.Model):
    user_form = models.ForeignKey(Form, on_delete=models.CASCADE)
    question_type = models.ForeignKey(Question_type, on_delete=models.CASCADE)
    question_title = models.CharField(max_length=255, blank=False)
    question_order = models.IntegerField(blank=False)

    def __str__(self):
        return self.question_title

class User_answer(models.Model):
    user_cpf = models.ForeignKey(User_cpf, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_field = models.TextField(blank=False)
    answer_date_creation = models.DateField(default=timezone.now)

    def __str__(self):
        return self.answer_field
