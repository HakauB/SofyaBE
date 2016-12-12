from django.db import models

# Create your models here.

class FileHouse(models.Model):
    submitted = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, default='')
    data = models.FileField(max_length=255, upload_to='uploads/')
    filetype = models.CharField(max_length=255, default='')
    owner = models.ForeignKey('auth.User', related_name='filehouses', on_delete=models.CASCADE, default=0)

    class Meta:
        ordering = ('submitted',)
