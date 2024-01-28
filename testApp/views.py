from django.shortcuts import render

# Create your views here.
def name_view(request):

    return render(request, 'testApp/name.html')

def age_view(request):

    name = request.GET['name']
    response = render(request, 'testApp/age.html')
    response.set_cookie('name', name)

    return response

def gf_view(request):

    age = request.GET['age']
    response = render(request, 'testApp/gf.html')
    response.set_cookie('age', age)

    return response

def results_view(request):

    gfname = request.GET['gfname']
    name = request.COOKIES.get('name')
    age = request.COOKIES.get('age')

    dict = {

        'name' : name,
        'age' : age,
        'gfname' : gfname
    }
    response = render(request, 'testApp/results.html', context=dict)

    return response


