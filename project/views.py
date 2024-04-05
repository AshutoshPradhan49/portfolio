from django.http import HttpResponse
from django.shortcuts import render #for HTML files

def aboutUs(request):
    return HttpResponse("Welcome to About-Us page.")
def courseDetails(request, courseid):
    return HttpResponse(courseid)
def homePage(request):
    data = {
        'title': 'Portfolio | Ashutosh Pradhan'
    }
    return render(request, "index.html", data)
def contact_view(request):
    return render(request, "contact.html")