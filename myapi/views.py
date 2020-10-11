from django.shortcuts import render
from rest_framework import viewsets
from django.views.generic import View, ListView
from django.db.models import CharField, Value as V
from django.db.models.functions import Concat
from .serializers import HeroSerializer
from .models import Hero, Data, SaveFile, Contacts, Tags
from django.contrib import messages
import mimetypes

class HeroViewSet (viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

class SearchView(ListView):
    model = Data
    template_name = 'data.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = Data.objects.filter(title__contains=query)
          result = postresult
       else:
           result = None
       return result



class AddFileView(View):
    data_model = Data
    contacts_model = Contacts
    save_file_model = SaveFile
    categories_model = Tags


    def get(self, request):

        files_data = self.save_file_model.objects.all()
        files_meta = self.data_model.objects.all()
        files_contacts = self.contacts_model.objects.all()
        files_tags = self.categories_model.objects.all()

        #allfiles = self.data_model.objects.all()
        return render(request, 'data.html', locals())

    def post(self, request):

        # handle files save and load
        get_file = request.FILES['file']
        get_title = request.POST.get('title')
        get_contact = request.POST.get('contact_in')
        get_category = request.POST.get('categories_in')
        get_date = request.POST.get('date_in')

        data = self.data_model(name=get_title, category=get_category,value = get_date, contact_id = get_contact)
        data.save()

        # upload single image
        if get_file is not False:
            # save file
            file_object = self.save_file_model(data=data, file=get_file)
            file_object.save()

        messages.success(request, 'File has beed added')

        return render(request, 'data.html', locals())



# Create your views here.
