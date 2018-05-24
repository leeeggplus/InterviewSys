from django.shortcuts import render
from .models import Question
from .forms import QuestionForm

# Create your views here.
def all_questions(request):
    '''
    list all questions in question dashboard
    '''
    questions = Question.objects.all()
    context = {
        'questions': questions
    }
    return render(request, 'question/questions.html', context)


def new(request):
    '''
    Create 
    '''
    # POST
    if request.method == 'POST':
        form = QuestionForm(request.POST)

        if form.is_valid():
            form.save()  
            return redirect(all_questions)   

    # GET
    form = QuestionForm()
    context = {
        'type': 0,
        'form': form,
    }
    return render(request, 'question/question_detail.html', context)
