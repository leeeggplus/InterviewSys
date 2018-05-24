from django.urls import path
from apps.question.views import all_questions, new


urlpatterns= [    
    path('all_questions/', all_questions, name='question_all_questions'), 
    path('new/', new, name='question_new'), 
];