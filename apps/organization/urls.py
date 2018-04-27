from django.urls import path
from apps.organization.views import new_org


urlpatterns= [    
    # path('all/', all_orgs, name='organization_all_orgs'),
    path('new/', new_org, name='organization_new_org'), 
];