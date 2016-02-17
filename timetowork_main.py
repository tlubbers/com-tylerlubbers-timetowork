from TimeToWork import TimeToWork
import urllib2
import json
import time

if __name__ == "__main__":

    apt_address_list = ['1940 Overlook Run Place Cumming GA','411 North Roosevelt Ave Bloomington IL','9401 roberts drive sandy springs GA','1970 Peachford Road dunwoody GA', '4000 dunwoody park dunwoody ga','302 perimeter center north atlanta ga', '1155 hammond drive sandy springs ga', '4777 Ashford Dunwoody Rd, Dunwoody, GA 30338']

    apt_name_list = ['Moms House', 'Bloomington', 'Lodge on the Chat', 'Dunwoody Gables', 'Two Blocks', 'The Bricks', 'Citizen', 'Post Crossing']

    current_office_addr = ['North Terraces 400 Perimeter Center Terrace Atlanta GA 30346']

    drivemode = "driving"

    ttw = TimeToWork()

    try:
      print ("DRIVE TIMES TO CURRENT WORK ADDRESS")
      print ("============================")
      ttw.make_request(apt_address_list, current_office_addr, mode=drivemode)
      dump = json.dumps(ttw.response, ensure_ascii=False, sort_keys=True, indent=2)
      decoded = json.loads(dump)
      count = 0
      for x in decoded:
        print (x['elements'][0]['duration']['text'] + " from " + apt_name_list[count])
        count = count + 1

    except urllib2.URLError, e:
        print "Error:",