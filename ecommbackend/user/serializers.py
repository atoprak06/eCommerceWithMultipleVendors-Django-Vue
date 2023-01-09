from djoser.serializers import UserCreatePasswordRetypeSerializer
from djoser.serializers import UserSerializer
from .models import UserProfile

class UserRegistrationSerializer(UserCreatePasswordRetypeSerializer):
    class Meta:
        model = UserProfile
        fields = ('username','email','first_name','last_name','user_age','user_country','user_city','user_address','is_vendor','user_gender','password')

class UserShowSerializer(UserSerializer):
    class Meta:
        model = UserProfile
        fields = ('username','email','first_name','last_name','user_age','user_country','user_city','user_address','is_vendor','user_gender')
