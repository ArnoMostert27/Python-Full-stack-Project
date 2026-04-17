from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import VehicleForm
from .models import Vehicle

@login_required
def list_vehicles(request):
    vehicles = Vehicle.objects.filter(owner=request.user)
    return render(request, 'vehicles/list.html', {'vehicles': vehicles})

@login_required
def create_vehicle(request):
    form = VehicleForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        vehicle = form.save(commit=False)
        vehicle.owner = request.user
        vehicle.save()
        return redirect('vehicles')
    return render(request, 'vehicles/form.html', {'form': form, 'action': 'Create'})

@login_required
def edit_vehicle(request, id):
    vehicle = get_object_or_404(Vehicle, id=id)
    form = VehicleForm(request.POST or None, request.FILES or None, instance=vehicle)
    if form.is_valid():
        form.save()
        return redirect('vehicles')
    return render(request, 'vehicles/form.html', {'form': form, 'action': 'Edit'})

@login_required
def delete_vehicle(request, id):
    vehicle = get_object_or_404(Vehicle, id=id)
    if request.method == "POST":
        vehicle.delete()
        return redirect('vehicles')
    return render(request, 'vehicles/delete.html', {'vehicle': vehicle})