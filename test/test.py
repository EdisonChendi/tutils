# coding: utf-8

import unittest
from tutils.ddict import Ddict


class TestDdict(unittest.TestCase):

    d = {
            'd1': {
                'd2': {
                    'd3': {
                        'd3_string': 'I am a string',
                        'd3_list': [1, 2, 3]
                    },
                    'd2_tuple': (2, 3, 4)
                },
                'd1_number': 100
            },
            'd4': "End"
        }

    def test_dict_type(self):
        d = Ddict(dict(a=1, b=2))
        self.assertTrue(isinstance(d, Ddict))
        self.assertTrue(isinstance(d, dict))

    def test_list_tuple(self):
        d = {
            'a_list': [1, 2, 3],
            'a_tuple': (4, 5, 6)
        }
        ddict_d = Ddict(d)
        self.assertDictEqual(d, ddict_d)

    def test_multi_level_dict(self):
        ddict_d = Ddict(self.d)
        self.assertDictEqual(ddict_d, self.d)
        self.assertTrue(ddict_d.d4 == 'End')
        self.assertDictEqual(ddict_d.d1, self.d['d1'])
        self.assertDictEqual(ddict_d.d1.d2, self.d['d1']['d2'])

    def test_missing_key(self):
        ddict_d = Ddict(self.d)
        self.assertTrue(ddict_d.d1.d4 is None)

    def test_muli_update(self):
        d = Ddict({"a": 1})
        d.update({"a": 2}, b=3, c=4)
        self.assertEqual(d.a, 2)
        self.assertEqual(d.b, 3)
        self.assertEqual(d.c, 4)

    def test_update(self):
        d = Ddict()
        try:
            d.update(1, a=1)
        except TypeError as e:
            self.assertIn("is not iterable", str(e))
        d.update(a=1, b=2)
        self.assertDictEqual(d, dict(a=1, b=2))

if __name__ == '__main__':
    unittest.main()
