from django.db import models
from django.contrib import admin
from django.forms import forms

# Create your models here.



class Motor (models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    time = models.DateTimeField()
    
class MotorAdmin(admin.ModelAdmin):
    list_display = ('title','body','time')


admin.site.register(Motor, MotorAdmin)
