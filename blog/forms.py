from django import forms
from .models import Comment, Post


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25, required=True, widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'Name'}))
    email = forms.EmailField(required=True, widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'E-Mail'}))
    to = forms.EmailField(required=True, widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'To'}))
    comments = forms.CharField(required=False,
                               widget=forms.Textarea(attrs={"class": "form-control mb-1", 'placeholder': 'Comments'}))


class PostForm(forms.ModelForm):
    title = forms.CharField(max_length=255,  widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'Title'}))
    body = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'Body'}))
    status = forms.ChoiceField(choices=(('DF', 'Draft'), ('PB', 'Published')),)
    tags = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'Tags separated with commas'}))

    class Meta:
        model = Post
        fields = ["title", "body", "status", 'tags']

    def clean_tags(self):
        tags = self.cleaned_data.get('tags')
        if tags:
            return [tag.strip() for tag in tags.split(',')]
        return []


class CommentForm(forms.ModelForm):
    name = forms.CharField(required=True,
                           widget=forms.TextInput(attrs={"class": "form-control", 'placeholder': 'Name'}))
    email = forms.EmailField(required=True,
                             widget=forms.EmailInput(attrs={"class": "form-control", 'placeholder': 'Email'}))
    body = forms.CharField(required=True, widget=forms.Textarea(attrs={"class": "form-control", 'placeholder': 'Text'}))

    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']


class SearchForm(forms.Form):
    query = forms.CharField(
        widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'Enter search term...'}))


class UpdatePostForm(forms.ModelForm):
    title = forms.CharField(max_length=255,
                            widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'Title'}))
    body = forms.CharField(required=False,
                           widget=forms.TextInput(attrs={"class": "form-control mb-1", 'placeholder': 'Body'}))
    status = forms.ChoiceField(choices=(('DF', 'Draft'), ('PB', 'Published')))

    class Meta:
        model = Post
        fields = ["title", "body", "status"]