import urllib2, json

API_KEY = '248079717ad743e5a371c11af1d8f800'


def get_bills(state, type):
  '''
  This function should accomplish the following tasks:
    - Open a connection to the /bills/ endpoing of Sunlight Foundation's OpenStates API:
      http://sunlightlabs.github.io/openstates-api/bills.html#methods/bill-search
    - Retrieve an API response with bills from the current legislative session in Missouri
    - print the titles of bills that contain "Transportation" in the "subjects" list
  '''
  response = urllib2.urlopen('http://openstates.org/api/v1/bills/?apikey=%s&state=%s&2015' % (API_KEY, state))
  json_objects_list = json.loads(response.read())

  for bill in json_objects_list:
    if type in bill['subjects']:
      print bill['title']


get_bills("mo",'Transportation')
