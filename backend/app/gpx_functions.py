import gpxpy

def get_total_distance_km(gpx):
    """
    Get total distance of GPX route
    Args:
        gpx (GPX): parsed GPX data

    Returns:
        (float): total distance in km
    """

    distance = 0

    # calculate distance between every 2 points
    for track in gpx.tracks:
        for segment in track.segments:
            previous_point = None
            for point in segment.points:
                if previous_point is not None:
                    distance += (point.distance_3d(previous_point) / 1000)
                previous_point = point
    return distance

def get_duration(gpx):
    """
    Get total duration of GPX route
    Args:
        gpx (GPX): parsed GPX data

    Returns:
        (int): total duration in seconds
    """

    times = []
    for track in gpx.tracks:
        for segment in track.segments:
            for point in segment.points:
                times.append(point.time)
                
    # This is not the fix! It is just to stop it crashing
    try:
        return (times[-1] - times[0]).total_seconds()
    
    except:
        return 1
    
    

def get_speed(gpx):
    """
    Get overall speec of GPX route in km/h
    Args:
        gpx (GPX): parsed GPX data

    Returns:
        (float): overall speed in km/h
    """
    distance_km = get_total_distance_km(gpx)
    duration_hours = get_duration(gpx) / 3600
    return distance_km / duration_hours

if __name__ =="__main__":
    with open("example_data/track1.gpx", "r") as file:
        data = file.read()

    gpx = gpxpy.parse(data)
    print(str(gpx.time))
    print(get_total_distance_km(gpx))
    hours = int(get_duration(gpx) / 3600)
    minutes = int((get_duration(gpx) % 3600) / 60)
    seconds = int(get_duration(gpx) % 60)
    print(hours, minutes, seconds)
    print(get_speed(gpx))