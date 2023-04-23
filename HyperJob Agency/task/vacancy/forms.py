from django import forms


class AddForm(forms.Form):
    description = forms.CharField(max_length=1024, label="info",
        widget=forms.TextInput(attrs={"placeholder": "Enter info"}))
