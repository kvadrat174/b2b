from rest_framework.response import Response
from rest_framework.views import APIView
from b2bservice import settings


from .serializers import CompanySerializer, ProductSerializer, OrderItemSerializer, OrderSerializer
from .models import Company, Product, OrderItem, Order

class B2bView(APIView):


    def get(self, request):
        company = Company.objects.all()
        product = Product.objects.all()
        order = Order.objects.all()
        orderitem = OrderItem.objects.all()

        serializer = CompanySerializer(company, many=True)
        serializer1 = ProductSerializer(product, many=True)
        serializer2 = OrderSerializer(order, many=True)
        serializer3 = OrderItemSerializer(orderitem, many= True)


        return Response({"Company": serializer.data,
                         "Product": serializer1.data,
                         "Order": serializer2.data,
                         "Order Item": serializer3.data})

class CompanyView(APIView):

    def post(self, request):
        company = request.data.get('company')

        serializer = CompanySerializer(data=company)
        if serializer.is_valid(raise_exception=True):
            company_saved = serializer.save()
        return Response({"success": "Company '{}' created successfully".format(company_saved.company_name)})

class ProductView(APIView):

    def post(self, request):
        product = request.data.get('Product')

        serializer1 = ProductSerializer(data=product)
        if serializer.is_valid(raise_exception=True):
            product_saved = serializer.save()
        return Response({"success": "Product '{}' created successfully".format(product_saved.product_name)})

class OrderView(APIView):
    def post(self, request):
        order = request.data.get('Order')

        serializer = ProductSerializer(data=order)
        if serializer.is_valid(raise_exception=True):
            order_saved = serializer.save()
        return Response({"success": "Order {} created successfully".format(order_saved)})

class OrderItemView(APIView):
    def post(self, request):
        orderitem = request.data.get('OrderItem')

        serializer = ProductSerializer(data=orderitem)
        if serializer.is_valid(raise_exception=True):
            orderitem_saved = serializer.save()
        return Response({"success": "OrderItem '{}' created successfully".format(orderitem_saved)})

    """def post(self, request):
        users = request.data.get('Users')

        # Create an article from the above data
        serializer = UsersSerializer(data=users)

        if serializer.is_valid(raise_exception=True):
            Users_saved = serializer.save()

        return Response({"success": "Users '{}' created successfully".format(Users_saved.login)})"""