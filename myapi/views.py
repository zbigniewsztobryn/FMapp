from django.shortcuts import render
from rest_framework import viewsets
from django.views.generic import View, ListView
from django.db.models import CharField, Value as V
from django.db.models.functions import Concat
from .serializers import HeroSerializer
from .models import Hero, Data, SaveFile, Contacts, Tags
from django.contrib import messages
from django.http import HttpResponse
import boto
import re
import os
from datetime import datetime
from django.conf import settings
from boto.s3.connection import OrdinaryCallingFormat
import mimetypes

from django.db.models import Q

class HeroViewSet (viewsets.ModelViewSet):
    queryset = Hero.objects.all().order_by('name')
    serializer_class = HeroSerializer

def home(request):
    return render (request, 'index.html', {'var': 'content'})







    # from boto.s3.connection import S3Connection
    # conn = S3Connection('<aws access key>', '<aws secret key>')
    # bucket = conn.get_bucket('mybucket')
    # key = bucket.get_key('mykey', validate=False)
    # url = key.generate_url(86400)


    # fname = request.GET['filename']
    # bucket_name = 'fmapplication'
    # key = s.get_bucket(bucket_name).get_key(fname)
    # key.get_contents_to_filename('static/files' + key.name)
    # wrapper = FileWrapper(open('static/files' + fname, 'rb'))
    # content_type = mimetypes.guess_type('/tmp/' + fname)[0]
    # response = HttpResponse(wrapper, content_type=content_type)
    # response['Content-Length'] = os.path.getsize('static/files' + fname)
    # response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(fname)


class SearchView(View):
    data_model = Data
    contacts_model = Contacts
    save_file_model = SaveFile
    categories_model = Tags
    template_name = 'index.html'
    context_object_name = 'all_search_results'

    # def handles3downloads(self, request):
    #     import boto
    #     conn = boto.connect_s3('AKIAR43Z6RQRISNTYBNQ', 'eWp0iJ6wJGvmtfGu0JEVihmg+NIkI6soHHAX24nR', host='eu-west-2')
    #     bucket = conn.get_bucket('fmapplication')
    #     s3_file_path = bucket.get_key('static/files/dummy_drawing_comment.pdf')
    #     url = s3_file_path.generate_url(60, 'GET', response_headers=response_headers,
    #                                     force_http=True)  # expiry time is in seconds
    #     file_response = requests.get(url)
    #     return render(request, 'index.html', locals())


    # def download(self, request):
    #
    #     import boto
    #     conn = boto.connect_s3('AKIAR43Z6RQRISNTYBNQ', 'eWp0iJ6wJGvmtfGu0JEVihmg+NIkI6soHHAX24nR')
    #     bucket = conn.get_bucket('fmapplication')
    #     s3_file_path = bucket.get_key('static/files')
    #     url = s3_file_path.generate_url(expires_in=600)  # expiry time is in seconds
    #
    #     return HttpResponseRedirect(url)

    def get(self, request):
        data_model = Data
        save_file_model = SaveFile
        files_data = self.save_file_model.objects.all()
        files_meta = self.data_model.objects.all()
        files_contacts = self.contacts_model.objects.all()
        files_tags = self.categories_model.objects.all()
        query = self.request.GET.get('search')

        if query:
            postresult = save_file_model.objects.filter(Q(file__icontains=query) |
                                                        Q(data__name__icontains=query) |
                                                        Q(data__category__icontains=query) |
                                                        Q(data__value__icontains=query) |
                                                        Q(data__contact__cont_fname__icontains=query) |
                                                        Q(data__contact__cont_lname__icontains=query) |
                                                        Q(data__contact__cont_company__icontains=query))
            result = postresult
        else:
            result = self.save_file_model.objects.all()
        return render(request, 'index.html', locals())

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
        return render(request, 'data.html', locals())

    def post(self, request):

        # handle files save and load
        get_file = request.FILES['file']
        get_title = request.POST.get('title')
        get_contact = request.POST.get('contact_in')
        get_category = request.POST.get('categories_in')
        get_date = request.POST.get('date_in')

        get_date_format = (datetime.strptime(get_date, '%Y-%m-%d').strftime('%y%m%d'))

        full_contact = self.contacts_model.objects.filter(id=get_contact)
        full_contact_list = []
        for i in full_contact:
            full_contact_list.append(str(i.cont_company))
        get_company = (full_contact_list[0])[0:3].upper()


        full_category = self.categories_model.objects.filter(id=get_category)
        full_category_list = []
        for i in full_category:
            full_category_list.append(str(i.categories))
        get_category_alias = (full_category_list[0])[0:3].upper()


        getalias = (get_date_format + '-' +
                    get_category_alias + '-' + \
                    get_company + '-' + \
                    str(get_file))


        data = self.data_model(name=get_title, initials =getalias , tag_id=get_category, value = get_date, contact_id = get_contact)
        data.save()

        # upload single image
        if get_file is not False:
            # save file
            file_object = self.save_file_model(data=data, file=get_file)
            file_object.save()

        messages.success(request, 'File has beed added')

        return render(request, 'data.html', locals())




# test it through!
# class AWSDownload(object):
#     access_key = None
#     secret_key = None
#     bucket = None
#     region = None
#     expires = getattr(settings, 'AWS_DOWNLOAD_EXPIRE', 5000)
#
#     def __init__(self,  access_key, secret_key, bucket, region, *args, **kwargs):
#         self.bucket = bucket
#         self.access_key = access_key
#         self.secret_key = secret_key
#         self.region = region
#         super(AWSDownload, self).__init__(*args, **kwargs)
#
#     def s3connect(self):
#         conn = boto.s3.connect_to_region(
#                 self.region,
#                 aws_access_key_id=self.access_key,
#                 aws_secret_access_key=self.secret_key,
#                 is_secure=True,
#                 calling_format=OrdinaryCallingFormat()
#             )
#         return conn
#
#     def get_bucket(self):
#         conn = self.s3connect()
#         bucket_name = self.bucket
#         bucket = conn.get_bucket(bucket_name)
#         return bucket
#
#     def get_key(self, path):
#         bucket = self.get_bucket()
#         key = bucket.get_key(path)
#         return key
#
#     def get_filename(self, path, new_filename=None):
#         current_filename =  os.path.basename(path)
#         if new_filename is not None:
#             filename, file_extension = os.path.splitext(current_filename)
#             escaped_new_filename_base = re.sub(
#                                             '[^A-Za-z0-9\#]+',
#                                             '-',
#                                             new_filename)
#             escaped_filename = escaped_new_filename_base + file_extension
#             return escaped_filename
#         return current_filename
#
#     def generate_url(self, path, download=True, new_filename=None):
#         file_url = None
#         aws_obj_key = self.get_key(path)
#         if aws_obj_key:
#             headers = None
#             if download:
#                 filename = self.get_filename(path, new_filename=new_filename)
#                 headers = {
#                     'response-content-type': 'application/force-download',
#                     'response-content-disposition':'attachment;filename="%s"'%filename
#                 }
#             file_url = aws_obj_key .generate_url(
#                                 response_headers=headers,
#                                  expires_in=self.expires,
#                                 method='GET')
#         return file_url
#
# bucket = AWS_STORAGE_BUCKET_NAME
# region = S3DIRECT_REGION
# access_key = AWS_ACCESS_KEY_ID
# secret_key = AWS_SECRET_ACCESS_KEY
# path = 'path/to/object/to/download/in/your/bucket/somefile.jpg'
#
# aws_dl_object =  AWSDownload(access_key, secret_key, bucket, region)
# file_url = aws_dl_object.generate_url(path, new_filename='New awesome file')