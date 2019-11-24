from django.db import models


class room(models.Model):
    city = models.CharField(max_length=220)
    rent = models.IntegerField(default=1)
    features = models.CharField(max_length=500)
    booked = models.IntegerField(default=0) #for permanent change, while in booking page
    flag = models.BooleanField(default= False) #for temporary change, used while pressing book button

    def __str__(self):
        # template = '{self.city} {self.rent} {self.features}'
        # return template.format(self)
        return self.city+str(self.rent)+self.features
    
