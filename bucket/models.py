from django.db import models

class Zone(models.Model):
    _ID = models.IntegerField(help_text='Enter the zone number')
    description = models.TextField(max_length=100, help_text='Enter a brief description about the zone')
    flow = models.FloatField(help_text='Approximate zone flow in GPM')
    area = models.FloatField(help_text='Approximate zone area in sf')

    def __str__(self):
        return self.title
