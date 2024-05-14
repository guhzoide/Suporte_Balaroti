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
    usuario_lib = forms.CharField(
        label="Matricula do usuário",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    usuario_efetua_liberacao = forms.CharField(
        label="Sua matricula",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

class CompararForms(forms.Form):
    usuario_com_lib = forms.CharField(
        label="Usuário com liberação",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    usuario_sem_lib = forms.CharField(
        label="Usuário sem liberação",
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )

    usuario_efetua_liberacao = forms.CharField(
        label="Sua matricula",
        required=True,
        max_length=100,
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
        label="Matricula",
        required=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
            }
        )
    )