from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'myapp/index.html')

def kanji(request):
    return render(request,'myapp/kanji.html')

def test(request):
    return render(request,'myapp/test.html')

def conversation(request):
    return render(request,'myapp/conversation.html')