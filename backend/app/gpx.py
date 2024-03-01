import gpxpy
import gpxpy.gpx
import folium
import os

class GPX:
    def __init__(self, filename):
        gpx_file_path = os.path.abspath('../example_data/'+filename)
        gpx_file = open(gpx_file_path, 'r')
        self.gpx = gpxpy.parse(gpx_file)
    
    def display(self, map=None, zoom=10):
        points = []
        for track in self.gpx.tracks:
            for segment in track.segments:        
                for point in segment.points:
                    points.append(tuple([point.latitude, point.longitude]))
        latitude = sum(p[0] for p in points)/len(points)
        longitude = sum(p[1] for p in points)/len(points)
        if not map:
            map = folium.Map(location=[latitude,longitude],zoom_start=zoom)
        folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(map)
        return map
    
    def get_moving_data(self):
        return self.gpx.get_moving_data()



    

# Be careful of waypoint2.gpx - it has a LOT of waypoints and runs very fucking slow
# Only uncomment one of these at a time - they stop the program when opened

# display_waypoints('waypoint1.gpx', 14).show_in_browser()
# display_track('track1.gpx', 14).show_in_browser()
# display_track('track2.gpx', 10).show_in_browser()
g = GPX('track1.gpx')
# g.display(13).show_in_browser()
print(g.get_moving_data())