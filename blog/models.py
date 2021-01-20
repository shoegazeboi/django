from django.db import models
from django.forms import ModelForm, Textarea


class News(models.Model):
    title = models.TextField('Заголовок', blank=True)
    text = models.TextField('Текст', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'


class Comments(models.Model):
    comment = models.TextField('Комментарий')

    def __str__(self):
        return self.comment

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'


class CommentsForm(ModelForm):
    class Meta:
        model = Comments
        fields = ('comment',)
        widgets = {'comment': Textarea(attrs={
            'class': 'form-control',
            'placeholder': 'введите комментарий',
            'cols': '1',
            'rows': '2',
            })
        }
