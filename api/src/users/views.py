from rest_framework import generics, status, permissions
from rest_framework.response import Response
from users.serializers import RegisterSerializer, ProfileUserSerializer


class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = (permissions.AllowAny, )

class RetrieveProfileAPIView(generics.RetrieveAPIView):
    serializer_class = ProfileUserSerializer
    #permission_classes = (permissions.IsAuthenticated, )

    def get_object(self):
    	return self.request.user


class WelcomeView(generics.GenericAPIView):
	permission_classes = (permissions.AllowAny, )

	def get(self,request,*args,**kwargs):
		return Response({'hello':'world'})

register = RegisterAPIView.as_view()
hello = WelcomeView.as_view()
profile = RetrieveProfileAPIView.as_view()