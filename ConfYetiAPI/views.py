from django.http import JsonResponse, HttpResponseBadRequest, HttpResponse
import json
from dateutil import parser

with open('data/conferences.json', 'r') as conferences_json:
    conferences = json.load(conferences_json)


def filter_conferences(request):
    global conferences

    ids = request.GET.getlist('id')
    projects = request.GET.getlist('project')
    participants = request.GET.getlist('participant')
    input_date = request.GET.get('dateStart')
    if input_date:
        try:
            date_start = parser.parse(request.GET.get('dateStart'))
        except parser.ParserError:
            return HttpResponse('Invalid date', status=422)
    else:
        date_start = None
    if len(request.GET.getlist('dateStart')) > 1:
        return HttpResponseBadRequest('dateStart param should be unique')

    input_date = request.GET.get('dateFinish')
    if input_date:
        try:
            date_finish = parser.parse(request.GET.get('dateFinish'))
        except parser.ParserError:
            return HttpResponse('Invalid date', status=422)
    else:
        date_finish = None
    if len(request.GET.getlist('dateFinish')) > 1:
        return HttpResponseBadRequest('dateFinish param should be unique')

    relevant_conferences = []
    for conference in conferences:
        if (not ids or conference['_id'] in ids) \
                and (not projects or (set(conference['projects']) & set(projects))) \
                and (not participants or (set(conference['participants'].keys()) & set(participants))) \
                and (not date_start or (date_start <= parser.parse(conference['dateStart'][:10]))) \
                and (not date_finish or (date_finish >= parser.parse(conference['dateFinish'][:10]))):
            relevant_conferences.append(conference)
    return JsonResponse(relevant_conferences, safe=False)
