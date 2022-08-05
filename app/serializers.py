from dataclasses import fields
from rest_framework import serializers
from .models import Toda
from django.template.defaultfilters import slugify
from .models import TimingTodo

class TodoSerializers(serializers.ModelSerializer):
    slug = serializers.SerializerMethodField()
    class Meta:
        model = Toda
        # fields = '__all__'
        exclude = ['created_at']
    

    def get_slug(self,obj):
        return slugify(obj.todo_title)


class timingtodoserializer(serializers.ModelSerializer):
    todo = TodoSerializers()
    class Meta:
        model = TimingTodo
        exclude = ['created_at','updated_at']
        # depth = 1