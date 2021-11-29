from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import IntegerField
from users.models import User
# Create your models here.


class Asset(models.Model):
    asset_name = models.TextField(max_length=30)
    asset_model = models.IntegerField(
        unique=True, db_index=True, null=True, blank=True)
    asset_allocated = models.BooleanField()

    def __str__(self) -> str:
        return f"{self.asset_name} {self.asset_model}"


class ApplicationRequest(models.Model):
    applicant = models.ForeignKey(User, on_delete=CASCADE)
    asset = models.ForeignKey(Asset, on_delete=CASCADE)
    application_date = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)


# model called asset
# asset_name
# asset_id
#allocated = boolean


# model - application request
##applicant = foreignkeyfields()
#asset = foreignkey
# date Auto now
#approved = Boolean
