import gpxpy
import gpxpy.gpx
import folium
import os

class GPX:
    def __init__(self, gpx_string):
        '''
        Initialize the GPX object with a given filename.

        Args:
            gpx_string (str): The stored string of GPX data
        '''
        self.gpx = gpxpy.parse(gpx_string)

        # Setup needed attributes of self.gpx
        self.time = self.gpx.time
    
    def display(self, map=None, zoom=10):
        '''
        Display the GPX file data on a map. 
        Args:
            map: folium.Map object to display the data on. If None, a new map is created.
            zoom: int, the zoom level of the map. Default is 10.
        Returns:
            map_html: str, the HTML string of the map. This can be used to put the map in a vue component.'''
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
        #return map - displays map directly in browser

        # Render the map to an HTML string
        map_html = map._repr_html_()
        return map_html

    def get_total_distance_km(self):
        """
        Get total distance of GPX route

        Returns:
            (float): total distance in km
        """

        distance = 0

        # calculate distance between every 2 points
        for track in self.gpx.tracks:
            for segment in track.segments:
                previous_point = None
                for point in segment.points:
                    if previous_point is not None:
                        distance += (point.distance_3d(previous_point) / 1000)
                    previous_point = point
        return distance

    def get_duration(self):
        """
        Get total duration of GPX route

        Returns:
            (int): total duration in seconds
        """

        times = []
        for track in self.gpx.tracks:
            for segment in track.segments:
                for point in segment.points:
                    if point.time != None:
                        times.append(point.time)
                    
        if len(times) == 0:
            return 0

        return (max(times) - min(times)).total_seconds()

    def get_speed(self):
        """
        Get overall speec of GPX route in km/h

        Returns:
            (float): overall speed in km/h
        """
        if self.get_duration() == 0:
            return 0

        distance_km = self.get_total_distance_km()
        duration_hours = self.get_duration() / 3600
        return distance_km / duration_hours

if __name__ =="__main__":
    with open("../example_data/track1.gpx", "r") as file:
        data = file.read()

    gpx = GPX(data)
    print(str(gpx.time))
    print(gpx.get_total_distance_km())
    hours = int(gpx.get_duration() / 3600)
    minutes = int(gpx.get_duration() % 3600 / 60)
    seconds = int(gpx.get_duration() % 60)
    print(hours, minutes, seconds)
    print(gpx.get_speed())

    with open("../example_data/track2.gpx", "r") as file:
        data = file.read()

    gpx = GPX(data)
    print(str(gpx.time))
    print(gpx.get_total_distance_km())
    hours = int(gpx.get_duration() / 3600)
    minutes = int(gpx.get_duration() % 3600 / 60)
    seconds = int(gpx.get_duration() % 60)
    print(hours, minutes, seconds)
    print(gpx.get_speed())