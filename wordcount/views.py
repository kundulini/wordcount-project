from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request , 'home.html')
    

def count(request):
    global fulltext
    global wordlist
    fulltext = request.GET['fulltext']    
    wordlist = fulltext.split() 
    print (fulltext)
    print (wordlist)
    return render(request, 'count.html',{'fulltext':fulltext ,'count':len(wordlist) })
    
def eggs(request):
    rep = 0
    fulltext2 = request.GET['fulltext2']   
    print(fulltext2)
    for i in wordlist :
        if i == fulltext2 :
            rep +=1
    return render(request, 'eggs.html', {'number': rep })
    
def about(request):
    return render(request, 'about.html')
    
    
    
    
