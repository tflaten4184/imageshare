from django.db import models

class Post(models.Model):
    text = models.CharField(max_length=600)
    image = models.ImageField()

    def __str__(self) -> str:
        return self.text