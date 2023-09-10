from rest_framework.response import Response
from rest_framework.views import APIView


class HelloApiView(APIView):
    """Test API View"""

    def get(self, request, *args, **kwargs):
        """Returns a list of APIView features
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        an_apiview = [
            'Uses HTTP methods as function (get, post, patch, put, delete)',
            'Is similar to a traditional Django View',
            'Gives you the most control over your application logic',
            'Is mapped manually to URLs',
        ]
        return Response({'message': 'Hello!', 'an_apiview': an_apiview})
