from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render
from qa.models import Question
from django.core.paginator import Paginator

# Create your views here.
from django.http import HttpResponse 
def test(request, *args, **kwargs):
        return HttpResponse('OK')


def question_text(request, id):
    try:
        question = Question.objects.get(id=id)
    except Question.DoesNotExist:
            raise Http404
    return render(request, 'question.html', {'question':question} )


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
