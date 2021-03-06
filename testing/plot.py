import pandas
import pandas as pd

# Import matplotlib and Basemap
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

# Set iPython to display visualization inline
#%matplotlib inline

raw_data = {'latitude': [27.173968, 27.164328, 20.930555, 31.784217, 29.935895],
            'longitude': [78.037519, 78.015289, 49.948611, 35.134277, 29.935895]}
df = pd.DataFrame(raw_data, columns = ['latitude', 'longitude'])
df

# Create a figure of size (i.e. pretty big)
fig = plt.figure(figsize=(20,10))
# Create a map, using the Gall–Peters projection
map = Basemap(projection='gall',
              # with low resolution,
              resolution = 'l',
              # And threshold 100000
              area_thresh = 100000.0,
              # Centered at 0,0 (i.e null island)
              lat_0=0, lon_0=0)

# Draw the coastlines on the map
map.drawcoastlines()

# Draw country borders on the map
map.drawcountries()

# Fill the land with grey
map.fillcontinents(color = '#888888')

# Draw the map boundaries
map.drawmapboundary(fill_color='#f4f4f4')

# Define our longitude and latitude points
# We have to use .values because of a wierd bug when passing pandas data
# to basemap.
x,y = map(df['longitude'].values, df['latitude'].values)

# Plot them using round markers of size 6
map.plot(x, y, 'ro', markersize=6)

# Show the map
plt.show()
