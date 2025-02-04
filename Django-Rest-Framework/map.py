import requests

API_KEY = "AIzaSyA8vjTv-BWMRDDfnzWTIWFAeEU2je0KcTk"

address = input("Ünvanı daxil edin: ")

def get_coordinates(address):
    url = f"https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        if data['results']:
            location = data['results'][0]['geometry']['location']
            return location['lat'], location['lng']
        else:
            print("Ünvan tapılmadı.")
            return None
    else:
        print("API sorğusu uğursuz oldu.")
        return None


def create_map_html(lat, lng):
    html_content = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Xəritə</title>
        <script src="https://maps.googleapis.com/maps/api/js?key={API_KEY}"></script>
        <script>
            function initMap() {{
                var location = {{lat: {lat}, lng: {lng}}};
                var map = new google.maps.Map(document.getElementById('map'), {{
                    zoom: 15,
                    center: location
                }});
                var marker = new google.maps.Marker({{
                    position: location,
                    map: map
                }});
            }}
        </script>
    </head>
    <body onload="initMap()">
        <h1>Xəritə</h1>
        <div id="map" style="width: 100%; height: 500px;"></div>
    </body>
    </html>
    """
    with open("map.html", "w", encoding="utf-8") as file:
        file.write(html_content)
    print("Xəritə 'map.html' faylına yaradıldı.")


coordinates = get_coordinates(address)
if coordinates:
    create_map_html(coordinates[0], coordinates[1])
