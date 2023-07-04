# I have created this file
from django.http import HttpResponse
from django.shortcuts import render


def analize(request):
    punctuations = '''!"#$%&'()*+, -./:;<=>?@[\]^_`{|}~'''

    text = request.POST.get('text', 'default')
    print(text)
    remove_punc = request.POST.get('removepunc', 'off')
    character_count = request.POST.get('character_count', 'off')

    analized_text = ''
    if remove_punc != "off" and text != 'default':

        for char in text:
            if char not in punctuations:
                analized_text += char
    elif character_count != 'off':
        char = 0
        for i in text:
            if i != ' ':
                char += 1
        params = {
            "purpose": "Remove punctuations",
            "analyzed_text": f"count of givean text ==> {char}"
        }
        return render(request, 'analize.html', params)

    else:
        return HttpResponse(f"No need for punctuation removeal for the string {analized_text}")
    params = {
        "purpose": "Remove punctuations",
        "analyzed_text": analized_text
    }

    return render(request, 'analize.html', params)


def index(request):
    return render(request, 'index.html')


def ReadContent(request):
    with open('E:\\CODES\\Django_CWH\\textutils\\TextContent\\Content.txt', "r") as f:
        data = f.read()
        f.close()
    return HttpResponse(data)


def about(request):
    return HttpResponse("Hello, About!")
