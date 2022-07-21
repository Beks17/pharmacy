from dataclasses import fields
from django.forms import ModelForm
from .models import *


class ActiveIngredientForm(ModelForm):
    class Meta:
        model = ActiveIngredient
        fields = "__all__"