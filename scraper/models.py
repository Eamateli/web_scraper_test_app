from django.db import models

class ScrapedData(models.Model):
    url = models.URLField(max_length=200)
    html = models.TextField()
    
    class Meta:
        app_label = 'scraper'

