from django.db import models

class UserModel(models.Model):
     email = models.EmailField(max_length = 254 , blank= True , null=True)
     opened = models.BooleanField(default=False)
    #  unique_code = models.UUIDField(null=True, blank=True , unique=True)
    #  status = models.BooleanField(default=False)
     def __str__(self):
         return self.email
     