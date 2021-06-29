from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')
#main homepage

def analyze(request):
    #get the text for analyze page
    djtext = request.POST.get('text','default')

    #Checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount' , 'off')

    #Check which checkbox is on
    if(removepunc =="on"):
        punctuations = ''' !()-[]{};:'"\,<>./?@#$%^&*_~ '''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed+char

        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if(fullcaps == "on"):
        analyzed=""
        for char in djtext:
            analyzed= analyzed+ char.upper()
        params = {'purpose': 'Change to Upper case', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char!= '\n' and char!='\r':
                analyzed = analyzed + char

        params = {'purpose': 'Removed New Lines', 'analyzed_text': analyzed}
        djtext = analyzed
        #return render(request, 'analyze.html', params)

    if(extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext=analyzed
        #return render(request, 'analyze.html', params)

    if (charcount == "on"):
        count=0
        for char in djtext:
            if char!=" ":
                 count = count + 1

        params = {
            'purpose': 'Count Character',
            'analyzed_text': len(djtext)
        }
        djtext=analyzed

    if(removepunc != "on" and newlineremover != "on" and extraspaceremover != "on" and fullcaps != "on"):
        return HttpResponse("ERROR!! Please Select Atleast One Operation")

    return render(request, 'analyze.html', params)

def aboutus(request):
    return render(request, 'about.html')
#about us page
def contactus(request):
    return render(request, 'contact.html')
#contact us page