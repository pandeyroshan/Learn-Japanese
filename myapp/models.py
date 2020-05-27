from django.db import models

# Create your models here.

class Kanji(models.Model):
    character = models.CharField(max_length = 100,blank=False)
    onyomi = models.CharField(max_length = 100,blank=True)
    kunyomi = models.CharField(max_length = 100,blank=True)
    meaning = models.TextField()

    def __str__(self):
        return self.character
    
    class Meta:
        verbose_name = 'Kanji'
        verbose_name_plural = 'Kanji'