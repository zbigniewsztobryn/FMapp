from rest_framework import serializers
from .models import Contacts, Data, Properties

class ContactsSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contacts
        fields = (
            'cont_fname',
            'cont_lname',
            'cont_company',
            'cont_phone'
        )

class DataSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Data
        fields = (
            'name',
            'category',
            'value',
            'initials'

        )


class PropertiesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Properties
        fields = (
            'guid',
            'related_zone_id',
            'related_doc',
            'elem_id',
            'serial_number',
            'producer',
            'name',
            'quantity',
            'production_date',
            'warranty_date',
            'price',
            'website',
        )
