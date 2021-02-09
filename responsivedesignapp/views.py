from django.shortcuts import render

# Create your views here.

def products(request):
    context = {}
     
    return render(request, 'responsivedesignapp/product.html', context)    


def homes(request):
    context = {}
     
    return render(request, 'responsivedesignapp/home.html', context)   


def contacts(request):
    context = {}
     
    return render(request, 'responsivedesignapp/contactus.html', context)



def peoples(request):
    context = {}
     
    return render(request, 'responsivedesignapp/people.html', context)
 
