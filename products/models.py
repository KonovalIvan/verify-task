import uuid

from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Product(BaseModel):
    name = models.CharField(max_length=128, null=False, blank=False, help_text='This name user see on his receipt')
    description = models.TextField(max_length=2000)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    amount = models.IntegerField(default=0)

    def __str__(self) -> str:
        return f"{self.name}"

    def short_description(self) -> str:
        return self.description[:128] if self.description else "No description"
