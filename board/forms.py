from django import forms


class BoardForm(forms.Form):
    title = forms.CharField(max_length=128, label="Title",
                            error_messages={
                                'required': 'Choose a title!'
                            })

    contents = forms.CharField(widget=forms.Textarea, label="Contents",
                               error_messages={
                                   'required': 'Write something!'
                               })
    tags = forms.CharField(label="Tags", required=False)
