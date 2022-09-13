# This is not a default file. I have created this file - Darshan

import os
from django.http import HttpResponse
from django.shortcuts import render

# Practice Code 1
# def index(request):
#     return HttpResponse("<h1>Hello Virat Bhai</h1> <a href='https://www.youtube.com/'><h2>YouTube</h2></a>")
#
# def about(request):
#     return HttpResponse("About Virat Bhai")
#
# def exercise_1(request):
#     module_dir = os.path.dirname(__file__)
#     file_path = os.path.join(module_dir, 'one.txt')     # full path to text.
#     txt_file = open(file_path, 'rt')
#     txt = txt_file.read()
#     return HttpResponse(txt)


def index(request):
    params = {'name': 'Virat', 'field': 'Django Project'}
    return render(request, 'index.html', params)
    # return HttpResponse("<h1>Home</h1> <a href='http://127.0.0.1:8000/char_count/'><button>Char Count</button></a>")


def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Get values of checkboxes (on/off)
    removepunc = request.POST.get('remove_punc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    removenewlines = request.POST.get('remove_new_lines', 'off')
    removeextraspaces = request.POST.get('remove_extra_spaces', 'off')
    countchars = request.POST.get('count_chars', 'off')

    # print(removepunc)
    # print(djtext)

    # Analyze the text
    if removepunc=='on':
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char in punctuations:
                analyzed = analyzed + ''
            else:
                analyzed = analyzed + char
        params = {'purpose': 'Punctuations Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if fullcaps=='on':
        analyzed = djtext.upper()
        params = {'purpose': 'Changed To Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if removenewlines=='on':
        analyzed = ' '.join(djtext.split())
        params = {'purpose': 'New Lines Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if removeextraspaces=='on':
        analyzed = ''
        n = len(djtext)
        for index,char in enumerate(djtext):
            if index!=n-1:
                if not(djtext[index]==' ' and djtext[index+1]==' '):
                    analyzed = analyzed + char
        params = {'purpose': 'Extra Spaces Removed', 'analyzed_text': analyzed}
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if countchars=='on':
        analyzed = 'Total Characters: ' + str(len(djtext))
        params = {'purpose': 'Number Of Characters', 'analyzed_text': analyzed}
        # return render(request, 'analyze.html', params)

    if removepunc!='on' and fullcaps!='on' and removenewlines!='on' and removeextraspaces!='on' and countchars!='on':
        return HttpResponse("<h1>Please Select Any Operation, Try Again...</h1>")

    return render(request, 'analyze.html', params)


def ex1(request):
    s = '''
        <h2> Navigation Bar </h2> 
        <a href="https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9"> Django Code With Harry Bhai </a> <br>
        <a href="https://www.facebook.com/"> Facebook </a> <br>
        <a href="https://www.flipkart.com/"> Flipkart </a> <br>
        <a href="https://www.hindustantimes.com/"> News </a> <br>
        <a href="https://www.google.com/"> Google </a> <br>
    '''
    return HttpResponse(s)


# Practice Code 3
# def ex1(request):
#     s = '''
#      <head><link href="https://fonts.googleapis.com/css?family=Abel" rel="stylesheet"></head>
#      <style> .h1,.h2,.h3,.h4,.h5,.h6,h1,h2,h3,h4,h5,h6 {
#         margin-bottom: .5rem;
#         font-family: 'abel', sans-serif;
#         font-weight: 700;
#         line-height: 1.2
#         } body {
#         font-size: 1rem;
#         background-color: Cyan }
#     </style>
#      <h1>My Website</h1> <a href="https://rohandas28.github.io/"> Click To Visit My Tiny Little Website!</a>
#      <h1>Harry Bhai Ka Website </h1> <a href="https://www.codewithharry.com/"> Click To Visit The Best Website!</a>
#      <h1>My Favourite Movie </h1> <a href= "https://www.google.com/search?q=interstellar&oq=interstellar&aqs=chrome..69i57j69i65.6672j0j1&sourceid=chrome&ie=UTF-8"> Click to See!</a>
#      <h1>My Favourite Youtube creator </h1> <a href="https://www.youtube.com/channel/UCeVMnSShP_Iviwkknt83cww"> Click To Visit And Subscribe To Him!</a>
#      <h1>Psst! Follow Me On Github! LoL!</h1> <a href="https://github.com/RohanDas28"> Click To Visit And Follow!</a>
#     '''
#     return HttpResponse(s)


# Practice Code 2
# def capitalize_first(request):
#     return HttpResponse("<h1>Capitalize First</h1>")
#
# def new_line_remove(request):
#     return HttpResponse("<h1>New Line Remover</h1>")
#
# def space_remove(request):
#     return HttpResponse("<h1>Space Remover</h1>")
#
# def char_count(request):
#     return HttpResponse("<h1>Character Counter</h1> <a href='/'><button>Back To Home</button></a>")












