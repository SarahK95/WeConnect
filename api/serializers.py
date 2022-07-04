from rest_framework import serializers

from api.models import User, Customer, owner, Facility, Hotel, Rooms, Booking


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username', 'email', 'is_owner']

class CustomerSignupSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
    class Meta:
        model=User
        fields=['username','email','password', 'password2']
        extra_kwargs={
            'password':{'write_only':True}
        }
    
    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        # 'name','contact',
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error":"password do not match"})
        user.set_password(password)
        user.is_customer=True
        user.save()
        Customer.objects.create(user=user)
        return user


class HotelAdminSignupSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(style={"input_type":"password"}, write_only=True)
    class Meta:
        model=User
        fields=['username','email','password', 'password2'] # 'name',
        extra_kwargs={
            'password':{'write_only':True}
        }
    

    def save(self, **kwargs):
        user=User(
            username=self.validated_data['username'],
            email=self.validated_data['email']
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']
        if password !=password2:
            raise serializers.ValidationError({"error":"password do not match"})
        user.set_password(password)
        user.is_owner=True
        user.save()
        owner.objects.create(user=user)
        return user

# Add Facility
class Facility(serializers.ModelSerializer):
     class Meta:
        model = Facility
        fields = "__all__"

        def create(self, validated_data):
            instance = self.Meta.model(**validated_data)
            instance.save()
            return instance

# Add Rooms
class Rooms(serializers.ModelSerializer):
     class Meta:
        model = Rooms
        fields = "__all__"

        def create(self, validated_data):
            instance = self.Meta.model(**validated_data)
            instance.save()
            return instance
# Add Hotel
class Hotel(serializers.ModelSerializer):
     class Meta:
        model = Hotel
        fields = "__all__"

        def create(self, validated_data):
            instance = self.Meta.model(**validated_data)
            instance.save()
            return instance

# Add Booking
class Booking(serializers.ModelSerializer):
     class Meta:
        model = Booking
        fields = "__all__"

        def create(self, validated_data):
            instance = self.Meta.model(**validated_data)
            instance.save()
            return instance
    