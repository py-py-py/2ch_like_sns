from django import forms
from .models import Thread, ResPost


class CreateThread(forms.ModelForm):
    class Meta:
        model = Thread
        fields = ("thread_name", )


class CreateResPostForm(forms.ModelForm):
    class Meta:
        model = ResPost
        fields = ("post_user", "post_text", "thread")

