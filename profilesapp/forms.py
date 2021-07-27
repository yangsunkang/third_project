from django.forms import ModelForm

from profilesapp.models import Profile


class ProfileCreationForm(ModelForm):
    class meta:
        model = Profile
        fields = ['image','nickname', 'messages']