from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import InventorySerializer
from .models import Inventory

"""
Inventory Overview
"""
@api_view(['GET'])
def InventroyOverview(request):
    api_urls = {
        'List' : '/inventory/',
        'Detail View' : '/inventory/<str:pk>/',
        'Create' : '/inventory-create/',
        'Update' : '/inventory-update/<str:pk>/',
        'Delete' : '/inventory-delete/<str:pk>/',
    }
    return Response(api_urls)


"""
Display all the inventories in the data base.
"""
@api_view(['GET'])
def inventoryList(request):
    inventories = Inventory.objects.all()
    
    for k,vals in request.GET.lists():
        for v in vals:
            inventories = inventories.filter(**{"%s__icontains" % k: v})
                
    serializer = InventorySerializer(inventories, many = True)
    return Response(serializer.data)

"""
Display Detailed view of single inventory using pk or name.
"""
@api_view(['GET'])
def inventoryDetail(request, pk):
    inventory = None
    try :
        inventory = Inventory.objects.get(id=pk)      
            
    except Inventory.DoesNotExist:
        inventory = None
        
    serializer = InventorySerializer(inventory, many = False)
    return Response(serializer.data)

"""
Update single inventory using pk.
"""
@api_view(['PATCH'])
def inventoryUpdate(request, pk):
    inventory = Inventory.objects.get(id = pk)
    serializer = InventorySerializer(instance=inventory, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

"""
Delete single inventory using pk.
"""
@api_view(['DELETE'])
def inventoryDelete(request, pk):
    inventory = Inventory.objects.get(id = pk)
    inventory.delete()
    
    return Response("Inventory ",inventory["name"], "(",inventory["id"] ,") deleted successfully.")

@api_view(['POST'])
def inventoryCreate(request):
    serializer = InventorySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)