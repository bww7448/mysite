from django.shortcuts import render
from django.http import HttpResponse, Http404
from .models import Question

def index(request):
    q_list = Question.objects.order_by('pub_date')[:5]
    str_list = [q.question_text for q in q_list]
    html = ','.join(str_list)
    #return HttpResponse(html)
    return render(request, 'polls/index.html', {'latest_question_list':q_list})

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

    #return HttpResponse("You're looking at question %s." % question_id)

def results(request, question_id): # 투표 결과 페이지
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def votes(request, question_id): # 투표 페이지
    return HttpResponse("You're voting on question %s." % question_id)
