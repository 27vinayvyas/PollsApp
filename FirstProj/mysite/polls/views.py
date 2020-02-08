from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Questions
# Create your views here.
def index(request):
    latest_question=Questions.objects.order_by('-pub_date')[:5]
    context={'latest_question':latest_question}
    return render(request,'polls/index.html',context)

def detail(request,question_id):
    question=get_object_or_404(Questions,id=question_id)
    #question = Questions.objects.get(id=question_id)
    return render(request,'polls/details.html',{'question':question})

def results(request,question_id):
    question=get_object_or_404(Questions,id=question_id)
    return render(request,'polls/results.html',{'question':question})

def votes(request,question_id):
    question=get_object_or_404(Questions,id=question_id)
    try:
        selected_choice=question.choice_set.get(id=request.POST['choice'])
    except:
        return render(request,'polls/details.html',{'question':question,'error_message':"please fill a choice"})
    else:
        selected_choice.votes +=1
        selected_choice.save()

        return HttpResponseRedirect(reverse('polls:results', args=[question.id]))   