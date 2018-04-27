from django.shortcuts import render, redirect, HttpResponse
from .forms import OrganizationForm

# Create your views here.

def new_org(request):
    if request.method == 'POST':
        form = OrganizationForm(request.POST)

        if form.is_valid():
            form.save()

    form = OrganizationForm()

    context = {
        'type': 0,
        'form': form,
    }

    return render(request, 'organization/org_detail.html', context)