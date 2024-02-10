from rest_framework import serializers
from users.models import User
from rest_framework_simplejwt.tokens import RefreshToken


class RegisterSerializer (serializers.ModelSerializer) : 
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('full_name','email','picture','password')
    
    def validate(self, attrs):
        email = attrs['email']

        if User.objects.filter(email=email).exists() : 
            raise serializers.ValidationError({
                'message' : "this email already exists"
            })
            

        return attrs
        
    def save(self, **kwargs):
        data = self.validated_data
        user = User.objects.create_user(**data)

        user.save()

        get_token = RefreshToken.for_user(user)

        tokens = {
            'refresh' : str(get_token),
            'access' : str(get_token.access_token),
        }

        return tokens

class LoginSerializer (serializers.Serializer) : 
    email = serializers.EmailField()
    password = serializers.CharField()

    tokens = None

    def validate(self, attrs):
        email = attrs['email']
        password = attrs['password']

        try : 
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({
                'message' : "invalid email"
            })
        
        if not user.check_password(password) : 
            raise serializers.ValidationError({
                'message' : "invalid password"
            })
        
        get_token = RefreshToken.for_user(user)

        self.tokens = {
            'refresh' : str(get_token),
            'access' : str(get_token.access_token),
        }
        return attrs