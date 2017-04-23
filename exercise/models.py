from django.db import models


class BodyPart(models.Model):
    identifier = models.CharField(max_length=200)
    video_url = models.CharField(max_length=200)


class TypeExercise(models.Model):
    identifier = models.CharField(max_length=200)
    body_part = models.ForeignKey(BodyPart, on_delete=models.CASCADE)
