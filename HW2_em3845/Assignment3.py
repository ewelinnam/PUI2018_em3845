
# coding: utf-8

# In[241]:


from __future__ import print_function
import json
import pylab as pl
import os

try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import os
import sys


# In[242]:


if not len(sys.argv) == 3:
    print ("Invalid number of arguments")
    sys.exit()

mta_key = sys.argv[1]
bus = sys.argv[2]
url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=B52"%(mta_key)

#url = "http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=7b7bd724-ffd1-49fc-92c3-98e10ed83b7c&VehicleMonitoringDetailLevel=calls&LineRef=B52"
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
dataDict = json.loads(data)


# In[243]:


dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][0]['MonitoredVehicleJourney']['VehicleLocation']


# In[244]:


trips = len(dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
location = list()

i = 0
for i in range(trips):
    if(dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['PublishedLineName']==bus):
        location.append(dataDict['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation'])  


# In[245]:


i = 0
print("Bus Line: "+bus)
print("Number of active buses:"+str(len(location)))
for i in range(len(location)):
    
    print("Bus "+str(i)+"is at "+str(location[i]))

