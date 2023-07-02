from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm
from .models import Works
from .utils import search_works, paginate_works
from crm.models import Order
from django.contrib.auth.models import User
from crm.forms import OrderForm
from django.contrib import messages
from sendmessage import send_telegram
from django.core.mail import send_mail, BadHeaderError


def home(request):
    works = Works.objects.all()
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            subject = 'Message'
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'content': form.cleaned_data['content'],
            }
            message = '\n'.join(body.values())
            try:
                send_mail(subject, message, form.cleaned_data['email'], ['vsitkov99@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            messages.success(request, 'Сообщение отправлено')
            return redirect('home')
    context = {
        'works': works,
        'form': form,
    }
    return render(request, 'portfolio/home.html', context)


def catalog(request):
    works, search_query = search_works(request)
    custom_range, works = paginate_works(request, works, 6)

    context = {
        'works': works,
        'search_query': search_query,
        'custom_range': custom_range,
    }
    return render(request, 'portfolio/catalog.html', context)


def work_main(request, pk):
    order_works = get_object_or_404(Works, id=pk)
    form = OrderForm(request.POST or None, initial={'order_works': order_works})

    if request.method == 'POST':
        form = OrderForm(request.POST or None, initial={'order_works': order_works})
        if form.is_valid():
            form.save()
            send_telegram(tg_work=str(form.cleaned_data.get('order_works')),
                          tg_name=form.cleaned_data.get('order_name'),
                          tg_phone=str(form.cleaned_data.get('order_phone')),
                          tg_email=form.cleaned_data.get('order_email'))
            if form.errors:
                messages.error(request, 'Данные введены не верно')
                messages.error(request, form.errors)
            else:
                messages.success(request, 'Заявка отправлена')
            return redirect('work-main', pk=order_works.id)

    context = {
        'order_works': order_works,
        'form': form,
    }
    return render(request, 'portfolio/work_main.html', context)


def about(request):
    return render(request, 'portfolio/about.html')


def contact(request):
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            subject = 'Message'
            body = {
                'name': form.cleaned_data['name'],
                'email': form.cleaned_data['email'],
                'content': form.cleaned_data['content']
            }

            message = '\n'.join(body.values())
            try:
                send_mail(subject, message, form.cleaned_data['email'], ['vsitkov99@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Найден некорректный заголовок')
            messages.success(request, 'Сообщение отправлено')
            return redirect('home')
    context = {
        'form': form,
    }
    return render(request, 'portfolio/contact.html', context)
