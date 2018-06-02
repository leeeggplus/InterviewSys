from django.urls import path
from apps.search.views import landing


urlpatterns= [    
    path('', landing, name='search_landing'),     
];