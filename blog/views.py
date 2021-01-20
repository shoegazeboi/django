from django.shortcuts import render
from .models import News, Comments, CommentsForm


def main_page(request):
    return render(request, 'blog/main_page.html', {'title': 'teqnikpasha'})


def news(request):
    error = ''
    if request.method == 'POST':
        comments_forms = CommentsForm(request.POST)
        if comments_forms.is_valid():
            comments_forms.save()

        else:
            error = 'Неправильно введен коментарий'

    name = 1
    if News.objects.values('title') is []:
        news = 'Пока что тут нету постов'
        print('qwerty')

    else:
        news = News.objects.all()

    comments = Comments.objects.all()
    comments_forms = CommentsForm()

    return render(request, 'blog/news.html',
                  {'title': 'Новости Паши', 'news': list(reversed(news)), 'comments': comments,
                   'form_of_comments': comments_forms, 'error': error})


def tickets(request):
    return render(request, 'blog/tickets.html', {'title': 'Билеты'})
