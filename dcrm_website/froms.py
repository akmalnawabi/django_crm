from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "First name",
                "class": "w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500",
            }
        ),
    )

    last_name = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Last name",
                "class": "w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500",
            }
        ),
    )

    email = forms.EmailField(
        label="",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Email",
                "class": "w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500",
            }
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        base_class = "w-full px-3 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"

        for field in ["username", "password1", "password2"]:
            self.fields[field].widget.attrs.update({"class": base_class})
            self.fields[field].label = ""


class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Record
        exclude = ("user",)
        widgets = {
            "first_name": forms.TextInput(
                attrs={"class": "w-full px-3 py-2 border rounded-lg"}
            ),
            "last_name": forms.TextInput(
                attrs={"class": "w-full px-3 py-2 border rounded-lg"}
            ),
            "email": forms.EmailInput(
                attrs={"class": "w-full px-3 py-2 border rounded-lg"}
            ),
            "address": forms.TextInput(
                attrs={"class": "w-full px-3 py-2 border rounded-lg"}
            ),
        }
