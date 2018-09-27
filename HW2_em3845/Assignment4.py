
# coding: utf-8

# In[227]:



from __future__ import print_function
import json
import pylab as pl
import os
import sys

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os
import sys

if not len(sys.argv) == 4:
    print ("Invalid number of arguments")
    sys.exit()

mta_key = sys.argv[1]
bus = sys.argv[2]
fout = open(sys.argv[3], "w")
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=B52"%(mta_key)


#url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=7b7bd724-ffd1-49fc-92c3-98e10ed83b7c&VehicleMonitoringDetailLevel=calls&LineRef=B52"
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
dataDict = json.loads(data)


# In[229]:



trips = len(dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
location = list()
next_stop = list()


# In[230]:


i = 0
for i in range(trips):
    stop = list()
    loc = list()
    if(dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['PublishedLineName']==bus):
        loc.append(dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude'])  
        loc.append(dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude'])  

        location.append(loc)
        if len(dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls'])!=0:
            stop.append(dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][1]['StopPointName'])
            stop.append(dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['OnwardCalls']['OnwardCall'][1]['Extensions']['Distances']['PresentableDistance'])
        else:
            stop.append("N/A")
            stop.append("N/A")
    next_stop.append(stop)


# In[232]:




fout.write("Latitude,Longitude,Stop Name,Stop Status\n")
    
for i in range(len(location)):
    thisline = ""
    thisline += str(location[i][0])+','+str(location[i][1])+','+str(next_stop[i][0])+','+str(next_stop[i][1])
    fout.write(thisline+"\n")

