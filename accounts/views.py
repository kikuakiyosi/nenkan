from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .models import CustomUser
from django.contrib.auth import login, logout
from .forms import ContactForm
from django.views import generic
from django.views.generic import FormView
from django.template import loader
from .models import Tweet
from django.urls import reverse


def index(request):
    tweet_list = Tweet.objects.all()
    return render(
        request,
        'index.html',
        {'tweet_list': tweet_list}
    )

def signup(request):
    username = request.POST['username']
    password = request.POST['password']
    new_user = CustomUser(username=username, password=password)
    new_user.save()
    return HttpResponse('ユーザーの作成に成功しました')


def signin(request):
    username = request.POST['username']
    password = request.POST['password']
    try:
        user = CustomUser.objects.get(username=username)
    except CustomUser.DoesNotExist:
        return HttpResponse('ログインに失敗しました')

    if user.password == password:
        login(request, user)  # これを実行するとユーザをログイン状態にできる
        return HttpResponseRedirect('/')
    else:
        return HttpResponse('ログインに失敗しました')


def signout(request):
    logout(request)
    return HttpResponseRedirect('/')

from django.core.mail import EmailMessage

# EmailMessage のインスタンスを作成する
emailMessage = EmailMessage(
        to=['fko2347003@stu.o-hara.ac.jp'],
        subject='This is subject',
        body='This is body',
)


emailMessage.send()




class ContactView(FormView,generic.ListView):
    model = Tweet
    template_name = 'index.html'  # TODO
    success_url = '/app/'
    form_class = ContactForm

    def form_valid(self, form):
        name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        message = form.cleaned_data['message']
        # メール送信などを行う
        
        emailMessage = EmailMessage(
        subject='お問い合わせがありました',
            body='name: {0}\nemail: {1}\nmessage: {2}'.format(name, email, message),
            to=['fko2347003@stu.o-hara.ac.jp'],
        )
        emailMessage.send()
        print(name, email, message)
        return super().form_valid(form)
        
    
def post(request):
    message = request.POST['message']
    name = request.POST['name']
    tweet = Tweet(message=message, name=name)
    tweet.save()
    return HttpResponseRedirect(reverse('accounts:index'))
