from rest_framework.views import APIView
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User
from rest_framework import status
import jwt, datetime
from jwt import decode, InvalidTokenError
import os



class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"status": "success","message":"User created successfully!"})
    
    def create(self,validated_data):
        password = validated_data.pop('password', None)

        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance



class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')

        if not email:
            raise AuthenticationFailed('Please provide an email.')

        if not password:
            raise AuthenticationFailed('Please provide a password.')

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('Incorrect email or password!')
        
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect email or password!!')
        
        payload = {
            'id': user.id,
            'email':user.email,
            'username':user.name,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, os.getenv('SECRET'), algorithm='HS256')

        response = Response({'status': 'success', 'message': 'Authentication performed successfully!', 'x-access-token': token})
        
        return response       
    
    


class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('token')
        response.data = {
            'message':'success!'
        }

        return response
    

class VerifyView(APIView):
    def get(self, request):
        token = request.COOKIES.get('token')
        if not token:
            return Response({'status': 'error', 'message': 'No token provided!'}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            payload = decode(token, os.getenv('SECRET'), algorithms=['HS256'])
            user_id = payload['id']

            return Response({'status': 'success', 'user_id': user_id}, status=status.HTTP_200_OK)
        except InvalidTokenError as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'status': 'error', 'message': 'An unexpected error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
       
class ProfileView(APIView):
    def get(self, request, id):
        token = request.COOKIES.get('token')
        if not token:
            return Response({'status': 'error', 'message': 'No token provided!'}, status=status.HTTP_401_UNAUTHORIZED)
        try:
            payload = decode(token, os.getenv('SECRET'), algorithms=['HS256'])   
            userid = payload ['id']


        except InvalidTokenError as e:
            return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'status': 'error', 'message': 'An unexpected error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                
        try:
            id = int(id)
        except ValueError:
            return Response({'error': 'Invalid ID provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        # if userid != id: #para mitigar, só passar o if abaixo.

        #     return Response({'status': 'error', 'message': 'Unauthorized'}, status=status.HTTP_401_UNAUTHORIZED)
      
        user = User.objects.filter(id=id).first()
        if not user:
            return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

        user_data = {
            'id': user.id,
            'username': user.name,
            'email': user.email,
            'document':user.document,
            'birthOfDate':user.birth,
            'plan':user.plan,
            
        }

        return Response(user_data, status=status.HTTP_200_OK)
    
