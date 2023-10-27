from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.shortcuts import render,get_object_or_404
# Create your views here.
from .models import Question



def index(request):
    q = Question.objects.order_by('-pub_date')[:5]
    #response = ','.join([p.question_text for p in q])
    #template = loader.get_template('index.html')
    context = {
        'questions_list': q
    }
    return render(request,'index.html',context)

def results(request,question_id):
    response = 'You are looking at the results of question %s'
    return HttpResponse(response % question_id)

def detail(request,question_id):
    '''
    try:
        q = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404('Question does not exist.')
    '''
    q = get_object_or_404(Question,pk=question_id)
    return render(request,'detail.html',{'question': q})

def vote(request,question_id):
    
    return HttpResponse('You are voting for question %s ' % question_id)