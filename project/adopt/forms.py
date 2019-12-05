from django.forms import ModelForm
from .models import Pet
class PetForm(ModelForm):
    class Pets:
        model = Pet
        fields = "__all__"
