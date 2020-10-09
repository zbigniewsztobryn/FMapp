from django.shortcuts import render
from rest_framework import viewsets
from django.views.generic import View

from .serializers import HeroSerializer
from .models import Hero, Data, SaveFile
from django.contrib import messages


class HeroViewSet (viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class AddFileView(View):
    data_model = Data
    save_file_model = SaveFile

    def get(self, request):

        files_data = self.save_file_model.objects.all()
        files_meta = self.data_model.objects.all()

        return render(request, 'data.html', locals())

    def post(self, request):

        # handle files save and load
        get_file = request.FILES['file']
        get_title = request.POST.get('title')

        data = self.data_model(name=get_file, category='finance')
        data.save()

        # upload single image
        if get_file is not False:
            # save file
            file_object = self.save_file_model(data=data, file=get_file)
            file_object.save()

        messages.success(request, 'File has beed added')

        return render(request, 'data.html', locals())



# Create your views here.
