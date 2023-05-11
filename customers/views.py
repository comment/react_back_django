from customers.models import Customer
from django.http import JsonResponse
from customers.serializers import CustomerSerializer


def customer(request):
    data = Customer.objects.all()
    serializer = CustomerSerializer(data, many=True)
    return JsonResponse({'customers': serializer.data})
