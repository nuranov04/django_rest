from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

User = get_user_model()


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    stage = models.IntegerField()
    first_name = models.CharField(
        max_length=50)
    second_name = models.CharField(
        max_length=50
    )
    sphere = models.CharField(
        max_length=50
    )
    email = models.EmailField()
    password = models.IntegerField()

    def __str__(self):
        return f'{self.first_name}'

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"
        ordering = ('-id',)


@receiver(post_save, sender=User)
def create_student(sender, instance, created, *args, **kwargs):
    if created and instance.is_student:
        Teacher.objects.create(user=instance)
