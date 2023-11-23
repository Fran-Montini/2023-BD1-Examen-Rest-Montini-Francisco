
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from .models import Customers, Suppliers, Categories, Orders, Orderdetails, Employees
from .models import Customers
from .models import Products
from django.db.models import F, Sum

class SerializadorPadre(ModelSerializer):
    class Meta:
        fields = '__all__'

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customers
        fields = '__all__'


class SupplierSerializer(SerializadorPadre):
    class Meta:
        model = Suppliers
        fields = '__all__'

class CategorieSerializer (SerializadorPadre):
   class Meta:
      model = Categories
      fields = '__all__'

class ProductSerializer (SerializadorPadre):
   class Meta:
      model = Products
      fields = '__all__'

class OrderdetailSerializer (SerializadorPadre):
   class Meta:
      model = Orderdetails
      fields = '__all__'

class OrderSerializer(SerializadorPadre):
   order_details = OrderdetailSerializer(many=True, read_only=True)

   class Meta:
      model = Orders
      fields = '__all__'

class EmployeeSerializer (SerializadorPadre):
   class Meta:
      model = Employees
      fields = '__all__'

#class ProductService:
#    def get_products_by_supplier_category_stock(self, supplier_id, category_id, stock_min):
#        try:
#            products = Products.objects.filter(
#                SupplierID=supplier_id,
#                CategoryID=category_id,
#                Discontinued='0'
#            ).annotate(
#                stockFuturo=Sum(F('UnitsInStock') + F('UnitsOnOrder'))
#            ).filter(stockFuturo__lt=stock_min).order_by('stockFuturo')
#            return products
#          except Products.DoesNotExist:
#            return None
#class Punto1Serializer(serializers.Serializer):
#    id = serializers.IntegerField()
#    apellido = serializers.CharField(max_length=50)
#    descripcion = CondicionIvaSerializer(many=False)
#    telefono = serializers.IntegerField()
#    nuevoTelefono = serializers.IntegerField()