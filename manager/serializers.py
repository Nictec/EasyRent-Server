from rest_framework import serializers
from django.contrib.auth.models import User, Group
from django.db.models import Q
from .models import *






class ShelfSerializer(serializers.ModelSerializer):
	class Meta:
		model = Shelf
		fields = ('__all__')

class EquipmentSerializer(serializers.ModelSerializer):
	avail_quantity = serializers.SerializerMethodField()
	class Meta:
		model = Equipment
		fields = '__all__'

	def get_avail_quantity(self, obj):
		assigned_sum = 0
		assignments = Assignment.objects.filter(~Q(order__status = 'F'), equipment=obj.id)
		for assignment in assignments:
			assigned_sum += assignment.quantity
		return obj.max_quantity - assigned_sum

class AssignmentSerializer(serializers.ModelSerializer):
	equipment_data = EquipmentSerializer(read_only=True, source="equipment")
	class Meta:
		model = Assignment
		fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
	assignment = AssignmentSerializer(many=True, read_only=True)
	class Meta:
		model = Order
		#fields = '__all__'
		exclude = ('assignments',)

class CalendarSerializer(serializers.ModelSerializer):
	title = serializers.CharField(source='name')
	start = serializers.DateField(source='dateStart')
	end = serializers.DateField(source='dateEnd')
	url = serializers.SerializerMethodField()
	class Meta:
		model = Order
		fields = ('title', 'start', 'end', 'url')
	def get_url(self, obj):
		order = obj.id
		host = 'localhost:8080/#/details/'
		return '#' + '/' + 'details' + '/' + str(order) + '/'

class ClientSerializer(serializers.ModelSerializer):
	class Meta:
		model = Client
		fields = '__all__'

class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ('id', 'url', 'username', 'email', 'groups', 'password', 'is_superuser')
    def create(self, validated_data):
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.is_staff=validated_data['is_superuser']
        user.save()
        return user



class GroupSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Group
		fields = ('url', 'name')
