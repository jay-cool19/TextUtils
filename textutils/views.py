#Created by Jayadev
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def analyze(request):
    #Get the text
    djtext = request.POST.get('text','default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc','off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    # Check which checkbox is on
    if removepunc == 'on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analized = ""
        for char in djtext:
            if char not in punctuations:
                analized = analized + char
        params = {'purpose':'Removing Punctuation', 'analyzed_text':analized}
        djtext = analized
    if fullcaps == 'on':
        analized = ""
        for char in djtext:
            analized = analized + char.upper()
            params = {'purpose': 'Change to Upper Case', 'analyzed_text': analized}
            djtext = analized
    if newlineremover == 'on':
        analized = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analized = analized + char
            params = {'purpose': 'Removed NewLines', 'analyzed_text': analized}
            djtext = analized
    if extraspaceremover == "on":
        analized = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analized = analized + char
        params = {'purpose': 'Removed Extra Space', 'analyzed_text': analized}
        djtext = analized
    return render(request, 'analyze.html', params)
