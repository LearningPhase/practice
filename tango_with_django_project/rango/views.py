from django.http import HttpResponse

def index(request):
    #This function states that if we get a request then
    # Then HttpResponse will return the string below
    return HttpResponse("Rango says Hello World! <a href='/rango/about'>About<a/>")
    # end quotations must encompass everything

def about(request):
    #creating an 'about' view for anyone who searching the \about\ in a url
    return HttpResponse("Here is the about page. <a href='/rango/'>Index<a/>")
