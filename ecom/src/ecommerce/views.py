from django.http import HttpResponse
from django.shortcuts import render

from .forms import ContactForm


def home_page(request):
    context = {
        "title": "Hello World!",
        "content": "Welcome to the home page."
    }
    return render(request, "home_page.html", context)


def about_page(request):
    context = {
        "title": "About Page",
        "content": " Welcome to the about page."
    }
    return render(request, "home_page.html", context)


def contact_page(request):
    contact_form = ContactForm()
    context = {
        "title": "Contact",
        "content": "welcome to the contact page.",
        "form": contact_form
    }
    if request.method == "POST":
        print(request.POST)
        print(request.POST.get('fullname'))
        print(request.POST.get('email'))
        print(request.POST.get('content'))
    return render(request, "contact/view.html", context)


# def home_page_old(request):
   #   html_ ="""
    #  <!doctype html>
# <html lang="en">

# <head>
   #   <meta charset="utf-8">
    #  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    # <!-- Bootstrap core CSS -->
    # <link href="../../dist/css/bootstrap.min.css" rel="stylesheet">
# </head>

# <body>

   #   <div class='text-center'>
    #      <h1>Hello, world!</h1>
    # </div>

    # <!-- Bootstrap core JavaScript
    #  ================================================== -->
    # <!-- Placed at the end of the document so the pages load faster -->
    # <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
    #    crossorigin="anonymous"></script>
    # <script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery-slim.min.js"><\/script>')</script>
    # <script src="../../assets/js/vendor/popper.min.js"></script>
    # <script src="../../dist/js/bootstrap.min.js"></script>
# </body>

# </html>
# """
   #   return HttpResponse(html_)
