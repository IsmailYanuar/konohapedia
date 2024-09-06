from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.FloatField()
    date = models.IntegerField()

    @property
    def is_mood_strong(self):
        return self.rating > 4.0