from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, "index.html")

def about(request):
    return HttpResponse("About page <a href='/'> back to home</a>")

def analyze(request):
    djtext= request.POST.get('text','default')
    rempunc= request.POST.get('removepunc','off')
    toUpper=request.POST.get('toUpper','off')
    removeNewLine=request.POST.get('removeNewLine','off')
    extraSpaceRemover=request.POST.get('extraSpaceRemover','off')
    characterCount=request.POST.get('characterCount','off')
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    if(rempunc=='on'):
        analyzed =""
        for char in djtext:
            if char not in punc:
                analyzed=analyzed+char   
        params= {
            'purpose':'Removed Punctutations',
            'analyzed_text':analyzed
        }
        djtext=analyzed

    if(toUpper=='on'):
        analyzed =""
        for char in djtext:
            analyzed=analyzed+char.upper()  
        params= {
            'purpose':'Changed to UpperCase',
            'analyzed_text':analyzed
        }
        djtext=analyzed

    if(removeNewLine=='on'):
        analyzed =""
        for char in djtext:
            if(char!='\n' and char!='\r'):
                analyzed=analyzed+char 
        params= {
            'purpose':'Removed New Line',
            'analyzed_text':analyzed
        }
        djtext=analyzed

    if(extraSpaceRemover=='on'):
        analyzed =""
        for index,char in enumerate(djtext):
            if not(djtext[index]==' ' and index+1!=len(djtext) and djtext[index+1]==' '):
                analyzed=analyzed+char 
        params= {
            'purpose':'Removed Extra Space',
            'analyzed_text':analyzed
        }
        djtext=analyzed

    if(rempunc!='on' and toUpper!='on' and removeNewLine!='on' and extraSpaceRemover!='on'):
        return HttpResponse('Error')
    
    return render(request,"analyze.html",params)
    
    