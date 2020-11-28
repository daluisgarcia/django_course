from django.http import HttpResponse
from django.template import loader

# Create your views here.
def index(request):
    num = request.session.get('num_visit', 0) + 1
    request.session['num_visit'] = num
    if num > 4 : del(request.session['num_visit'])
    template = loader.get_template('hello/index.html')
    resp = HttpResponse(template.render({'num': num}, request))
    resp.set_cookie('dj4e_cookie', 'ff2d5fc3', max_age=1000)
    return resp