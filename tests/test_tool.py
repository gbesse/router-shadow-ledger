import copy
import json
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tool import check
DATA = json.loads((Path(__file__).resolve().parents[1]/'examples/requests.json').read_text())

class RouterTests(unittest.TestCase):
    def test_cheap_route_violates_latency(self):
        result = check(DATA)
        self.assertFalse(result['ok'])
        self.assertTrue(result['requests'][1]['constraint_violation'])

    def test_eligible_route_passes(self):
        data = copy.deepcopy(DATA)
        data['requests'][1]['chosen'] = 'fast-safe'
        self.assertTrue(check(data)['ok'])

    def test_missing_counterfactual_rejected(self):
        data = copy.deepcopy(DATA)
        data['requests'][0]['outcomes'] = []
        with self.assertRaises(ValueError):
            check(data)
