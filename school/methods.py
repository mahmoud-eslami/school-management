from rest_framework.response import Response
from rest_framework import status

# make a method for reusable Response
def CustomResponse(self , status_code , errors , message , data , status):
    return Response({"status_code":str(status_code),"error":errors,"data":data,"message":message},status)
