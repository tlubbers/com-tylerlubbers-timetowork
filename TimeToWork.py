import json
import urllib2
import urllib
import os
import copy
import ast
import operator

DISTANCE_MATRIX_URL = "http://maps.googleapis.com/maps/api/distancematrix/"

KEY = "AIzaSyCVrl2L1WEwK1qAlztvfguRxAJSE4ihago"

class TimeToWork(object):
  def __init__(self, api_key=KEY, url=DISTANCE_MATRIX_URL):
    self.api_key = api_key
    self.url = url
    self.response = ''
    self.origins = ''
    self.destinations = ''
    self.dict_response = {'distance': {'value': {}, 'text': {}, },
                          'duration': {'value': {}, 'text': {}, },
                         }

  def make_request(self, origins, destinations, mode='driving', timeout=None):
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

