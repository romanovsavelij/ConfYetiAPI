# ConfYetiAPI

REST API for Conf Yeti

## Install

    pip3 install django
    pip3 install python-dateutil

## Run the app

    python3 manage.py runserver 8000

## Run the tests

    python3 manage.py test

## Requests

* **URL**

  /conferences/

* **Method:**

  `GET`
  
*  **Query string params**

   **Optional:**
 
   `id=[alphanumeric]` <br />
    *id=5c092621a19ac14bd086c39e*
       
   **Optional:**
 
   `project=[string]` <br />
   *project=WebStorm*
   
   **Optional:**
 
   `participant=[string]` <br />
   *participant=Anna.Smolkina*

   **Optional:**
 
   `dateStart=[<YEAR>-<MONTH>-<DATE>]` <br />
   *dateStart=2019-02-09*
   
   **Optional:**
 
   `dateFinish=[<YEAR>-<MONTH>-<DATE>]` <br />
   *dateFinish=2019-02-09*
  
   **Multiple values**
   
   You can specify several values of id, project and participant params. In this case you will get all the conferences, containing at least one of the ids, one of the project and one of the participants, specified in params.
   
   However, dateStart and dateFinish params should be unique.
   
  
* **Success Response:**

  * **Code:** 200 <br />
    **Content:** JSON containing conferences filtered by given params 
 
* **Error Response:**

  * **Code:** 400 Bad Request <br />
    **Content:** `dateStart param should be unique`
    
  * **Code:** 400 Bad Request <br />
    **Content:** `dateFinish param should be unique`
    
  * **Code:** 422 UNPROCESSABLE ENTRY <br />
    **Content:** `Invalid date`
   
## Examples

### Request

`curl -i -X GET -d 'project=WebStorm&project=PyCharm&dateStart=2019-02-09' http://localhost:8000/conferences/`

### Result

Those conferences which start not earlier than 2019-02-09 and related to either WebStorm or PyCharm.

