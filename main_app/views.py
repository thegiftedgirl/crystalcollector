from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Crystal, Energy
from .forms import CleansingForm


        
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def crystals_index(request):
    crystals = Crystal.objects.all()
    return render(request, 'crystals/index.html', {'crystals': crystals })

def crystals_detail(request, crystal_id):
    crystal = Crystal.objects.get(id=crystal_id)
    cleansing_form = CleansingForm()

    energys_crystal_doesnt_have = Energy.objects.exclude(id__in = crystal.energys.all().values_list('id'))
    
    return render(request, 'crystals/detail.html', {
        'crystal': crystal, 
        'cleansing_form': cleansing_form,
        'energys': energys_crystal_doesnt_have
        }
    )
def add_cleansing(request, crystal_id):
    form = CleansingForm(request.POST)
    if form.is_valid():
        new_cleansing = form.save(commit=False)
        new_cleansing.crystal_id = crystal_id
        new_cleansing.save()
    return redirect('detail', crystal_id=crystal_id)

def assoc_energy(request, crystal_id, energy_id):
    Crystal.objects.get(id=crystal_id).energys.add(energy_id)
    return redirect('detail', crystal_id= crystal_id)

class CrystalCreate(CreateView):
    model = Crystal
    fields = '__all__'
   
class CrystalUpdate(UpdateView):
    model = Crystal 
    fields = ['description', 'properties', 'color']  

class CrystalDelete(DeleteView):
    model = Crystal
    success_url = '/crystals/'

class EnergyList(ListView):
    model = Energy

class EnergyDetail(DetailView):
    model = Energy

class EnergyCreate(CreateView):
    model = Energy
    fields = "__all__"
    success_url = '/energys/'

class EnergyUpdate(UpdateView):
    model = Energy
    fields = "__all__"
    success_url = '/energys/'

class EnergyDelete(DeleteView):
    model = Energy
    success_url = '/energys/'