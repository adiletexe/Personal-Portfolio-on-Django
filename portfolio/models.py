from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=240)
    image = models.ImageField()
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"