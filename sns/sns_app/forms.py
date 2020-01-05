from django import forms
from .models import Thread, ResPost


class CreateThread(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ("thread_name", )


class CreateResPost(forms.ModelForm):
    class Meta:
        model = ResPost
        fields = ("post_user", "post_text",)


class CreateRespost2(forms.Form):
    thread = forms.IntegerField()
    post_user = forms.CharField(max_length=20)
    post_text = forms.Textarea()
