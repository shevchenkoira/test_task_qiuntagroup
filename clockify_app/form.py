from django import forms


class ParsingForm(forms.Form):
    workspace_url = forms.URLField()
