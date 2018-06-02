from django.shortcuts import render, redirect, HttpResponse, get_object_or_404

# Create your views here.
def landing(request):
    '''
    landing of search
    '''
    context = {
        
    }
    return render (request, 'search/landing.html', context)
