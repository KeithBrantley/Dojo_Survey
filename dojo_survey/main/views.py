from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'index.html')

def results(request):
    # print(request.POST)
    # print(request.POST['name'])
    context={
        'name': request.POST["name"],
        'dojo_location' : request.POST["dojo_location"],
        'favorite_language': request.POST["favorite_language"],
        'comment': request.POST["comment"]
    }
    return render(request, 'results.html', context)

def direct_to_index(request):
    return redirect('/')

