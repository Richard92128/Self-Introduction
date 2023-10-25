from django.forms import ModelForm
from home.models import Rattata, Lang


# Create the form class.
class RattataForm(ModelForm):
    class Meta:
        model = Rattata
        fields = '__all__'

class LangForm(ModelForm):
    class Meta:
        model = Lang
        fields = '__all__'