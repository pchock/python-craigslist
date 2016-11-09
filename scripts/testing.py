__author__ = 'parkerchocklett'

from craigslist import CraigslistHousing


BOXES = {

    "lake_merritt" : [
        [37.791558, -122.243114],
        [37.816616, -122.278562]
    ],

}

def in_box(coords, box):
    if box[0][0] < coords[0] < box[1][0] and box[1][1] < coords[1] < box[0][1]:
        return True
    return False

cl_h = CraigslistHousing(site='sfbay', area='eby', category='apa',
                         filters={'max_price': 5000, 'private_room': False})

for result in cl_h.get_results(sort_by='price_asc', geotagged=True, limit=2500):
    try:
        geotag = result["geotag"]
        area_found = False
        area = ""
        for a, coords in BOXES.items():
            if in_box(geotag, coords):
                area = a
                area_found = True
                print result
    except:
        pass