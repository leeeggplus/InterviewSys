from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
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


def modify(request, question_id):
    '''
    modify question details
    '''
    # GET
    if request.method == 'GET':
        question_to_modify = get_object_or_404(Question, id=question_id)
        form = QuestionForm(instance=question_to_modify)

        context = {
            'type': 1,
            'question_id': question_id,
            'form': form,
        }
        return render(request, 'question/question_detail.html', context)

    # POST
    else:
        form = QuestionForm(request.POST)        
        if form.is_valid():        
            # get existing instance
            exist = Question.objects.get(id=question_id)
            question_body = form.cleaned_data['question_body']            
            exist.answer_body = form.cleaned_data['answer_body']
            exist.level = form.cleaned_data['level']
            exist.save() 

            # clear & update tags.
            exist.tags.clear()
            for tag in form.cleaned_data['tags']:  
                exist.tags.add(tag)    
        

        questions = Question.objects.all()
        context = {
            'questions': questions
        }

        return redirect(all_questions)


def delete(request, question_id):
    '''
    delete question by ID: question_id from URL
    '''
    try:
        question_to_delete = Question.objects.get(id=question_id)
        question_to_delete.delete()

    except Question.DoesNotExist:
        pass    

    questions = Question.objects.all()
    context = {
        'questions': questions
    }

    return redirect(all_questions)
 
