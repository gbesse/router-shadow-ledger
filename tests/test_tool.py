import copy
import json
import sys
import unittest
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tool import check, audit_magpie_group
DATA = json.loads((Path(__file__).resolve().parents[1]/'examples/requests.json').read_text())
MAGPIE = json.loads((Path(__file__).resolve().parents[1]/'examples/magpie-order-events.json').read_text())

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

    def test_magpie_order_violation(self):
        result = audit_magpie_group(MAGPIE)
        self.assertFalse(result['ok'])
        self.assertIn('order policy expected', str(result['findings']))

    def test_magpie_expected_fallback(self):
        data = copy.deepcopy(MAGPIE)
        data['events'][0]['chosen'] = 'vendor-a/strong'
        self.assertTrue(audit_magpie_group(data)['ok'])

    def test_magpie_smart_policy_not_inferred(self):
        data = copy.deepcopy(MAGPIE)
        data['group']['routing'] = 'smart'
        self.assertEqual(audit_magpie_group(data)['policy_unverified_events'], 2)
