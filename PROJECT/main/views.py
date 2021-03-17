from django.shortcuts import render, redirect
import account.forms
import account.views
from django.utils import timezone

from .models import *
from .forms import *


def home(request):
    try:
        alarms = Clock.objects.filter(user=request.user)
    except:
        alarms = []

    form = ClockForm()

    if request.method == 'POST':
        print(request.POST)
        form = ClockForm(request.POST)
        if form.is_valid():
            temp = form.save(commit=False)
            temp.user = request.user
            temp.save()
        return redirect('/')

    talarms = []

    for i in alarms:
        print(i.settedtime, datetime.datetime.now())
        if i.settedtime.astimezone(timezone.utc).replace(tzinfo=None) < datetime.datetime.now():
            i.delete()
        else:
            talarms.append(i)

    context = {'tasks': talarms, 'form': form}

    return render(request, 'homepage.html', context)


class SignupView(account.views.SignupView):
    form_class = SignupForm

    def after_signup(self, form):
        super(SignupView, self).after_signup(form)


def home_view(request):
    context = {}

    context['form'] = InputForm()

    return render(request, "home.html", context)
