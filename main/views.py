from django.shortcuts import render, HttpResponse, redirect
from .models import Messages, NewTable
from .forms import MessagesForm, NewTableForm
from django.http import HttpResponseRedirect


def index(request):
    if 'name' not in request.session:
        request.session['name'] = 'none-1_session'
    if request.method == 'POST':
        form = MessagesForm(request.POST)
        if form.is_valid():
            request.session.set_expiry(0)
            request.session['name'] = form['name'].value()
            form.save()
            form = MessagesForm()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    messages = Messages.objects.order_by('-id')[0:4]
    if request.session['name'] == 'none-1_session':
        form = MessagesForm()
    else:
        form = MessagesForm(initial={'name': request.session['name']})
        form.fields['name'].widget.attrs['readonly'] = True
    context = {'title': 'Главная комната', 'messages': messages, 'form': form, 'name': request.session['name']}
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
