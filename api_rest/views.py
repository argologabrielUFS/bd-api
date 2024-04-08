from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Endereco, Loja, Plataforma, Vendedor
from .serializers import EnderecoSerializer, LojaSerializer, PlatSerializer, VendSerializer

import json

#GET GERAL

@api_view(['GET'])
def get_end(request):

    if request.method == 'GET':

        users = Endereco.objects.all()                          # Get all objects in User's database (It returns a queryset)

        serializer = EnderecoSerializer(users, many=True)       # Serialize the object data into json (Has a 'many' parameter cause it's a queryset)

        return Response(serializer.data)                    # Return the serialized data
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_plat(request):

    if request.method == 'GET':

        users = Plataforma.objects.all()                          # Get all objects in User's database (It returns a queryset)

        serializer = PlatSerializer(users, many=True)       # Serialize the object data into json (Has a 'many' parameter cause it's a queryset)

        return Response(serializer.data)                    # Return the serialized data
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_loja(request):

    if request.method == 'GET':

        users = Loja.objects.all()                          # Get all objects in User's database (It returns a queryset)

        serializer = LojaSerializer(users, many=True)       # Serialize the object data into json (Has a 'many' parameter cause it's a queryset)

        return Response(serializer.data)                    # Return the serialized data
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_vend(request):

    if request.method == 'GET':

        users = Vendedor.objects.all()                          # Get all objects in User's database (It returns a queryset)

        serializer = VendSerializer(users, many=True)       # Serialize the object data into json (Has a 'many' parameter cause it's a queryset)

        return Response(serializer.data)                    # Return the serialized data
    
    return Response(status=status.HTTP_400_BAD_REQUEST)

# CRUDZAO DA MASSA
@api_view(['GET','POST','PUT','DELETE'])
def end_manager(request):

# ENDEREÇOS

    if request.method == 'GET':

        try:
            if request.GET['cpf']:                         # Check if there is a get parameter called 'user' (/?user=xxxx&...)

                cpf_numb = request.GET['cpf']         # Find get parameter

                try:
                    user = Endereco.objects.get(pk=cpf_numb)   # Get the object in database
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = EnderecoSerializer(user)           # Serialize the object data into json
                return Response(serializer.data)            # Return the serialized data

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
# POST

    if request.method == 'POST':

        new_end = request.data
        
        serializer = EnderecoSerializer(data=new_end)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(status=status.HTTP_400_BAD_REQUEST)

# PUT

    if request.method == 'PUT':

        cpf_number = request.data['cpf']

        try:
            updated_user = Endereco.objects.get(pk=cpf_number)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = EnderecoSerializer(updated_user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

# DELETE

    if request.method == 'DELETE':

        try:
            user_to_delete = Endereco.objects.get(pk=request.data['cpf'])
            user_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','POST','PUT','DELETE'])
def loja_manager(request):

# LOJAS

    if request.method == 'GET':

        try:
            if request.GET['cnpj']:                         # Check if there is a get parameter called 'user' (/?user=xxxx&...)

                cnpj_numb = request.GET['cnpj']         # Find get parameter

                try:
                    user = Loja.objects.get(pk=cnpj_numb)   # Get the object in database
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = LojaSerializer(user)           # Serialize the object data into json
                return Response(serializer.data)            # Return the serialized data

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
# POST

    if request.method == 'POST':

        new_loja = request.data
        
        serializer = LojaSerializer(data=new_loja)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(status=status.HTTP_400_BAD_REQUEST)

# PUT

    if request.method == 'PUT':

        cnpj_number = request.data['cnpj']

        try:
            updated_user = Loja.objects.get(pk=cnpj_number)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = LojaSerializer(updated_user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

# DELETE

    if request.method == 'DELETE':

        try:
            user_to_delete = Loja.objects.get(pk=request.data['cnpj'])
            user_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['GET','POST','PUT','DELETE'])
def plat_manager(request):

# PLATAFORMAS

    if request.method == 'GET':

        try:
            if request.GET['cnpj']:                         # Check if there is a get parameter called 'user' (/?user=xxxx&...)

                cnpj_numb = request.GET['cnpj']         # Find get parameter

                try:
                    user = Plataforma.objects.get(pk=cnpj_numb)   # Get the object in database
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = PlatSerializer(user)           # Serialize the object data into json
                return Response(serializer.data)            # Return the serialized data

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
# POST

    if request.method == 'POST':

        new_plat = request.data
        
        serializer = PlatSerializer(data=new_plat)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(status=status.HTTP_400_BAD_REQUEST)

# PUT

    if request.method == 'PUT':

        cnpj_number = request.data['cnpj']

        try:
            updated_user = Loja.objects.get(pk=cnpj_number)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = PlatSerializer(updated_user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

# DELETE

    if request.method == 'DELETE':

        try:
            user_to_delete = Plataforma.objects.get(pk=request.data['cnpj'])
            user_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','POST','PUT','DELETE'])
def vend_manager(request):

# VENDEDOR

    if request.method == 'GET':

        try:
            if request.GET['id_vend']:                         # Check if there is a get parameter called 'user' (/?user=xxxx&...)

                id_numb = request.GET['id_vend']         # Find get parameter

                try:
                    user = Vendedor.objects.get(pk=id_numb)   # Get the object in database
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                serializer = VendSerializer(user)           # Serialize the object data into json
                return Response(serializer.data)            # Return the serialized data

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
            
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    
# POST

    if request.method == 'POST':

        new_vend = request.data
        
        serializer = VendSerializer(data=new_vend)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(status=status.HTTP_400_BAD_REQUEST)

# PUT

    if request.method == 'PUT':

        id_number = request.data['cnpj']

        try:
            updated_user = Vendedor.objects.get(pk=id_number)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = VendSerializer(updated_user, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
        return Response(status=status.HTTP_400_BAD_REQUEST)

# DELETE

    if request.method == 'DELETE':

        try:
            user_to_delete = Vendedor.objects.get(pk=request.data['id_vend'])
            user_to_delete.delete()
            return Response(status=status.HTTP_202_ACCEPTED)
        except:
            return Response(status=status.HTTP_400_BAD_REQUEST)