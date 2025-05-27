from django import forms
from .models import Forum, Topic, Post

class ForumForm(forms.ModelForm):
    class Meta:
        model = Forum
        fields = ['name', 'description']

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = ['title']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['content']