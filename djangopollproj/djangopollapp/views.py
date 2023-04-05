from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.utils import timezone

from django.shortcuts import render,redirect

from .filters import PollFilter
from .models import User,Poll,Choice
from .forms import RegisterForm,LoginForm,PollForm,ChoiceForm
from django.http import HttpResponse
from django.contrib import auth
from django.contrib.auth import login,authenticate
from django.contrib.auth.hashers import make_password,check_password
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import permission_required
from django.shortcuts import get_object_or_404


def PollView(request):
    print("@@@@", request.user)
    if request.method == 'POST':
        form = PollForm(request.POST)
        if form.is_valid():
            poll = form.save(commit=False)
            # poll.owner = request.user
            poll.is_active = True
            poll.owner=request.user
            poll.save()

            return HttpResponse("poll created")


    else:
        form = PollForm()
    return render(request, 'poll.html', {'form': form})


def ChoiceView(request):
    count = Choice.objects.all().count()
    message = None
    print(count)
    if request.method == 'POST':
        form = ChoiceForm(request.POST)
        if form.is_valid():
            print(request.user)
            if Choice.objects.filter(user=request.user).exists():
                # message = "User already voted"
                return HttpResponse('exists')
            current_time = timezone.now()
            print(current_time)
            poll = form.cleaned_data.get('poll')
            print(poll.end_date)
            if poll.end_date < current_time:
                return redirect('count/')
            poll = form.save(commit=False)
            poll.save()
            Choice.objects.update(user=request.user)
            message = "Choices created"
    else:
        form = ChoiceForm()
        message = None
    return render(request, 'choice.html', {'form': form,'count':count,'message':message})

def Count(request):
    count = Choice.objects.all().count()
    print(count)
    return render(request,'count.html',{'count':count})

# @permission_required('Poll.can_edit_poll', raise_exception=True)

def PollViewall(request):
    poll_data = Poll.objects.all()
    paginator = Paginator(poll_data, 2)
    page_number = request.GET.get('page')
    poll_data = paginator.get_page(page_number)
    return render(request,'pollall.html',{'poll_data':poll_data})


def Pollupdate(request, id):
    poll_data = Poll.objects.get(id=id)
    # print(poll_data.owner)
    if request.method == 'POST':
        if poll_data.owner == request.user:
            title = request.POST.get("title",False)
            description = request.POST["description"]
            pub_date = request.POST["pub_date"]
            end_date = request.POST["end_date"]
            poll_data.title = title
            poll_data.description = description
            poll_data.pub_date = pub_date
            poll_data.end_date = end_date
            poll_data.id=id
            print(poll_data.id)
            poll_data.save()
            return HttpResponse('updated successfull')
        else:
            return HttpResponse('no permission to update')


    return render(request, 'pollupdate.html', {"poll_data": poll_data})

def Polldelete(request, id):
    Poll_data = Poll.objects.get(id=id)
    print()
    print(Poll_data.owner)
    if Poll_data.owner == request.user:
        Poll_data.delete()
        return HttpResponse('deleted')
    else:
        return HttpResponse('no permissions to delete')


from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import render, redirect

def RegisterView(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login/')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def LoginView(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            print(request.user)
            return redirect('home/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


def Home(request):
    return render(request,'home.html')

def WelcomeHome(request):
    return render(request,'welcomehome.html')

from django_filters.views import FilterView


class NumericPaginator:
    pass


def PollViewall(request):
    f = PollFilter(request.GET, queryset=Poll.objects.all())
    paginator = Paginator(f.qs,2)
    page = request.GET.get('page')

    try:
        polls = paginator.page(page)
    except PageNotAnInteger:
        polls = paginator.page(1)
    except EmptyPage:
        polls = paginator.page(paginator.num_pages)

    return render(request, 'pollall.html', {'filter': f, 'polls': polls})