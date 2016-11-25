from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm, SignupForm, LoginForm
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

from django.contrib import auth

# Create your views here.
from django.http import HttpResponse 
def test(request, *args, **kwargs):
        return HttpResponse('OK')

def answer(request):
    if request.method == "POST":
        form = AnswerForm(request.POST)
        form._user = request.user
        if form.is_valid():
            answer = form.save()
            url = answer.get_url()
            return HttpResponseRedirect(url)
        else:
            answer = form.save()
            url = answer.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()

def qa_full(request, id):
    try:
        question = Question.objects.get(id=id)
        answers = question.answer_set.all()
        form = AnswerForm()
    except Question.DoesNotExist:
            raise Http404
    return render(request, 'question.html', {
        'question':question,
        'answers':answers,
        'form':form,
        } )


def questions_list_all(request):
    questions = Question.objects.order_by('-id')
    limit = request.GET.get('limit',10)
    page = request.GET.get('page',1)
    paginator = Paginator(questions,limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request,'questions.html', {
        'questions':  page.object_list,
        'paginator': paginator,
        'page': page,
        })


def questions_list_popular(request):
    questions = Question.objects.order_by('-rating')
    limit = request.GET.get('limit',10)
    page = request.GET.get('page',1)
    paginator = Paginator(questions,limit)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request,'questions.html', {
        'questions':  page.object_list,
        'paginator': paginator,
        'page': page,
        })

def question_add(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        form._user = request.user
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'question_add.html', {
        'form' : form,
        })

def signup(request):

    if request.method == "POST":
        form = SignupForm(request.POST)
        username = request.POST['username']
        password = request.POST['password']
        if form.is_valid():
            form.save()
            user = auth.authenticate(username=username, password=password)
            auth.login(request, user)
            return HttpResponseRedirect('/')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {
        'form' : form,
        })


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        #form = LoginForm(request.POST)
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            print("AUTH OK")
            return HttpResponseRedirect('/')
        else:
            print("AUTH NOT OK")
            return HttpResponseRedirect('/')
    else:
        form = LoginForm()
    return render(request, 'login.html', {
        'form' : form,
        })
