from django.db import models
from taggit.managers import TaggableManager

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=100)
    manager_name = models.CharField(max_length=50, blank=False)
    manager_alias = models.CharField(max_length=50, blank=False)
    manager_email = models.EmailField(blank=False)
    # parent organization, recursive, allow null
    parent_org = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, db_index=True)
    skills = TaggableManager()

    def __str__(self):
        return self.name

    
    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type


    
