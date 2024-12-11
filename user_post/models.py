from django.db import models

class Poster(models.Model):
  title=models.CharField(max_length=200)
  comment=models.TextField()
  written_by=models.TextField()

  def __str__(self):
    return f'{self.title}- {self.comment}:  {self.wriiten_by}'


