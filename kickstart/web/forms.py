from django import forms
from .tasks import send_email

class ContactUsForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.widgets.Textarea(attrs={'rows':4, 'cols':60}))
    email = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']
        email = self.cleaned_data['email']
        cc_myself = self.cleaned_data['cc_myself']

        send_email.delay('stebax@gmail.com',email,subject,message,cc_myself)

class FanOutForm(forms.Form):
    message = forms.CharField(widget=forms.widgets.Textarea(attrs={'rows':4, 'cols':60}))

