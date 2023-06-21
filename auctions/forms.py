from django import forms
from .models import Action, Comment
from django.utils.translation import gettext_lazy as _

class ActionForm(forms.ModelForm):
    class Meta:
        model = Action
        fields = ('title', 'description', 'image', 'categorie', 'initial_bid')
        labels = {
            'title': 'Title',
            'description': 'Description',
            'image': 'URL Image',
            'categorie': 'Categorie',
            'initial_bid': 'Initial Bid'
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for input in ['title', 'description', 'image', 'categorie', 'initial_bid']:
            self.fields[input].widget.attrs.update({"class": "form-control form-control-lg"})

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('title', 'comment')
        labels = {
            'title': '',
            'comment': ''
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({"placeholder": "Title", "class": "form-control"})
        self.fields['comment'].widget.attrs.update({"placeholder": "Comment", "class": "form-control"})
