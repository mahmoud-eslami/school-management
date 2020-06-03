from rest_framework.response import Response
from rest_framework import status
from random import randint

# make a method for reusable Response
def CustomResponse(self , status_code , errors , message , data , status):
    return Response({"status_code":str(status_code),"error":errors,"data":data,"message":message},status)

# give me number of digit . random code generated wit size of that digit
def GenerateResetCode(self, num):
    start_with = 10**(num-1)
    end_with = (10**num)-1
    return randint(start_with,end_with)
