from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator


class Task(models.Model):
    user = models.ForeignKey( User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    priority = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(10)])

    def __str__(self):
        return self.title
    
    
    class Meta:
        ordering = ['complete','-priority', 'created']
