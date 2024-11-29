from django import forms
from .models import Messages


class MessagesForm(forms.ModelForm):
    class Meta:
        model = Messages
        fields = ['name', 'email', 'phone_number', 'body']

    def __init__(self, *args, **kwargs):
        super(MessagesForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-comtrol'

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        phone_number = cleaned_data.get('phone_number')

        if not email and not phone_number:
            raise forms.ValidationError("Email yoki telefon raqami kiritilishi shart!")
        return cleaned_data
