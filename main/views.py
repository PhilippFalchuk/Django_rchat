from django.shortcuts import render, HttpResponse, redirect
from .models import Messages, NewTable
from .forms import MessagesForm, NewTableForm
from .myclasses import Username


def index(request):
    uname = Username('none-1')
    if request.method == 'POST':
        form = MessagesForm(request.POST)
        if form.is_valid():
            uname.name = form['name'].value()
            form.save()


    messages = Messages.objects.order_by('id')
    if uname.name == 'none-1':
        form = MessagesForm()
    else:
        form = MessagesForm(initial={'name': uname.name})
    context = {'title': 'Главная страница сайта', 'messages': messages, 'form': form, 'name': uname.name}
    return render(request, 'main/index.html', context)


def first(request):
    if (request.method == 'POST'):
        form = NewTableForm(request.POST)
        if form.is_valid():
            form.save()

    tables = NewTable.objects.order_by('id')
    form = NewTableForm()
    context = {'title': 'первый раздел сайта', 'tables': tables, 'form': form}
    return render(request, 'main/first.html', context)
