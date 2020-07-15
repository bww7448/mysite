from django.shortcuts import render
from django.http import request, HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
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
    choice_id = request.POST['choice'] #없으면 프로그램 에러 ㅠㅠ
    # request.POST.get('choice') #없으면 none 리턴
    #질문 조회

    question = Question.objects.get(id=question_id)
    #보기 조회
    choice = question.choice_set.get(id = choice_id)
    #투표수 증가
    choice.votes += 1
    #저장
    choice.save()
    return HttpResponseRedirect('/polls/%s/' %question_id)
    #return HttpResponseRedirect(reverse('detail', args = (question.id)))
    #return HttpResponse("You're voting on question %s." % question_id)
def reset(request, question_id):
    question = Question.objects.get(id = question_id)
    choice_list = question.choice_set.all()
    for choice in choice_list:
        choice.votes = 0
        choice.save()
    return HttpResponse('ok')
