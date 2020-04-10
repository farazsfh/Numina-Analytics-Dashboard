import datetime as dt


devices = {'Streetscape': ('SWLSANDBOX1', 'img/Streetscape.png'), 'Outside': ('SWLSANDBOX3', 'img/Outside.png'),
           'UnderRaincoat': ('SWLSANDBOX2', 'img/UnderRaincoat.png')}

events = {'City Moments': (dt.datetime(2019, 8, 16, 19), dt.datetime(2019, 8, 17, 2)),
         'Open Sidewalk #4': (dt.datetime(2019, 3, 2, 15), dt.datetime(2019, 3, 2, 19)),
         'Sidewalk Summer Open House': (dt.datetime(2019, 6, 29, 12), dt.datetime(2019, 6, 29, 18)),
         'Startup Open House': (dt.datetime(2019, 9, 26, 16), dt.datetime(2019, 9, 26, 20)),
         'Tap:Ex Augmented Opera Day 1': (dt.datetime(2019, 11, 20, 18), dt.datetime(2019, 11, 20, 22)),
         'Tap:Ex Augmented Opera Day 2': (dt.datetime(2019, 11, 21, 18), dt.datetime(2019, 11, 21, 22)),
         'Tap:Ex Augmented Opera Day 3': (dt.datetime(2019, 11, 22, 18), dt.datetime(2019, 11, 22, 22)),
         'Tap:Ex Augmented Opera Day 4': (dt.datetime(2019, 11, 23, 18), dt.datetime(2019, 11, 23, 22))}

# User-defined sensor zones and their corresponding Numina IDs
OutsideZones = {'Tables': 43034,
                 'Hedge': 43035,
                 'Raincoat': 43036,
                 'Tiles': 43037,
                 'Concrete': 43038,
                 'Leaf': 43039}

RaincoatZones = {'Entrance': 43048,
                 'Top Raincoat': 43049,
                 'Right Raincoat': 43050,
                 'Left Raincoat': 43051,
                 'Right Concrete': 43052,
                 'Left Concrete': 43053}

StreetscapeZones = {'Back Building': 43040,
                 'Side Building': 43041,
                 'Tables': 43042,
                 'Left Walkway': 43043,
                 'Right Walkway': 43044,
                 'Stairs': 43045,
                 'Left of Tables': 43046,
                 'Right of Tables': 43047}

inv_OutsideZones, inv_RaincoatZones, inv_StreetscapeZones = [{v: k for k, v in x.items()} 
                                                             for x in [OutsideZones, 
                                                                       RaincoatZones, 
                                                                       StreetscapeZones]]

