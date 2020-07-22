from django.http import HttpResponse
#from django.template import loader
from django.http import Http404
from django.shortcuts import get_object_or_404, render

from .models import Question

def index(request):
    # chapter 1
#    return HttpResponse("Hello, world. You're at the data_regist index.")
    # chapter 3
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
#    template = loader.get_template('data_regist/index.html')
#    context = {
#        'latest_question_list': latest_question_list,
#    }
#    return HttpResponse(template.render(context, request))
    context = {'latest_question_list': latest_question_list}
    return render(request, 'data_regist/index.html', context)

def detail(request, question_id):
#    try:
#        question = Question.objects.get(pk=question_id)
#    except Question.DoesNotExist:
#        raise Http404("Question does not exist")
#    return render(request, 'data_regist/detail.html', {'question': question})
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'data_regist/detail.html', {'question': question})

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
