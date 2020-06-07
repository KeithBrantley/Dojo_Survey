from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Wooo I got it!")

def results(request):
    return HttpResponse("This is the response page!")

def number_of_results(request, num_of_results):
    return HttpResponse(f"I have {num_of_results} as a result")