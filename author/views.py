from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Author
from .serializers import AuthorSerializer


class AuthorListApiView(APIView):
    # user authentication verify
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, *args, **kwargs):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
        }
        serializer = AuthorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetailApiView(APIView):
    # user authentication verify
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, author_id):
        try:
            return Author.objects.get(id=author_id)
        except Author.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, author_id, *args, **kwargs):
        author_instance = self.get_object(author_id)
        if not author_instance:
            return Response(
                {"res": "Object with author id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = AuthorSerializer(author_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, author_id, *args, **kwargs):
        author_instance = self.get_object(author_id)
        if not author_instance:
            return Response(
                {"res": "Object with author id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
        }
        serializer = AuthorSerializer(instance = author_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, author_id, *args, **kwargs):
        author_instance = self.get_object(author_id)
        if not author_instance:
            return Response(
                {"res": "Object with author id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        author_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )