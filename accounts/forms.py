from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label='名前', required=True)
    email = forms.EmailField(label='メールアドレス', required=True)
    message = forms.CharField(label='メッセージ', required=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['placeholder'] = '名前を入力してください'
        self.fields['email'].widget.attrs['placeholder'] = 'メールアドレスを入力してください'
        self.fields['message'].widget.attrs['placeholder'] = 'メッセージを入力してください'
