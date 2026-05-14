from django.db import models

class Url(models.Model):
    long_url = models.TextField()
    short_code = models.CharField(max_length=10, unique=True)
    created_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'urls'

    def __str__(self):
        return f"{self.short_code} -> {self.long_url}"
    
class Counter(models.Model):
    value = models.IntegerField(default=0)

    class Meta:
        db_table = 'counter'