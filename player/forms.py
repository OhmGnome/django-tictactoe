from django.forms import ModelForm

from .models import Invitation


class InvitationForm(ModelForm):
    class Meta:
        # the class that the ModelForm generates input fields from
        model = Invitation
        # fields to exclude from this form
        exclude = ('from_user', 'timestamp')
