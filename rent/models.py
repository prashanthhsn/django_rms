from django.db import models


class room(models.Model):
    city = models.CharField(max_length=220)
    rent = models.IntegerField(default=1)
    features = models.CharField(max_length=500)

    def __str__(self):
        # template = '{self.city} {self.rent} {self.features}'
        # return template.format(self)
        return self.city+str(self.rent)+self.features