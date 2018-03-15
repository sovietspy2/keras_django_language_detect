from django.db import models
from django.utils import timezone

class Prediction(models.Model):

    @classmethod
    def create(cls, t, m, g):
        pr = cls(text=t, model_predicted=m, google_prediction=g)
        pr.date = timezone.now()
        # do something with the book
        return pr

    text = models.CharField(max_length=200)
    model_predicted = models.CharField(max_length=20)
    google_prediction = models.CharField(max_length=20)
    date = models.DateTimeField('date')

