from django.contrib.auth.models import User, Group
from rest_framework import serializers

#CAMPOS QUE DESEO MOSTRAR EN MI API
class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','username','email','groups','password','is_staff','is_active')

    

class GroupSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name')