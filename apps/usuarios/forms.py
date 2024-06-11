from django import forms

class LoginForms(forms.Form):
    nome_login = forms.CharField(
        label="Usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    senha = forms.CharField(
        label="Senha",
        required=True,
        max_length=70,
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control",
            }
        )
    )

class LiberarForms(forms.Form):
    usuario_lib = forms.IntegerField(
        label="Matrícula do usuário",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    usuario_efetua_liberacao = forms.IntegerField(
        label="Sua matrícula",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

class CompararForms(forms.Form):
    usuario_com_lib = forms.IntegerField(
        label="Matrícula com liberação",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    usuario_sem_lib = forms.IntegerField(
        label="Matrícula sem liberação",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    usuario_efetua_liberacao = forms.IntegerField(
        label="Sua matrícula",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

class ContaOmniForms(forms.Form):
    CHOICES = (('Vendedor', 'Vendedor'),('Gestao', 'Gestao'),)
    acesso = forms.ChoiceField(choices=CHOICES)

    loja = forms.CharField(
        label="Loja",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    nome = forms.CharField(
        label="Nome",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    email = forms.CharField(
        label="E-mail",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    matricula = forms.IntegerField(
        label="matrícula",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )