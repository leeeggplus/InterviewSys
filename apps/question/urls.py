from django.urls import path
from apps.question.views import all_questions, new, modify, delete


urlpatterns= [    
    path('all_questions/', all_questions, name='question_all_questions'), 
    path('new/', new, name='question_new'), 
    path('modify/<int:question_id>/', modify, name='question_modify'), 
    path('delete/<int:question_id>/', delete, name='question_delete'), 
];