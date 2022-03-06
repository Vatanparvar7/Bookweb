from django.shortcuts import render



def page_not_found_view(request, exception):
    return render(request, '404.html', )

def handle_server_found(request,):
    return render(request, '404.html', )