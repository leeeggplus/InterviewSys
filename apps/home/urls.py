from django.urls import path
from apps.home.views import landing


urlpatterns= [    
    # path('all/', all_orgs, name='organization_all_orgs'),
    path('', landing, name='home_landing'), 
];