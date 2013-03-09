import datetime

from django.db import models


class Result(models.Model):
    input_text = models.TextField()
    output_text = models.TextField()
    success = models.BooleanField()
    date = models.DateTimeField()

    @classmethod
    def create(cls, input_text, output_text, success):
        return cls(input_text=input_text, output_text=output_text,
                   success=success, date=datetime.datetime.now())

    def short_input(self):
        return unicode(self.input_text[:30])

    def __unicode__(self):
        return unicode(self.date)


class Feedback(models.Model):
    rating = models.IntegerField()
    text = models.TextField()
    result = models.ForeignKey(Result)

    def __unicode__(self):
        return unicode(self.text)
