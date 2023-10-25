from django.db import models
from django.core.validators import MinLengthValidator

class Lang(models.Model):
    def __str__(self) -> str:
        return self.name
    
    name = models.CharField(max_length=200, help_text='Lang Name', validators=[MinLengthValidator(1, 'the name longer than 1 char')])

class Rattata(models.Model):
    def __str__(self) -> str:
        return self.name
    
    name = models.CharField(max_length=200, help_text='Lang Name', validators=[MinLengthValidator(4, 'the name longer than 4 char')])
    weight = models.FloatField()
    lang = models.ManyToManyField('Lang', through='Rule')

class Rule(models.Model):
    lang = models.ForeignKey('Lang', on_delete=models.CASCADE)
    rattata = models.ForeignKey('Rattata', on_delete=models.CASCADE)