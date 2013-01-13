from django.http import HttpResponse, Http404
from django.template import Context
from django.template.loader import get_template
import datetime
from django.shortcuts import render_to_response

# Prints Hello world
def hello(request):
    return HttpResponse("Hello world")

# Returns the date and time in html
def current_datetime(request):
    now = datetime.datetime.now()
    # t = get_template('current_datetime.html')
    # html = t.render(Context({'current_date': now}))
    # return HttpResponse(html)
    return render_to_response('current_datetime.html', {'current_date': now})


def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    # html = "<html><body>In {} hour(s), it will be {}.</body></html>".format(offset, dt)
    # return (html)
    return render_to_response('hours_ahead.html', {'hours_offset': offset, 'next_time': dt})
