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

landing_page_html = """
<h1>Numina Dashboard</h1>
Welcome to our Numina Dashboard!
<br><br>
By Amy, Antoine, and Faraz
"""

zone_reference_html = """
<h3>Under Raincoat</h3> <br> <img src="img/UnderRaincoatZones.png"> <br>
<h3>Streetscape</h3> <br> <img src="img/StreetscapeZones.png"> <br>
<h3>Outside</h3> <br> <img src="img/OutsideZones.png">
"""

privacy_statement_html = """
<h1>Our Privacy Philosophy</h1>
In the digital world today, the balance between personal privacy and the benefits of data collection are often scrutinized. In our website, we queried Numina API data from the sensors at 307 for use in our data analysis. Throughout all of our data processing, we respected the privacy of indivduals being recorded and did not include any personally identiable information about them. In addition, the sample images overlayed in our heatmaps have no recognizable people or faces in them. The majority of the Numina data was used strictly for counting occurences of objects detected at certain times near the sensors.
<br><br>
Overall, data collection is significantly beneficial and informative for society as it supports smart decision making by companies and the government. The analysis from data helps society understand people's interactions and as a result, helps people efficiently tailor action for specific needs. For instance, in this case it helps Sidewalk Labs make informed decisions about future developments or construction based on data analysis on dwell time and pedestrian traffic. We believe that the benefits for this method of data collection outweigh the negligible privacy concerns.
"""