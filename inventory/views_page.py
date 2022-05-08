from django.shortcuts import render
from .models import Inventory

"""
Inventory Render Pages
"""

"""
Display all the inventories in the data base.
"""
def inventoryList(request):
    inventories = Inventory.objects.all()
    
    for k,vals in request.GET.lists():
        for v in vals:
            inventories = inventories.filter(**{"%s__icontains" % k: v})
            
    return render(request, 'inventory/view_list.html', {'inventories': inventories, 'page_title': "Inventory List"})

"""
Display Detailed view of single inventory using pk or name.
"""
def inventoryDetail(request, pk):

    inventory_name = request.GET.get('name', None)
    inventory = None
    try :
        if inventory_name is not None:
            inventory = Inventory.objects.get(name__iexact=inventory_name)
        else :
            inventory = Inventory.objects.get(id=pk)
            
    except Inventory.DoesNotExist:
        inventory = None
        
    return render(request, 'inventory/view_details.html', {'inventory': inventory})
