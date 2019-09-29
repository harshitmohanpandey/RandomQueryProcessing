"""this file contains code for accepting POST request and parse json values then call usecase methods"""
from rest_framework.response import Response
from rest_framework.views import APIView
from .usecase import *


class check(APIView):
    
    def post(self, request, format=None):
        """
        Accepts user request , and calls use_case_one function to run query
        """
        try:
            groupby=tuple(x+"_field" for x in request.data['brockendownby'].split(','))
            sortby=request.data['sortby']
            if request.data['sortby']!='CPI':
                sortby=sortby +"_field"
            
            if request.data['sortorder'].lower() == "descending":           
                sortby="-"+sortby

            if request.data['usecase'] =="1":                
                date=request.data['occuredbefore']           
                output_entries=use_case_one(groupby,date,sortby)

            elif request.data['usecase'] =="2":
                os=request.data['os']
                revenuemonth=request.data['revenuemonth']
                datefrom="01-"+revenuemonth
                dateto="31-"+revenuemonth
                output_entries=use_case_two(groupby,datefrom,dateto,os,sortby)

            elif request.data['usecase'] =="3":
                revenuedate=request.data['revenuedate']
                country=request.data['country']            
                output_entries=use_case_three(groupby,revenuedate,country,sortby) 

            elif request.data['usecase'] =="4":  
                country=request.data['country']            
                output_entries=use_case_four(groupby,country,sortby)

            else:  return Response({"Message":"No use case found"},status=400)

            return Response(output_entries)

        except Exception as e:
            return Response({"Message":"Error Occured while processing your request. This information might be helpfull"+str(e)},status=500)

