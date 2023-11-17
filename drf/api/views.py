from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import PersonSerializer
from .models import Person


@api_view(['GET'])
def api_urls(request):
    api_urls ={
        'list':'',
         'retrieve':'retrieve/<str:pk>/',
         'create':'create/',
         'update':'update/<str:pk>/',
         'delete':'delete/<str:pk>/',
         'Information':'This django Rest Framework API I created it so as to demonstrate CRUD List Application\n The DRF has a model of a person ',
    }

    return Response(api_urls)

@api_view(['GET'])
def listing(request):
    list =Person.objects.all()
    serializer =PersonSerializer(list, many=True)

    return Response(serializer.data)

@api_view(['GET'])
def Details(request, pk):
    list =Person.objects.get(id=pk)
    serializer=PersonSerializer(list, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def create(request):
    serializer =PersonSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
@api_view(['POST'])
def update(request, pk):
    list =Person.objects.get(id=pk)
    serializer =PersonSerializer(instance=list, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    
@api_view(['DELETE'])
def delete(request, pk):
    list =Person.objects.get(id=pk)
    list.delete()
    return Response('The Object Was deleted Successfully')

















    



