from django.urls import path
from apps.search.views import landing, search_org, search_question


urlpatterns= [    
    path('', landing, name='search_landing'),  
    path('orgnization/<str:resume_name>/', search_org, name='search_search_org'),    
    path('question/<str:resume_name>/', search_question, name='search_search_question'),    
];