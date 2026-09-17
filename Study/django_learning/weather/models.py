from django.db import models

# Creating my first model SavedCity

class SavedCity(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name