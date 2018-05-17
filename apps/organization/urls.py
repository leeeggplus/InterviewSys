from django.urls import path
from apps.organization.views import new_or_modify, all_orgs, delete


urlpatterns= [    
    path('all_orgs/', all_orgs, name='organization_all_orgs'), 
    path('new_or_modify/', new_or_modify, name='organization_new_or_modify'), 
    path('delete/<int:org_id>/', delete, name='organization_delete'), 
];