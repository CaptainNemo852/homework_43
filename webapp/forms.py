from django import forms
from webapp.models import Article, Comment

class SearchProjectForm(forms.Form):
    article_name = forms.CharField(max_length=50, required=False, label="Поиск проект")


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'text', 'author']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['user', 'article', 'text']


class CommentsForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']