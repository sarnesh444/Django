from django import forms
from .models import Post, Comment


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        #fields we will make use of from the model
        fields = ('author','title', 'text',)
        #if we want to edit the widget of a particular field
        #textinputclass - predefined class for styling
        #editable - predefined class for styling
        #medium-editor-textarea-predefined class for styling text like the one on medium
        #postcontent - developer defined css class for styling



#the widgets dict here helps tailor the form by editing widgets and also
#enables styling by adding pre-defined as well as devloper defined classes
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }
