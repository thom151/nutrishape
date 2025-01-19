from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    height = models.IntegerField(null=True, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    goal_weight = models.IntegerField(null=True, blank=True)
    weekly_goal =models.IntegerField(null=True, blank=True)
    age=models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.username} is {self.age} years old, has a height: {self.height}cm has a weight: {self.weight}kg has a goal of {self.goal_weight}kg and a weekly goal of {self.weekly_goal}kg'

class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="goal_user")
    GOAL_CHOICES = [
        ('LW', 'Lose weight'),
        ('MW', 'Maintain Weight'),
        ('GW','Gain Weight'),
    ]

    goal = models.CharField(max_length = 3, choices=GOAL_CHOICES)

    def __str__(self):
        return f" {self.user} wants tO {self.goal} "


class ActivityLevel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="act_user")
    LEVEL_CHOICES = [
        ('S', 'Sedentary'),
        ('LA', 'Lightly Active'),
        ('MA','Moderately Active'),
        ('VA','Very Active'),
        ('EA','Extra Active')
    ]
    level = models.CharField(max_length= 3, choices=LEVEL_CHOICES)

    def __str__(self):
        return f"{self.user}'s activity level is {self.level}"





class Sex(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="sex_user")
    SEX_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female')
    ]

    sex = models.CharField(max_length=1, choices=SEX_CHOICES)

    def __str__(self):
        return f'{self.user} is a {self.sex}'





class DailyCalorie(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="daily_cal_user")
    calories=models.IntegerField()

    def __str__(self):
        return f'{self.user} needs to lose {self.calories} daily'


class Thread(models.Model):
    user= models.ForeignKey(User, on_delete=models.CASCADE, related_name="thread_user")
    subject= models.CharField(max_length =256, default="new chat")
    threads = models.CharField(max_length = 256)

    def __str__(self):
        return f'{self.subject} thread - Created by: {self.user}.'
