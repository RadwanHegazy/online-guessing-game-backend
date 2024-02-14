from rest_framework import serializers
from ..models import Battle, Help 
from django.core.cache import cache

class HelpTextSerializer (serializers.ModelSerializer) : 
    class Meta :
        model = Help
        fields = "__all__"

class BattleSerializer (serializers.ModelSerializer) : 
    help_text = HelpTextSerializer(many=True)
    word = serializers.CharField(write_only=True)
    class Meta : 
        model = Battle
        fields = "__all__"

    def validate(self, attrs):
        word = str(attrs['word']).split(' ')

        if len(word) > 1 :
            raise serializers.ValidationError({
                'message' : "please enter a valid word"
            },code=400)

        return attrs

    def save(self, **kwargs):
        help_text_list = self.validated_data['help_text']
        
        battle = Battle.objects.create(
            created_by = self.validated_data['created_by'],
            word = self.validated_data['word'],
        )

        for i in help_text_list : 
            help_text_model = Help.objects.create(
                text = i['text']
            )

            help_text_model.save()

            battle.help_text.add(help_text_model)
            battle.save()
        
        battle_id = {
            'id' : battle.id
        }

        
        battles = BattleSerializer(Battle.objects.all(),many=True)
        cache.set('battles',battles.data,3600)


        return battle_id
    
    def handel_user (self, user) :
        
        if user is not None :
            return {
                'id' : user.id,
                'full_name' : user.full_name,
                'picture' : user.picture.url,
            }
    
    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['word_len'] = len(str(instance.word))

        data['vs'] = self.handel_user(instance.vs)
        data['created_by'] = self.handel_user(instance.created_by)
        

        return data