from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Catalog
from .serializers import CatalogSerializer


class CatalogListApiView(APIView):
    # user authentication verify
    permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, *args, **kwargs):
        catalogs = Catalog.objects.all()
        serializer = CatalogSerializer(catalogs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create
    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
        }
        serializer = CatalogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CatalogDetailApiView(APIView):
    # user authentication verify
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, catalog_id):
        try:
            return Catalog.objects.get(id=catalog_id)
        except Catalog.DoesNotExist:
            return None

    # 3. Retrieve
    def get(self, request, catalog_id, *args, **kwargs):
        catalog_instance = self.get_object(catalog_id)
        if not catalog_instance:
            return Response(
                {"res": "Object with catalog id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CatalogSerializer(catalog_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 4. Update
    def put(self, request, catalog_id, *args, **kwargs):
        catalog_instance = self.get_object(catalog_id)
        if not catalog_instance:
            return Response(
                {"res": "Object with catalog id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'name': request.data.get('name'),
        }
        serializer = CatalogSerializer(instance = catalog_instance, data=data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # 5. Delete
    def delete(self, request, catalog_id, *args, **kwargs):
        catalog_instance = self.get_object(catalog_id)
        if not catalog_instance:
            return Response(
                {"res": "Object with catalog id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        catalog_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )