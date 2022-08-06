from django.db import models

# Create your models here.
class Blogs(models.Model):
    title = models.CharField(max_length=80)
    description = models.CharField(max_length=240)
    date = models.DateField(blank=False)
    image = models.ImageField(blank=True)
    text = models.TextField(max_length=1000)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"