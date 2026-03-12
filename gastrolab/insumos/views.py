from django.shortcuts import render, redirect
from insumos.forms import InsumoForm
from insumos.models import Insumo
# Create your views here.
def insumo_view(request):
    insumos = Insumo.objects.all().order_by('-data_criacao')
    print(insumos)
    # search = request.GET.get('search')
    
    # if search:
    #     insumos = insumos.filter(model__icontains=search)
        
    return render(
        request,
        'insumos/insumos.html',
        {'insumos':insumos}
    )

def new_insumo_view(request):
    if request.method == 'POST':
        new_insumo_form = InsumoForm(request.POST)
        if new_insumo_form.is_valid():
            new_insumo_form.save()
            return redirect('listar_insumos')
    else:
        new_insumo_form = InsumoForm()
    return render(request, 'insumos/cadastro_insumos.html', {'new_insumo_form':new_insumo_form})