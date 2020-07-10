from django.shortcuts import render

# Create your views here.
def ProductView(request):
    return render(request, 'html/basic-table.html')