import uuid
from django.db import models
from supplier.models import Supplier

# Create your models here.
class Inventory(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    note = models.TextField()
    stock = models.IntegerField()
    availability = models.BooleanField(default=False, blank=True, null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE,)

    objects = models.Manager()
    
    def __str__(self):
        return str(self.name)+ " (" + str(self.id)+")"