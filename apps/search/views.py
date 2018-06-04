from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from apps.organization.models import Organization
from apps.question.models import Question

# Create your views here.
def landing(request):
    '''
    landing of search
    '''
    context = {
    }
    return render (request, 'search/landing.html', context)


def search_org(request, resume_name):
    '''
    search org via resume
    '''
    keywords, res1, res2, res3 = [], [], [], []

    if resume_name == "Resume_Mary_Huang":
        keywords = ["Windows OS", "Linux OS", "Hyper-V", ]

        res1 = Organization.objects.filter(skills__name__in=["Windows OS", "Windows", ])
        res2 = Organization.objects.filter(skills__name__in=["Linux OS", "Linux", ])
        res3 = Organization.objects.filter(skills__name__in=["Hyper-V", ])             

    if resume_name == "Resume_Ling":
        keywords = ["Storage", "TCP/IP", "Word", ]

        res1 = Organization.objects.filter(skills__name__in=["Storage", ])
        res2 = Organization.objects.filter(skills__name__in=["TCP/IP", ])
        res3 = Organization.objects.filter(skills__name__in=["Word", ])

    context = {
        "res1": res1,
        "res2": res2,
        "res3": res3,
        "keywords": keywords,
    }
    
    return render(request, 'search/org_result.html', context)


def search_question(request, resume_name):
    '''
    search question via resume
    '''
    keywords, level, res1, res2, res3 = [], [], [], [], []

    if resume_name == "Resume_Mary_Huang":
        keywords = ["Windows OS", "Linux OS", "Hyper-V", ]
        level = ["Advanced", "Senior", "Advanced", ]

        res1 = Question.objects.filter(tags__name__in=["Windows OS", "Windows", ], level=3)
        res2 = Question.objects.filter(tags__name__in=["Linux OS", "Linux", ], level=2)
        res3 = Question.objects.filter(tags__name__in=["Hyper-V", ], level=3)             

    if resume_name == "Resume_Ling":
        keywords = ["Storage", "TCP/IP", "Word", ]
        level = ["Senior", "Senior", "Senior", ]

        res1 = Question.objects.filter(tags__name__in=["Storage", ], level=2)
        res2 = Question.objects.filter(tags__name__in=["TCP/IP", ], level=2)
        res3 = Question.objects.filter(tags__name__in=["Word", ], level=2)

    context = {
        "res1": res1,
        "res2": res2,
        "res3": res3,
        "keywords": keywords,
        "level": level,
    }
    
    return render(request, 'search/question_result.html', context)