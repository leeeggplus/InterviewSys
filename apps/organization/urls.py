from django.urls import path
from apps.organization.views import new, all_orgs, delete, modify


urlpatterns= [    
    path('all_orgs/', all_orgs, name='organization_all_orgs'), 
    path('new/', new, name='organization_new'), 
    path('delete/<int:org_id>/', delete, name='organization_delete'), 
    path('modify/<int:org_id>/', modify, name='organization_modify'), 
];