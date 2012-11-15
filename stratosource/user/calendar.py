
import httplib, urllib
#from stratosource.admin.models import CalendarEvent
#from django.core.exceptions import ObjectDoesNotExist
from stratosource.admin.management import ConfigCache

def submitCalendarREST(method, params):
    cal_host = ConfigCache.get_config_value('calendar.host')
    if cal_host is None or len(cal_host) == 0: return

    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/javascript"}
    conn = httplib.HTTPConnection(cal_host)
    conn.request("POST", "/wdcalendar/php/datafeed.php?method=%s" % method, params, headers)
    response = conn.getresponse()
    print "%s=%s %s" % (method, response.status, response.reason)
    conn.close()


def addCalendarReleaseEvent(release_id, release_name, relDate):
    datestr = relDate.strftime('%m/%d/%Y')
    params = urllib.urlencode({'StartTime': datestr, 'EndTime': datestr, 'Subject': release_name, 'ReleaseId': release_id})
    submitCalendarREST('addrelease', params)
#    event = CalendarEvent()
#    event.subject = release_name
#    event.startTime = relDate
#    event.endTime = relDate
#    event.isAllDayEvent = 1
#    event.release_id = release_id
#    event.save()

def updateCalendarReleaseEvent(relid, relDate):
    datestr = relDate.strftime('%m/%d/%Y')
    params = urllib.urlencode({'StartTime': datestr, 'EndTime': datestr, 'ReleaseId': relid})
    submitCalendarREST('updaterelease', params)
#    try:
#        event = CalendarEvent.objects.get(release_id=relid)
#        event.startTime = relDate
#        event.endTime = relDate
#        event.save()
#    except ObjectDoesNotExist:
#        pass


def removeCalendarReleaseEvent(release_id):
    params = urllib.urlencode({'ReleaseId': release_id})
    submitCalendarREST('removerelease', params)
#    try:
#        event = CalendarEvent.objects.get(release_id=release_id)
#        event.delete()
#    except ObjectDoesNotExist:
#        pass
    pass
