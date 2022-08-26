from django.db import models
from scraping.utils import from_cyrillic_to_eng

class City(models.Model):
    name = models.CharField(max_length=50, 
                            verbose_name= 'City name',
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'City name'
        verbose_name_plural = 'City names'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)

class Language(models.Model):
    name = models.CharField(max_length=50, 
                            verbose_name= 'Programming language',
                            unique=True)
    slug = models.CharField(max_length=50, blank=True, unique=True)

    class Meta:
        verbose_name = 'Programming language'
        verbose_name_plural = 'Programming languages'
    
    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = from_cyrillic_to_eng(str(self.name))
        super().save(*args, **kwargs)