from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.title
