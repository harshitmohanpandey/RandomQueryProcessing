Content-Type: application/json
Request Type: POST

Usecase 1:

URL :http://127.0.0.1:8000/v1/api/usecase/
Payload: {"usecase":"1","occuredbefore":"01-06-2017","brockendownby":"channel,country","sortby":"clicks","sortorder":"descending"}

Usecase 2:

URL:http://127.0.0.1:8000/v1/api/usecase/
Payload:{"usecase":"2","revenuemonth":"05-2017","os":"ios","brockendownby":"date","sortby":"date","sortorder":"ascending"}

Usecase 3:

URL:http://127.0.0.1:8000/v1/api/usecase/
Payload:{"usecase":"3","revenuedate":"01-06-2017","country":"US","brockendownby":"os,date","sortby":"revenue","sortorder":"descending"}

Usecase 4:

URL:http://127.0.0.1:8000/v1/api/usecase/
Payload:{"usecase":"4","country":"CA","brockendownby":"channel,country","sortby":"CPI","sortorder":"descending"}

Steps to run the code using command line interface:

step1: Install all dependencies from requirements.txt file.
step2: Open CMD interface and run:   python manage.py runserver

Notes:
1.In each json payload you can have multiple brockendownby columns.
2.sortby any column.
3.sortorder value can only be ascending or descending.
4. country and os values can also be changed according to need.
