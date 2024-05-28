import uuid

from django.core.validators import MinValueValidator
from django.db import models


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ProductCategory(models.TextChoices):
    """
    Also can add the ability to select from related models categories, then this can be extended without going into
    the code. Also can instead of creating a model create an enum class with a selection, it is not difficult, and it is
    convenient. This way is simplest and corresponds to the requirements that I can not specify
    """

    # TODO: Add gettext translating: usage eg. _("food")
    NO_CAT = (
        "-",
        "No category",
    )
    FOOD = (
        "F",
        "Food",
    )
    CONSUMABLES = (
        "C",
        "Consumables",
    )
    MANUFACTURED = (
        "M",
        "Manufactured",
    )
    SERVICES = (
        "S",
        "Services",
    )


class Product(BaseModel):
    name = models.CharField(max_length=128, null=False, blank=False, help_text="This name user see on his receipt")
    description = models.TextField(max_length=2000, blank=True, default="")
    price = models.DecimalField(max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    amount = models.IntegerField(default=0)
    category = models.CharField(
        max_length=128,
        default=ProductCategory.NO_CAT,
        choices=ProductCategory.choices,
        blank=False,
        null=False,
    )
    # TODO: after adding authorization add field ForeignKey created_by and edited_by, last one changes automatically
    # TODO: when someone change model

    def __str__(self) -> str:
        return f"{self.name}"

    def short_description(self) -> str:
        return self.description[:128] if self.description else "No description"
