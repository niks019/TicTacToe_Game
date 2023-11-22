from django.db import models

# Create your models here.

class feed_back(models.Model):
    feed_text = models.TextField(max_length=100)
    feed_scale = [
        (1, 'One'),
        (2, 'Two'),
        (3, 'Three'),
        (4, 'Four'),
        (5, 'Five'),
        (6, 'Six'),
        (7, 'Seven'),
        (8, 'Eight'),
        (9, 'Nine'),
        (10, 'Ten'),
    ]
    feed_scale = models.CharField(max_length=6, choices=feed_scale, default=10)
