from django.shortcuts import render
# from django.http import HttpResponse

def about(request):
    # return HttpResponse("Rango says here is the about page! <a href = '/rango/'>Index</a>")
    context_dict = {'boldmessage': 'This tutorial has been put together by coldmoon6261.'}
    return render(request, 'about/about.html', context=context_dict)
