from django import forms

class formsCupom(forms.Form):
    data = forms.DateField(
        label="Escolha uma data",
        required=True,
        widget=forms.DateInput(format="%d-%m-%y", attrs={"type": "date"}),
    )

    numero_cupom = forms.IntegerField(
        label='Número do cupom',
        required=True,
    )