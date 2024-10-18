from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    context = {
        "variable1": "this is sent",
        "variable2": "Mohammadi"
    }
    return render(request, 'index.html', context)
    #return HttpResponse("this is home page")
def about(request):
    return render(request, 'about.html')
    #return HttpResponse("this is about page")
def contact(request):
    return render(request, 'contact.html')
def products(request):
    return render(request, 'products.html')
def hardwareitems(request):
    return render(request, 'hardwareitems.html')
def safetyitems(request):
    return render(request, 'safetyitems.html')
def lightingproducts(request):
    return render(request, 'lightingproducts.html')
def plumbingitems(request):
    return render(request, 'plumbingitems.html')
def cleaningproducts(request):
    return render(request, 'cleaningproducts.html')
def paintingtools(request):
    return render(request, 'paintingtools.html')
def adhesivessealantsandtapes(request):
    return render(request, 'adhesivessealantsandtapes.html')
