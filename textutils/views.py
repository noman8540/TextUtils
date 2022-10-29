# I have created this file - Noman
from django.http import HttpResponse
from django.shortcuts import render



# def about(request):
    # return HttpResponse('''About <a href="https://www.facebook.com/"> Noman fb page <a href="/"> <h1>Back</h1> ''')

# here <a href="/" Home - we used this for go back to the homepage means to the starting page

# def removepunc(request):
#     # get the text
#     djtext = (request.GET.get('text', 'default')) 
#     # analyze the text
#     print(djtext)
    
    
#     # first get is in the capital and
#     # second in the small for get the result of the text
#     # this means if any text written in the text area then the result give the text
#     # but if the text is not write then it give the result as default
#     return HttpResponse("remove punc")


# def analyze(request):
#     djtext = (request.GET.get('text', 'default'))
#     removepunc = (request.GET.get('removepunc', 'off'))
#     print(removepunc)
#     print(djtext) 
    
#     return HttpResponse("remove punc")


# def analyze(request):
#     djtext = (request.GET.get('text', 'default'))
#     analyzed = djtext
#     params = {'purpose': 'Removing punctutaions', 'analyzed_text': analyzed}
#     return render(request, 'analyze.html', params)



def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")


def about(request):
    return render(request, 'about.html')



def analyze(request):
    #Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    numberremover = request.POST.get('numberremover', 'off')

    #Check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
                
        params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if fullcaps=="on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose': 'Change To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            # if djtext[index] == " " and djtext[index+1] == " ":
                # pass
            # or 
            if not(djtext[index] == " " and djtext[index+1] == " "):
                analyzed = analyzed + char
                
        params = {'purpose': 'Extar Space Remover', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    
    if (numberremover == "on"):
        analyzed = ""
        numbers = '0123456789'

        for char in djtext:
            if char not in numbers:
                analyzed = analyzed + char
        
        params = {'purpose': 'Removed Number', 'analyzed_text': analyzed}
        djtext = analyzed
    
    
    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        
        params = {'purpose' : 'Remove NewLines', 'analyzed_text' : analyzed}
        # return render(request, 'analyze.html', params)
    
    # else:
    #     return HttpResponse("Error")

    

    if (removepunc != 'on' and newlineremover != 'on'  and fullcaps != 'on' and extraspaceremover != 'on' and numberremover != 'on'):
        return HttpResponse("Please select any Operation and try again!")

    
    return render(request, 'analyze.html', params)

