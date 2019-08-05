from rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from mackta_api.models import User # ProfileFeedItem

class CustomRegisterSerializer(RegisterSerializer):
    # id = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta: 
        model = User
        fields = ('id', 'email', 'first_name','last_name', 'password')
        # extra_kwargs = {
        #     'password': {
        #         'write_only' : True,
        #         'style' : {'input_type': 'password1'}
        #     }
        # }
    
    
    email = serializers.EmailField(required=True)
    first_name = serializers.CharField(required=True)
    last_name = serializers.CharField(required=True)
    password1 = serializers.CharField(write_only=True)


    def get_cleaned_data(self):
        super(CustomRegisterSerializer, self).get_cleaned_data()

        return{
            'id' : self.validated_data.get('id', ''),
            'email' : self.validated_data.get('email', ''),
            'first_name' : self.validated_data.get('first_name', ''),
            'last_name' : self.validated_data.get('last_name', ''),
            'password1' : self.validated_data.get('password1', ''),
        }
 

# class CustomUserDetailsSerializer(serializers.ModelSerializer):

#         class Meta:
#             model = User
#             fields = ('email','first_name', 'last_name')
#             read_only_fields = ('email',)

# class ProfileFeedItemSerializer(serializers.ModelSerializer):
#     """Serializes profile feed items"""

#     class Meta:
#         model = ProfileFeedItem
#         fields = ('id', 'user_profile', 'status_text', 'created_on')
#         extra_kwargs = {'user_profile' : {'read_only' : True}}