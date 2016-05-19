# -*- coding: utf-8 -*-

import pysal
from shapely.geometry import Polygon, Point
import csv
from gjson import DistrictJSON


AREA_CODE_DICT = {
    "Länsi-Pasila": 171,
    "Itä-Pasila": 173
}


def select_by_location(input, output, polygon):
    n = 0
    fin = pysal.open(input)
    with open(output, 'w') as fout:
        writer = csv.writer(fout)

        for i in range(len(fin)):
            if i == 0:
                writer.writerow(fin[0])
            else:
                coord = fin[i][0][1]
                if coord != 'NA':
                    lat, lon = coord.split(',')
                    point = Point(float(lon), float(lat))
                    if polygon.contains(point):
                        n += 1
                        writer.writerow(fin[i])

    print(n)


def main():
    input = "records_with_coordinates.csv"
    results = "lpasila_records.csv"
    districts_file = 'osaalueet.geojson'

    districts = DistrictJSON(districts_file)

    poly = districts.get_polygon(AREA_CODE_DICT['Länsi-Pasila'])

    select_by_location(input, results, poly)
    print(poly.centroid)


if __name__ == '__main__':
    main()
