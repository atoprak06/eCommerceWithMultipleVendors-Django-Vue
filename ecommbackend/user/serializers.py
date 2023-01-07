from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer
from djoser.serializers import UserCreatePasswordRetypeSerializer
from .models import UserProfile

class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        model = UserProfile
        fields = ('username','email','first_name','last_name','user_age','user_country','user_city','user_address','is_vendor',)

class UserRePasswordSerializer(UserCreatePasswordRetypeSerializer):
    class Meta(UserCreatePasswordRetypeSerializer.Meta):        
        fields = ('username','email','first_name','last_name','user_age','user_country','user_city','user_address','is_vendor','password',)