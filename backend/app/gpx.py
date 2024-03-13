import gpxpy
import gpxpy.gpx
import folium
import os

class GPX:
    
    def __init__(self, filename):
        '''
        Initialize the GPX object with a given filename.

        Args:
            filename (str): The name of the file to be parsed.
        '''
        gpx_file_path = os.path.abspath('./example_data/'+filename)  #example_data is now in backend directory to load it into docker image.
        #TODO: remove example_data once upload functionality is implemented properly
        gpx_file = open(gpx_file_path, 'r')
        self.gpx = gpxpy.parse(gpx_file)
    
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

    
    #def get_moving_data(self):
        #return self.gpx.get_moving_data()