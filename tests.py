import unittest
import utils


class MyTestCase(unittest.TestCase):

    def test_bbox_creator_radius_0(self):
        try:
            bbox = utils.location_to_bounding_box_by_radius(10, 15, 0)
            self.assertEqual([10, 15, 10, 15], bbox)
        except AssertionError:
            pass
        except Exception as e:
            self.fail('Unexpected exception raised: %s' % e)
        else:
            self.fail('ExpectedException not raised')

    def test_bbox_creator_latlon_0(self):
        bbox = utils.location_to_bounding_box_by_radius(0, 0, 15)
        self.assertEqual(0, sum(bbox))
        self.assertEqual(bbox[0], -1 * bbox[2])
        self.assertEqual(bbox[1], -1 * bbox[3])

    def test_bbox_creator_lon_negative_longitude_is_0(self):
        sign = lambda a: (a > 0) - (a < 0)
        bbox = utils.location_to_bounding_box_by_radius(-10, 0, 15)
        self.assertNotEqual(sign(bbox[0]), sign(bbox[2]))
        self.assertEqual(sign(bbox[1]), sign(bbox[3]))

    def test_bbox_creator_symmetry(self):
        bbox_1= utils.location_to_bounding_box_by_radius(37, 33, 15)
        bbox_2= utils.location_to_bounding_box_by_radius(-37, -33, 15)
        self.assertEqual(sum(bbox_1), -1 * sum(bbox_2))
        self.assertEqual(bbox_1[0], -1 * bbox_2[2])
        self.assertEqual(bbox_1[1], -1 * bbox_2[3])
        self.assertEqual(bbox_1[2], -1 * bbox_2[0])
        self.assertEqual(bbox_1[3], -1 * bbox_2[1])

    def test_bbox_symmetry_on_zero_lines(self):
        bbox_1= utils.location_to_bounding_box_by_radius(0, 30, 10)
        bbox_2= utils.location_to_bounding_box_by_radius(30, 0, 10)
        self.assertEqual(sum(bbox_1), sum(bbox_2))
        self.assertEqual(bbox_1[0], bbox_2[1])
        self.assertEqual(bbox_1[2], bbox_2[3])


    def test_external_api(self):
        url = '''http://www.overpass-api.de/api/xapi?way[amenity=school][bbox=%s]'''
        response_from_osm_api = utils.get_nodes([144.877, -37.8195, 144.931, -37.77], url)
        all_ways_node = response_from_osm_api['osm']['way']

        ## test by counting :
        sum = 0
        for way in all_ways_node:
            if 'tag' in way:
                sum += 1 if {'k': 'amenity', 'v': 'school'} in way['tag'] else 0

        # validate sum equal to len (all_ways_node)
        self.assertEqual(sum, len(all_ways_node))



if __name__ == '__main__':
    unittest.main()
