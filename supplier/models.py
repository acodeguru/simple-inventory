import uuid
from django.db import models

# Create your models here.
class Supplier(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)

    objects = models.Manager()
    
    def __str__(self):
        return str(self.name)+ " (" + str(self.id)+")"