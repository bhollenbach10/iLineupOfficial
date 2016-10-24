from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import *
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import NameForm






# Create your views here.
def index(request):
    try:
        form1 = request.GET['form1']
        form2 = request.GET['form2']
    except:
        form1 = ''
        form2 = ''
    template = loader.get_template('index.html')
    context = {
        'categories': Category.objects.all(), }
    context['form1'] = form1
    context['form2'] = form2
    try:
        context['prod_name'] = request.GET['product_name']
    except:
        context['prod_name'] = ''
    print(context['prod_name'])
    return HttpResponse(template.render(context, request))


def product(request, id=1):
    template = loader.get_template('product.html')
    context = {
        'product': Product.objects.get(id=id)
    }
    return HttpResponse(template.render(context, request))

def product_artist(request):
    if request.method == 'POST':
        form = NameForm(request.post)
        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
        else:
            form = NameForm()
        return render(request, 'name.html' , {'form': form})

