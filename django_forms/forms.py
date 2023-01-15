from django import forms
from web.forms.models import Contact

class EmailSender(forms.Form):

    users = forms.ModelMultipleChoiceField(queryset=Contact.objects.all(),widget = forms.CheckboxSelectMultiple)
    message = forms.CharField(max_length=400)