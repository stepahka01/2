from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    host_name = request.META["HTTP_HOST"],
    user_agent = request.META["HTTP_USER_AGENT"],
    client_address = request.META["REMOTE_ADDR"],

    return HttpResponse(f"""
    <p>Host: {host_name}</p> 
    <p>User_Agent: {user_agent}</p>
    <p>Client_Address: {client_address}</p>
    """)


def error(request):
    return HttpResponse("К сожалению, произошла ошибка", status=400, reason="Incorect data")


def user(request, name='Undefined', folder='Undefined', folder_num=0):
    return HttpResponse(f"Name:{name}, Folder_Name:{folder}, Folder_Num:{folder_num}")
