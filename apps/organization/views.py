from django.shortcuts import render, redirect, HttpResponse
from .forms import OrganizationForm
from .models import Organization

# Create your views here.

def all_orgs(request):
    '''
    list all organizations in org dashboard
    '''
    orgs = Organization.objects.all()
    context = {
        'orgs': orgs
    }
    return render(request, 'organization/orgs.html', context)


def new_or_modify(request):
    # POST
    if request.method == 'POST':
        form = OrganizationForm(request.POST)

        if form.is_valid():
            org_name = form.cleaned_data['name']             

            try:                                     
                exist = Organization.objects.get(name=org_name)    
                # exist - update org info  
                exist.name = form.cleaned_data['name']
                exist.manager_name = form.cleaned_data['manager_name']
                exist.manager_alias = form.cleaned_data['manager_alias']
                exist.manager_email = form.cleaned_data['manager_email']
                exist.parent_org = form.cleaned_data['parent_org']
                exist.save()  

                # clear tags
                exist.skills.clear()

                for tag in form.cleaned_data['skills']:  
                    exist.skills.add(tag)                

            except Organization.DoesNotExist:
                # does not exist, directly save the form                
                form.save()
            
            return redirect(all_orgs)   

    # GET
    form = OrganizationForm()

    context = {
        'type': 0,
        'form': form,
    }

    return render(request, 'organization/org_detail.html', context)


def delete(request, org_id):
    '''
    delete organization by ID: org_id from URL
    '''
    try:
        org_to_delete = Organization.objects.get(id=org_id)
        org_to_delete.delete()

    except Organization.DoesNotExist:
        pass    

    orgs = Organization.objects.all()
    context = {
        'orgs': orgs
    }

    return render(request, 'organization/orgs.html', context)