from django.shortcuts import render

# Create your views here.
def heavymain(request):
    return render(request,'heavymain.html')


def index(request):
    return render(request, 'light_main.html')

def oneselection(request):
    return render(request, 'one_selection.html')    


def heavydetail(request): 
    return render(request,'heavydetail.html')   

def heavyfirst(request):
       return render(request,'heavyfirst.html')