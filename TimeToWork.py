import json
import urllib2
import urllib
import os
import copy
import ast
import operator
import time

DISTANCE_MATRIX_URL = "http://maps.googleapis.com/maps/api/distancematrix/"

KEY = "AIzaSyCVrl2L1WEwK1qAlztvfguRxAJSE4ihago"

class TimeToWork(object):
  def __init__(self, api_key=KEY, url=DISTANCE_MATRIX_URL, current_office_addr = "North Terraces 400 Perimeter Center Terrace Atlanta GA 30346", transit_mode = "driving"):
    self.api_key = api_key
    self.url = url
    self.response = ''
    self.origins = ''
    self.destinations = ''
    self.dict_response = {'distance': {'value': {}, 'text': {}, },
                          'duration': {'value': {}, 'text': {}, },
                         }
    self.current_office_addr = current_office_addr
    self.transit_mode = transit_mode

  def make_request(self, origins, destinations, transit_mode, timeout=None):
    data = {}
    self.origins = [origins] if type(origins) == str else origins
    self.destinations = [destinations] if type(destinations) == str else destinations
    data['origins'] = origins if type(origins) == str else '|'.join(origins)
    data['destinations'] = destinations if type(destinations) == str else '|'.join(destinations)

    data['mode'] = mode

    url_values = urllib.urlencode(data)
    output_format = 'json'
    url = os.path.join(self.url, output_format)

    # print ast.literal_eval(urllib2.urlopen(url + '?' + url_values).read())
    self.response = ast.literal_eval(urllib2.urlopen(url + '?' + url_values, timeout=timeout).read())['rows']
    self.dict_response = {'distance': {'value': {}, 'text': {}, },  # Reset temporary dict
                          'duration': {'value': {}, 'text': {}, },
                          }
    return True

  def print_times_to_current_work_address():
    try:
      print ("DRIVE TIMES TO CURRENT WORK ADDRESS")
      print ("============================")
      make_request(apt_address_list, current_office_addr, mode=drivemode)
      dump = json.dumps(ttw.response, ensure_ascii=False, sort_keys=True, indent=2)
      decoded = json.loads(dump)
      count = 0
      for x in decoded:
        print (x['elements'][0]['duration']['text'] + " from " + apt_name_list[count])
        count = count + 1

    except urllib2.URLError, e:
        print "Error:",

  def log_time_increments_as_CSV(delay=None, increment_length = None, number_of_increments):

    increment_in_seconds = 15*60
    if (increment_length != None)
      increment_in_seconds = increment_length * 60

    if (delay != None):
      sleep(delay)

    i = 0
    while (i != number_of_increments):






