from rest_framework import serializers 
from django.apps import apps
 
class FundraiserSerializer(serializers.ModelSerializer):
   owner = serializers.ReadOnlyField(source='owner.id') #Users can see who the owner is, but they cannot change the owner through the API
   class Meta:
       model = apps.get_model('fundraisers.Fundraiser') 

class PledgeSerializer(serializers.ModelSerializer):
   class Meta:
       model = apps.get_model('fundraisers.Pledge') 
       fields = '__all__'

class FundraiserDetailSerializer(FundraiserSerializer):
    pledges = PledgeSerializer(many=True, read_only=True) #read-only here means users can only read the pledges not editing them to prevent cases of an owner writing other owners pledges

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.goal = validated_data.get('goal', instance.goal)
        instance.image = validated_data.get('image', instance.image)
        instance.is_open = validated_data.get('is_open', instance.is_open)
        instance.date_created = validated_data.get('date_created', instance.date_created)
        instance.owner = validated_data.get('owner', instance.owner)
        instance.save()
        return instance
    
    #Adding a custom update () so user can update comment and anonymous fields, but MUST edit permission later to only the supporter can make changes in view.py
    def update(self, instance, validated_data):
        instance.comment = validated_data.get('comment', instance.comment)
        instance.anonymous = validated_data.get('anonymous', instance.anonymous)
        instance.save()
        return instance