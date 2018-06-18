from django.http import HttpResponse
from django.shortcuts import render


def home_page(request):
  return render(request, "home_page.html", {})

def about_page(request):
  return render(request, "home_page.html", {})

def contact_page(request):
  return render(request, "home_page.html", {})



#def home_page_old(request):
 #   html_ ="""
  #  <!doctype html>
#<html lang="en">

#<head>
 #   <meta charset="utf-8">
  #  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
   # <!-- Bootstrap core CSS -->
   # <link href="../../dist/css/bootstrap.min.css" rel="stylesheet">
#</head>

#<body>

 #   <div class='text-center'>
  #      <h1>Hello, world!</h1>
   # </div>

   # <!-- Bootstrap core JavaScript
   #  ================================================== -->
   # <!-- Placed at the end of the document so the pages load faster -->
   # <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
    #    crossorigin="anonymous"></script>
    #<script>window.jQuery || document.write('<script src="../../assets/js/vendor/jquery-slim.min.js"><\/script>')</script>
    #<script src="../../assets/js/vendor/popper.min.js"></script>
    #<script src="../../dist/js/bootstrap.min.js"></script>
#</body>

#</html>
#"""
 #   return HttpResponse(html_)