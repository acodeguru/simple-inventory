from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase
from rest_framework import status
from supplier.models import Supplier
from .models import Inventory


class InventoryTest(APITestCase):

    inventory = None 
    
    def setUp(self):
            supplier = Supplier.objects.create(name='Supplier 1')
                
            self.inventory = Inventory.objects.create(
                name='Test 1', description="Description Test 1", note='Note Test 1', stock=10, availability=True, supplier=supplier, 
            )
            Inventory.objects.create(
                name='Test 2', description="Description Test 2", note='Note Test 2', stock=40, availability=True, supplier=supplier, 
            )

    def test_page_inventories(self):
        # get API response
        response = self.client.get(reverse('inventory-page-list'))
        # get data from db
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        
    def test_page_inventory_details(self):
        response = self.client.get(reverse('inventory-page-detail', kwargs={'pk': self.inventory.id}))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
               
    def test_api_inventories(self):
        response = self.client.get(reverse('inventory-api-list'), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        
