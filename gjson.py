import json
from shapely.geometry import Polygon, Point


class DistrictJSON:
    def __init__(self, filename):
        self._filename = filename
        self._poly_dict = {}

        self.load()

    def load(self):
        with open(self._filename) as f:
            data = json.loads(f.read())

            for shape in data['features']:
                id = int(shape['properties']['TUNNUS'])
                coords = shape['geometry']['coordinates'][0]
                self._poly_dict[id] = Polygon(coords)

    def get_polygon(self, id):
        return self._poly_dict[id]


def main():
    file = 'osaalueet.geojson'
    districts = DistrictJSON(file)
    districts.load()
    print(districts.get_polygon(171))
    print(districts.get_polygon(171).contains(Point(24.92046539288323, 60.20190764575884)))


if __name__ == '__main__':
    main()