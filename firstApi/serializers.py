from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    department = serializers.CharField(max_length=100)
    email =serializers.EmailField(max_length=30)


    def create(self, validated_data):
      return Contact.objects.create(validated_data)  



    def update(self, instance, validated_data):
      
        instance.name = validated_data.get('name', instance.name)
        instance.department= validated_data.get('department', instance.department)
        instance.email = validated_data.get('email', instance.email)
       
        instance.save()
        return instance           
        