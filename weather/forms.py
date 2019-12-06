from .models import City
from django.forms import ModelForm, TextInput


class CityForm(ModelForm):
    class Meta:
        model = City
        fields = ['name']
        widgets = {'name': TextInput(attrs={'class': 'btn btn-lg btn-block btn-outline-primary',
                                            'name': 'city',
                                            'id': 'city',
                                            'placeholder': 'Search'})}
