from django.shortcuts import render, redirect, get_object_or_404
from django.forms import ModelForm
from products.models import Articulo

class ProductForm(ModelForm):
    class Meta:
        model = Articulo
        fields = ['nombre_item', 'tipo_item', 'precio', 'cantidad']


def products_index(request):
    search_query = request.GET.get('search_box', None)
    if search_query is None or search_query is '':
        products = Articulo.objects.all()     
    else:
        products = Articulo.objects.filter(nombre_item__iexact=search_query)

    context = {
        'products': products
    }
    return render(request, 'products_index.html', context)

def products_create(request, template_name='product_form.html'):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, template_name, {'form':form})

def products_update(request, pk, template_name='product_form.html'):
    product= get_object_or_404(Articulo, pk=pk)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, template_name, {'form':form})

def products_delete(request, pk, template_name='confirm_delete.html'):
    products= get_object_or_404(Articulo, pk=pk)    
    if request.method=='POST':
        products.delete()
        return redirect('/deleted')
    return render(request, template_name, {'object':Articulo})

def deleted(request,template_name='deleted.html'):
    return render(request, template_name)
