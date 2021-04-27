from .models import Messages, NewTable
from django.forms import ModelForm, TextInput, Textarea


class MessagesForm(ModelForm):
    class Meta:
        model = Messages
        fields = ["name", "message"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введиту своё имя'
        }),
            "message": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите сообщение'
            }),
        }


class NewTableForm(ModelForm):
    class Meta:
        model = NewTable
        fields = ["upperfield", "lowerfield"]
        widgets = {
            "upperfield": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'введите верхнее поле'
            }),
            "lowerfield": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'введите нижнее поле'
            }),
        }
