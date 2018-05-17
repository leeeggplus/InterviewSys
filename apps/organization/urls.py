from django.urls import path
from apps.organization.views import new_or_modify_org, all_orgs


urlpatterns= [    
    path('all_orgs/', all_orgs, name='all'), 
    path('new_or_modify/', new_or_modify_org, name='new_or_modify_org'), 
];