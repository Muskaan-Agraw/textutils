from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def ex1(request):
    sites = ['''<h1>For Entertainment  </h1> <a href="https://www.youtube.com/"> Youtube Videos</a> ''',
             '''<h1>For Interaction  </h1> <a href="https://www.facebook.com/"> Facebook</a> ''',
             '''<h1>For Insight  </h1> <a href="https://www.ted.com/talks"> Ted Talks</a> ''',
             '''<h1>For Internship  </h1> <a href="https://www.internshala.com">Internship</a> ''']
    return HttpResponse((sites))
def analyze(request):
    # Get the text
    djtext = request.POST.get('text', 'default')

    # Check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')

    # If no checkbox is selected, return an error message
    if removepunc == "off" and fullcaps == "off" and newlineremover == "off" and extraspaceremover == "off" and charcount == "off":
        return HttpResponse("Error: Please select at least one operation")

    analyzed = djtext  # Initialize with input text

    # Apply transformations one by one based on checkbox selection
    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = "".join(char for char in analyzed if char not in punctuations)

    if fullcaps == "on":
        analyzed = analyzed.upper()

    if newlineremover == "on":
        analyzed = "".join(char for char in analyzed if char != "\n" and char != "\r")

    if extraspaceremover == "on":
        analyzed = " ".join(analyzed.split())  # Removes extra spaces

    # Prepare params dictionary for rendering
    params = {'purpose': 'Text Processed', 'analyzed_text': analyzed}


    return render(request, 'analyze.html', params)
