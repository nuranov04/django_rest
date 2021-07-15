from django.db import models
from pygments.formatters.html import HtmlFormatter
from pygments.lexers import get_lexer_by_name
from django.contrib.auth import get_user_model
from apps.teacher.models import Teacher

User = get_user_model()


class Course(models.Model):
    course = models.CharField(
        max_length=255,
        verbose_name='Название курса'
    )
    description = models.TextField()
    owner = models.ForeignKey(Teacher, related_name='courses', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.course}'

    class Meta:
        ordering = ('-id',)


class Exercise(models.Model):
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name='cour'
    )
    exercise = models.CharField(
        max_length=100,
        verbose_name='exercise'
    )
    url = models.URLField(
        blank=True, null=True,
    )
    create_at = models.DateTimeField(auto_now_add=True)
    start_at = models.DateTimeField()
    end_at = models.DateTimeField()

    def __str__(self) -> str:
        return f"{self.create_at} -- {self.exercise}"


class Exercise_file(models.Model):
    exercise_file = models.FileField(
        upload_to='files',
        verbose_name='закрепленные файлы',
        blank=True, null=True,
    )
    exercise = models.ForeignKey(
        Exercise,
        on_delete=models.CASCADE,
        related_name='exercise_file',
    )

    def __str__(self) -> str:
        return f"{self.exercise}--{self.exercise_file}"


def save(self, *args, **kwargs):
    """
    Use the `pygments` library to create a highlighted HTML
    representation of the code snippet.
    """
    lexer = get_lexer_by_name(self.language)
    description = 'table' if self.description else False
    options = {'course': self.title} if self.title else {}
    formatter = HtmlFormatter(style=self.style, description=description,
                              full=True, **options)
    self.description = description(self.course, lexer, formatter)
    super(Course, self).save(*args, **kwargs)
