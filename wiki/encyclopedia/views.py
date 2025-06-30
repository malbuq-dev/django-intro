from django.shortcuts import render, redirect
from django.http import HttpResponse
from markdown import markdown
from random import randint
from . import util


def index(request):
    if request.method == "POST":
        name = request.POST['q']
        
        if util.get_entry(name) != None:
            return redirect('readPage', name=name)
        else:
            entries = util.list_entries()
            suggestionlist = []

            for entry in entries:
                if  entry.lower().find(name.lower()) != -1:
                    suggestionlist.append(entry)
            
            if len(suggestionlist) != 0:
                return render(request, 'encyclopedia/suggestions.html', {
                    "entries" : suggestionlist,
                })
            else:
                return redirect('readPage', name=name)
           
    else:
        return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def readPage(request, name):
    if util.get_entry(name) != None:
        content = markdown(util.get_entry(name))
        return render(request, "encyclopedia/page.html", {
            "title" : name,
            "content" : content,
        })
    else:
        return render(request, "encyclopedia/notFound.html", {
            "title" : name,
        })
    
def createNewPage(request):
    if request.method == "POST":
        title = request.POST['title'].title()
        if util.get_entry(title) == None:
            content = f"#{title}\n{request.POST['content']}"
            util.save_entry(title, content)
            return redirect('readPage', name=title)
        else:
            return render(request, "encyclopedia/titleAlreadyInUse.html")
    else:
        return render(request, "encyclopedia/createNewPage.html")
        
def randomPage(request): #for views.py
    randomIndex = randint(0, len(util.list_entries()) - 1)
    pageName = util.list_entries()[randomIndex]
    return redirect('readPage', name=pageName)
    
def editPage(request, title):
    if request.method == "POST":
        content = request.POST['content']
        print(content)
        print(title)
        util.save_entry(title, content)
        return redirect('readPage', name=title)
        
    content = util.get_entry(title)
    return render(request, "encyclopedia/editPage.html", {
        "content": content,
        "title": title,
    })




    