### Response
```
HTTP/1.1 200 OK
Date: Sat, 04 Apr 2020 17:12:09 GMT
Server: WSGIServer/0.2 CPython/3.7.4
Content-Type: application/json
X-Frame-Options: DENY
Content-Length: 6578
X-Content-Type-Options: nosniff

[{"_id": "5c092621a19ac14bd086c39e", "title": "Techfest 2019", "projects": ["Sales"], "location": {"city": "Nayang Technological University School of Computing", "country": "Singapore"}, "tags": [], "dateStart": "2019-02-08T12:00:00.000Z", "dateFinish": "2019-02-08T12:00:00.000Z", "participants": {}, "ytLink": "https://youtrack.jetbrains.com/issue/PANDA-4000", "attendance": 100, "link": "https://www.facebook.com/SCSETechFest2018/", "comments": [], "status": "ACCEPTED"}, {"_id": "5c092621a19ac14bd086c3ac", "title": "SunshinePHP", "projects": ["PhpStorm"], "location": {"city": "Miami, Florida", "country": "United States"}, "tags": [], "dateStart": "2019-02-08T12:00:00.000Z", "dateFinish": "2019-02-09T12:00:00.000Z", "participants": {}, "ytLink": "https://youtrack.jetbrains.com/issue/PANDA-3794", "attendance": 350, "link": "http://2018.sunshinephp.com", "comments": [], "status": "ACCEPTED"}, {"_id": "5c092621a19ac14bd086c3ae", "title": "PyTennessee", "projects": ["PyCharm"], "location": {"city": "Nashville", "country": "United States"}, "tags": [], "dateStart": "2019-02-09T12:00:00.000Z", "dateFinish": "2019-02-10T12:00:00.000Z", "participants": {}, "ytLink": "https://youtrack.jetbrains.com/issue/PANDA-3595", "attendance": 300, "link": "https://www.pytennessee.org/", "comments": [], "status": "ACCEPTED"}, {"_id": "5c092622a19ac14bd086c3b0", "title": "Academic Conference", "projects": ["Education"], "location": {"city": "Turkey", "country": "Turkey"}, "tags": [], "dateStart": "2019-02-09T12:00:00.000Z", "dateFinish": "2019-02-15T12:00:00.000Z", "participants": {}, "ytLink": "https://youtrack.jetbrains.com/issue/PANDA-3980", "attendance": 5000, "link": "https://youtrack.jetbrains.com/issue/PANDA-2791", "comments": [], "status": "PROPOSED"}, {"_id": "5c092622a19ac14bd086c3b2", "title": "frontenddeveloperlove", "projects": ["WebStorm"], "location": {"city": "Amsterdam, NL", "country": "Netherlands"}, "tags": [], "dateStart": "2019-02-13T12:00:00.000Z", "dateFinish": "2019-02-15T12:00:00.000Z", "participants": {}, "ytLink": "https://youtrack.jetbrains.com/issue/PANDA-2804", "attendance": 2000, "link": "https://www.frontenddeveloperlove.com", "comments": [], "status": "ACCEPTED"}, {"_id": "5c092622a19ac14bd086c3b4", "title": "Developers Summit Japan 2019", "projects": ["Marketing"], "location": {"city": "Tokyo, Japan", "country": "Japan"}, "tags": [], "dateStart": "2019-02-14T12:00:00.000Z", "dateFinish": "2019-02-15T12:00:00.000Z", "participants": {}, "ytLink": "https://youtrack.jetbrains.com/issue/PANDA-3992", "attendance": 2500, "link": "https://event.shoeisha.jp/devsumi/20190214", "comments": [], "status": "PROPOSED"}, {"_id": "5c092622a19ac14bd086c3b6", "title": "MODELWARD", "projects": ["MPS"], "location": {"city": "Prague", "country": "Czech Republic"}, "tags": [], "dateStart": "2019-02-20T12:00:00.000Z", "dateFinish": "2019-02-22T12:00:00.000Z", "participants": {}, "ytLink": "https://youtrack.jetbrains.com/issue/PANDA-2945", "attendance": null, "link": "http://www.modelsward.org/", "comments": [], "status": "ACCEPTED"}, {"_id": "5c092622a19ac14bd086c3b8", "title": "PHP UK 2018", "projects": ["PhpStorm"], "location": {"city": "London", "country": "United Kingdom"}, "tags": [], "dateStart": "2019-02-20T12:00:00.000Z", "dateFinish": "2019-02-22T12:00:00.000Z", "participants": {}, "ytLink": "https://youtrack.jetbrains.com/issue/PANDA-3693", "attendance": 700, "link": "https://www.phpconference.co.uk/", "comments": [], "status": "ACCEPTED"}, {"_id": "5c092622a19ac14bd086c3ba", "title": "Developer Week", "projects": ["IntelliJ IDEA", "Kotlin", ".NET"], "location": {"city": "San Francisco", "country": "United States"}, "tags": [], "dateStart": "2019-02-20T12:00:00.000Z", "dateFinish": "2019-02-24T12:00:00.000Z", "participants": {}, "ytLink": "https://youtrack.jetbrains.com/issue/PANDA-3783", "attendance": 8000, "link": "http://www.developerweek.com/", "comments": [], "status": "ACCEPTED"}, {"_id": "5c092622a19ac14bd086c3bc", "title": "Machine Learning Prague 2019", "projects": ["PyCharm", "DataLore"], "location": {"city": "Prague", "country": "Czech Republic"}, "tags": [], "dateStart": "2019-02-22T12:00:00.000Z", "dateFinish": "2019-02-24T12:00:00.000Z", "participants": {"Anna.Smolkina": {"type": "PARTICIPANT", "status": "INVITED", "invited": true}}, "ytLink": "https://youtrack.jetbrains.com/issue/PANDA-3940", "attendance": 1000, "link": "https://mlprague.com", "comments": [], "status": "ACCEPTED"}, {"_id": "5c092622a19ac14bd086c3be", "title": "NG India", "projects": ["WebStorm"], "location": {"city": "Gurgaon", "country": "India"}, "tags": [], "dateStart": "2019-02-23T12:00:00.000Z", "dateFinish": "2019-02-23T12:00:00.000Z", "participants": {}, "ytLink": "https://youtrack.jetbrains.com/issue/PANDA-3944", "attendance": 500, "link": "https://www.ng-ind.com/", "comments": [], "status": "ACCEPTED"}, {"_id": "5c38ba9cc32bcb68a56767c5", "title": "Pycon APAC", "projects": ["PyCharm"], "location": {"city": "Makati", "country": "Philippines"}, "tags": [], "dateStart": "2019-02-23T12:00:00.000Z", "dateFinish": "2019-02-24T12:00:00.000Z", "participants": {}, "ytLink": "https://youtrack.jetbrains.com/issue/PANDA-4120", "attendance": null, "link": "https://pycon-tickets.python.ph/", "comments": [], "status": "ACCEPTED"}, {"_id": "5c49a5ddc32bcb68a5676801", "title": "Javantura Conference", "projects": ["IntelliJ IDEA"], "location": {"city": "Zagreb", "country": "Croatia"}, "tags": [], "dateStart": "2019-02-23T12:00:00.000Z", "dateFinish": "2019-02-23T12:00:00.000Z", "participants": {}, "ytLink": "https://youtrack.jetbrains.com/issue/PANDA-4189", "attendance": 350, "link": "https://javantura.com/", "comments": [], "status": "REJECTED"}, {"_id": "5c542880c32bcb68a567680f", "title": "KCD 2019", "projects": ["Marketing"], "location": {"city": "Seoul", "country": "Korea, Republic of"}, "tags": [], "dateStart": "2019-02-24T12:00:00.000Z", "dateFinish": "2019-02-24T12:00:00.000Z", "participants": {}, "ytLink": "https://youtrack.jetbrains.com/issue/PANDA-4213", "attendance": 250, "link": "https://kcd2018.festa.io/", "comments": [], "status": "ACCEPTED"}, {"_id": "5c092622a19ac14bd086c3c0", "title": "Mobile World Congress", "projects": ["Marketing"], "location": {"city": "Barcelona", "country": "Spain"}, "tags": [], "dateStart": "2019-02-25T12:00:00.000Z", "dateFinish": "2019-02-28T12:00:00.000Z", "participants": {}, "ytLink": "https://youtrack.jetbrains.com/issue/PANDA-3278", "attendance": 100000, "link": "https://www.mobileworldcongress.com/", "comments": [], "status": "REJECTED"}]
```


### Request

`curl -i -X GET http://localhost:8000/conferences/?id=5c092621a19ac14bd086c3ae`

### Result

Conference with _id = 5c092621a19ac14bd086c3ae.

### Response
```
HTTP/1.1 200 OK
Date: Sat, 04 Apr 2020 17:32:11 GMT
Server: WSGIServer/0.2 CPython/3.7.4
Content-Type: application/json
X-Frame-Options: DENY
Content-Length: 422
X-Content-Type-Options: nosniff

[{"_id": "5c092621a19ac14bd086c3ae", "title": "PyTennessee", "projects": ["PyCharm"], "location": {"city": "Nashville", "country": "United States"}, "tags": [], "dateStart": "2019-02-09T12:00:00.000Z", "dateFinish": "2019-02-10T12:00:00.000Z", "participants": {}, "ytLink": "https://youtrack.jetbrains.com/issue/PANDA-3595", "attendance": 300, "link": "https://www.pytennessee.org/", "comments": [], "status": "ACCEPTED"}]
```
