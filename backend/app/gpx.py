import gpxpy
import gpxpy.gpx
import folium
import os

def display_track(file_name, zoom):
    '''
    overlay a gpx route on top of an OSM map using Folium
    some portions of this function were adapted
    from this post: https://stackoverflow.com/questions/54455657/
    how-can-i-plot-a-map-using-latitude-and-longitude-data-in-python-highlight-few
    '''
    gpx_file_path = os.path.abspath('../example_data/'+file_name)
    gpx_file = open(gpx_file_path, 'r')
    gpx = gpxpy.parse(gpx_file)
    points = []
    for track in gpx.tracks:
        for segment in track.segments:        
            for point in segment.points:
                points.append(tuple([point.latitude, point.longitude]))
    latitude = sum(p[0] for p in points)/len(points)
    longitude = sum(p[1] for p in points)/len(points)
    myMap = folium.Map(location=[latitude,longitude],zoom_start=zoom)
    folium.PolyLine(points, color="red", weight=2.5, opacity=1).add_to(myMap)
    return (myMap)

def display_waypoints(file_name, zoom):
    '''
    overlay a gpx route on top of an OSM map using Folium
    some portions of this function were adapted
    from this post: https://stackoverflow.com/questions/54455657/
    how-can-i-plot-a-map-using-latitude-and-longitude-data-in-python-highlight-few
    '''
    gpx_file_path = os.path.abspath('../example_data/'+file_name)
    gpx_file = open(gpx_file_path, 'r')
    gpx = gpxpy.parse(gpx_file)
    points = []
    for point in gpx.waypoints:
        points.append(tuple([point.latitude, point.longitude]))
    latitude = sum(p[0] for p in points)/len(points)
    longitude = sum(p[1] for p in points)/len(points)
    myMap = folium.Map(location=[latitude,longitude],zoom_start=zoom)
    for point in gpx.waypoints:
        folium.Marker(location=[point.latitude, point.longitude], popup=point.name).add_to(myMap)
    return (myMap)

# Be careful of waypoint2.gpx - it has a LOT of waypoints and runs very fucking slow
# Only uncomment one of these at a time - they stop the program when opened

# display_waypoints('waypoint1.gpx', 14).show_in_browser()
display_track('track1.gpx', 14).show_in_browser()
# display_track('track2.gpx', 10).show_in_browser()