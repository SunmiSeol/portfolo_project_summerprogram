from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from program.models import Program
from program.serializers import ProgramSerializer
from rest_framework.decorators import api_view

# Create your views here.
# def index(request):
#     return render(request, "tutorials/index.html")


def index(request):
    print("------------------------- Summer Programs for Kids in NYC")
    queryset = Program.objects.all()
    return render(request, "programs/index.html", {'programs': queryset})


class index(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'programs/index.html'

    def get(self, request):
        queryset = Program.objects.all()
        return Response({'programs': queryset})


class list_all_programs(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'programs/program_list.html'

    def get(self, request):
        queryset = Program.objects.all()
        return Response({'programs': queryset})



@api_view(['GET', 'POST', 'DELETE'])
def program_list(request):
    if request.method == 'GET':
        summerprograms = Program.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            summerprograms = summerprograms.filter(title__icontains=title)

        programs_serializer = ProgramSerializer(summerprograms, many=True)
        return JsonResponse(programs_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        programs_data = JSONParser().parse(request)
        programs_serializer = ProgramSerializer(data=programs_data)
        if programs_serializer.is_valid():
            programs_serializer.save()
            return JsonResponse(programs_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(programs_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Program.objects.all().delete()
        return JsonResponse(
            {
                'message':
                '{} Programs were deleted successfully!'.format(count[0])
            },
            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'PUT', 'DELETE'])
def program_detail(request, pk):
    try:
        summerprograms = Program.objects.get(pk=pk)
    except Program.DoesNotExist:
        return JsonResponse({'message': 'The program does not exist'},
                            status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        programs_serializer = ProgramSerializer(summerprograms)
        return JsonResponse(programs_serializer.data)

    elif request.method == 'PUT':
        program_data = JSONParser().parse(request)
        programs_serializer = ProgramSerializer(summerprograms, data=program_data)
        if programs_serializer.is_valid():
            programs_serializer.save()
            return JsonResponse(programs_serializer.data)
        return JsonResponse(programs_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        summerprograms.delete()
        return JsonResponse({'message': 'Program was deleted successfully!'},
                            status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def registration_open_list(request):
    summerprograms = Program.objects.filter(registration_open=True)

    if request.method == 'GET':
        programs_serializer = ProgramSerializer(summerprograms, many=True)
        return JsonResponse(programs_serializer.data, safe=False)