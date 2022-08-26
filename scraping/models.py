from django.db import models

class City(models.Model):
    name = models.CharField(max_length=50, verbose_name= 'city name')
    slug = models.CharField(max_length=50, blank=True)

    class Meta:
        verbose_name = 'city name'
        verbose_name_plural = 'city names'
    
    def __str__(self):
        return self.name