from django.db import models
from taggit.managers import TaggableManager

QUESTION_LEVEL_CHOICES = (
    (1, 'Junior'),
    (2, 'Senior'),
    (3, 'Advanced'),
)

# Create your models here.
class Question(models.Model):
    question_body = models.TextField(max_length=1000, blank=False)
    answer_body = models.TextField(max_length=1000, blank=False)
    level = models.IntegerField(null=False, blank=False, choices=QUESTION_LEVEL_CHOICES)
    created_at = models.DateTimeField(null=False, blank=False, auto_now=True)
    tags = TaggableManager()

    def __str__(self):
        return self.question_body

    
    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type


    class Meta:
        ordering = ('created_at', 'level', )

