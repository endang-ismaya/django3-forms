from django import forms
from django.core import validators


def check_for_e(value):
    if value[0].lower() != 'e':
        raise forms.ValidationError('Name should start with "e"')


class FormName(forms.Form):
    name = forms.CharField(validators=[check_for_e])
    email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput,
                                 validators=[validators.MaxLengthValidator(0)])

    # def clean_botcatcher(self):
    #     botcather = self.cleaned_data['botcatcher']
    #     if len(botcather) > 0:
    #         raise forms.ValidationError('Gotcha Bot!')
    #     return botcather
