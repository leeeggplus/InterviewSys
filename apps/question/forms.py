from django.forms import ModelForm
from .models import Question

class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ('question_body', 'answer_body', 'level', 'tags', )
