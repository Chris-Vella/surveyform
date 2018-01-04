from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render (request, 'index.html')

def formProcess(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1

    request.session['data'] = {
        "Name": request.POST['name'],
        "Dojo Location": request.POST['dojo_loc'],
        "Favorite Language": request.POST['fave_lang'],
        "Comments": request.POST['comments']
    }
    return redirect('/show_results')

def showResults(request):
    print "Show results!"
    print request.session
    return render(request, 'results.html')