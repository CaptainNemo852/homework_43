from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=200, verbose_name='Заголовок')
    text = models.TextField(max_length=2000, verbose_name='Текст')
    author = models.ForeignKey('User', on_delete=models.CASCADE, related_name='articles', verbose_name='Автор')
    comment_by = models.ManyToManyField('User', through='Comment', through_fields=('article', 'user'),
        related_name='comment_by', verbose_name='Комментарий пользователя')
    rated_by = models.ManyToManyField('User', through='Mark', through_fields=('article', 'user'),
        related_name='rated_by', verbose_name='Оценки пользователя')

    def __str__(self):
        return "%s : %s" % (self.title, self.author.name)

class User(models.Model):
    name = models.CharField(max_length=50, verbose_name='Имя пользователя')
    favorite = models.ManyToManyField(Article, blank=True, related_name='favored_by', verbose_name='Избранное')
    commented_articles = models.ManyToManyField(Article, through='Comment', through_fields=('user', 'article'),
         related_name='comments_articles', verbose_name='Комментированные')
    rated_articles = models.ManyToManyField(Article, through='Mark', through_fields=('user', 'article'),
         related_name='rated_articles',
         verbose_name='Оцененные')

    def __str__(self):
        return self.name

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='comment')
    article = models.ForeignKey(Article, on_delete=models.PROTECT, null=True, blank=True, related_name='comment')
    text = models.TextField(max_length=1000, verbose_name='комментарий')
    comment_2 = models.ForeignKey('Comment', on_delete=models.PROTECT, null=True, blank=True, related_name='comment')

    def __str__(self):
        return "%s - %s" % (self.text, self.user.name)

class Mark(models.Model):
    MARK_TERRIBLY = 'Ужасно'
    MARK_POORLY = 'Плохо'
    MARK_NORM = 'Нормально'
    MARK_GOOD = 'Хорошо'
    MARK_FINE = 'Отлично'

    MARK_CHOICES = (
        (MARK_TERRIBLY, 'Ужасно'),
        (MARK_POORLY, 'Плохо'),
        (MARK_NORM, 'Нормально'),
        (MARK_GOOD, 'Хорошо'),
        (MARK_FINE, 'Отлично')
    )

    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='mark')
    article = models.ForeignKey(Article, on_delete=models.PROTECT, related_name='mark')
    mark = models.CharField(max_length=25, choices=MARK_CHOICES, default=MARK_NORM, verbose_name="оценка")

    def __str__(self):
        return "%s: %s - %s" % (self.article.title, self.mark, self.user.name)