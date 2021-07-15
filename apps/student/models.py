from django.db import models
from django.contrib.auth import get_user_model
from django.dispatch import receiver
from django.db.models.signals import post_save

User = get_user_model()


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    first_name = models.CharField(
        max_length=50
    )
    surname = models.CharField(
        max_length=50
    )
    image = models.ImageField(
        blank=True, null=True
    )

    def __str__(self):
        return f"{self.surname}"


def __str__(self):
    return f"{self.first_name}"


class Meta:
    verbose_name = "Студент"
    verbose_name_plural = "Студенты"
    ordering = ('-id',)


@receiver(post_save, sender=User)
def create_student(sender, instance, created, *args, **kwargs):
    if created and instance.is_student:
        Student.objects.create(user=instance)
