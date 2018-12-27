from django.db import models

class Location(models.Model):

    lid = models.CharField(max_length=10)
    lshortname = models.CharField(max_length=3)
    lname = models.CharField(max_length=50)

    def __str__ (self):
        return '%s %s %s' % (self.lid, self.lshortname, self.lname)
