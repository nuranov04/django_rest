from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    is_teacher = models.BooleanField(default=False, verbose_name='Учитель')
    is_student = models.BooleanField(default=False, verbose_name='Студент')

