from django import forms
from django.db.models import fields
from django.db.models.query import QuerySet
from django.forms import widgets
from django.forms.formsets import all_valid
from django.forms.models import ALL_FIELDS
from .models import Asset, ApplicationRequest

#from django.contrib.auth.models import User


class ApplicationRequestForm(forms.ModelForm):
    asset = forms.ModelChoiceField(
        queryset=Asset.objects.filter(asset_allocated=False),
        widget=forms.Select(
            attrs={
                "class": "form-control",
                "placeholder": "select-asset",
                "id": "select-asset"
            }
        )
    )

    class Meta:
        model = ApplicationRequest
        fields = ['asset']