# HTML for the landing page
landing_page_html = """
<h1>Numina Dashboard</h1>
Welcome to our Numina Dashboard! Please ensure that a "login.py" file with the variables "login" and "pwd" exist, with values that are a valid email address and the corresponding password. <i>To begin, in Jupyter notebook, click the "Voila" widget in the toolbar; you will need to select a new option in the dropdown on each dashboard tab to load the graphs. The graphs take a moment to load (possible a couple minutes), so do not stress if they do not appear right away.</i>
<br>
By Amy, Antoine, and Faraz
<br><br>

<h2>Considerations We Took Into Account</h2>
<ul>
<li>Due to there being little data involving bicycles or vehicles, we have omitted them from our dashboards. This was done to reduce query load to slightly improve our dashboard's performance. If the sensor involved more roads, we would be sure to include bicycle and vehicle data in our dashboard.</li>
<li>This dashboard was designed to answer specific questions in mind; as such, the tabs are organized to allow users to answer these questions for themselves.</li>
<li>We decided to use Plotly for our dashboard, which gives the user the ability to interact with (in addition to customizing the queries/parameters). However, this comes with drawbacks, </li>
</ul>

<h2>Documentation/User Guide</h2>

<b>View by Event</b><br>
This tab allows users to view data for a certain event. This list of events was scraped from the web and condensed to include only events that occurred at 307. Users are also able to pick the sensor and choose if they want to look at data only for a given hour or the cumulative data up to a given hour. 
<br><i>Heatmap</i>: A simple heatmap of sensor activity for pedestrians for the given sensor. The warmer the color, the less activity there was; likewise, the cooler the cooler the area, the more activity there was. This was produced by simply querying the Numina API.
<br><i>Desire line Heatmap</i>: A heatmap that emphasize areas with a high level of area, but with a low gradient (more simply, connected areas with very similar color/density on a heatmap). The darker blue lines represent common paths people tend to follow when walking. Data was first queried from the Numina API, then a simple gradient field was calculated. Next, the gradient field is multiplied by the heatmap (to emphasize areas with high density but low gradient).
<br><i>Hourly Dwell Time [parameter]</i>: The user first selects the dwell time parameter they want to look at from the interact buttons (mean dwell time, median dwell time, etc.) for the sensor and date range. This data was simply queried from the Numina API.
<br><i>Dwell time [parameter] by Zone</i>: After the user selects a parameter, this graph displays the [parameter] dwell time for each zone for the given sensor (these zones can be seen in the "Zone References" tab). Like the previous graph, this data was just queried from the Numina API after manually creating the zones.

<br><b>View by Date Range</b><br>
This tab is very similar to the "View by Event" tab, except users are able to select a date range instead of a single event. Please refer to the section above for detailed information about each graph.

<br><b>Plan Maintenance</b><br>
This tab allows users (most importantly those who overlook the site) to see the mean pedestrian counts by weekday, the mean pedestrian counts by hour, and a timeseries graph of daily pedestrian counts. The user can also select which day of the week they want to schedule maintenance, and after how many hours of "usage" maintenance should occur. An algorithm then calculates when to best do maintenance with these parameters and plots them has red vertical bars. "Usage" is defined as how many people visit the are the sensor covers, and takes into consideration that events are high usage.

<br><b>Privacy Statement</b><br>
An outline of our privacy philosophy, and how we incorporated it into our dashboard. 
<br><b>Zone Reference</b><br>
A tab that explains and graphically displays the zone breakdown of each sensor; this information is most useful when analyzing the dwell time information. The text corresponds with the zone name (accessible from Numina's own dashboard), and the lines indicate the zone boundaries.
"""

zone_reference_html = """
<h3>Under Raincoat</h3> <br> <img src="img/UnderRaincoatZones.png"> <br>
<h3>Streetscape</h3> <br> <img src="img/StreetscapeZones.png"> <br>
<h3>Outside</h3> <br> <img src="img/OutsideZones.png">
"""

# HTML for the privacy statement
privacy_statement_html = """
<h1>Our Privacy Philosophy</h1>
In the digital world today, the balance between personal privacy and the benefits of data collection are often scrutinized. In our website, we queried Numina API data from the sensors at 307 for use in our data analysis. Throughout all of our data processing, we respected the privacy of individuals being recorded and did not include any personally identifiable information about them. In addition, the sample images overlayed in our heatmaps have no recognizable people or faces in them. The majority of the Numina data was used strictly for counting occurrences of objects detected at certain times near the sensors.
<br><br>
Overall, data collection is significantly beneficial and informative for society as it supports smart decision making by companies and the government. The analysis from data helps society understand people's interactions and as a result, helps people efficiently tailor action for specific needs. For instance, in this case it helps Sidewalk Labs make informed decisions about future developments or construction based on data analysis on dwell time and pedestrian traffic. We believe that the benefits for this method of data collection outweigh the negligible privacy concerns.
<br><br>

<h3>Data We Used</h3>
In order to create our visualizations and tables for our dashboard, we used the Numina API to collect data. All the information we gather through the Numina API is aggregate, meaning it does not provide us with any information involving a specific person. For example, our dwell time values are the mean of dwell time values for everyone detected by a sensor. In the following table, we describe all types of data we used and how we ensured that we were respecting the privacy of people detected by the sensor.

<img src="img/DataSources.png"  width="1192" height="306">
"""