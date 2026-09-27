"""Offline router regret from supplied, observed counterfactual outcomes."""
import json
import sys
from pathlib import Path


def check(data):
    findings = []
    rows = []
    for request in data['requests']:
        ceiling = request.get('latency_ceiling_ms', float('inf'))
        floor = request.get('quality_floor', 0)
        outcomes = {o['model']: o for o in request['outcomes']}
        chosen = request['chosen']
        if chosen not in outcomes:
            raise ValueError(f'{request["id"]}: chosen outcome missing')
        eligible = [o for o in outcomes.values() if o['quality'] >= floor and o['latency_ms'] <= ceiling]
        if not eligible:
            findings.append(f'{request["id"]}: no eligible observed outcome')
            continue
        # Cost is minimized among outcomes satisfying stated quality and latency constraints.
        best = min(eligible, key=lambda o: o['cost'])
        observed = outcomes[chosen]
        violates = observed['quality'] < floor or observed['latency_ms'] > ceiling
        regret = max(0, observed['cost'] - best['cost'])
        row = {'id': request['id'], 'segment': request['segment'], 'chosen': chosen,
               'best_observed_eligible': best['model'], 'cost_regret': round(regret, 4),
               'constraint_violation': violates}
        rows.append(row)
        if violates:
            findings.append(f'{request["id"]}: chosen outcome violates quality or latency constraint')
    average_regret = sum(r['cost_regret'] for r in rows) / len(rows) if rows else 0
    if average_regret > data.get('max_average_regret', float('inf')):
        findings.append(f'average cost regret {average_regret:.3f} exceeds threshold')
    by_segment = {}
    for row in rows:
        by_segment.setdefault(row['segment'], []).append(row)
    segments = {key: {'requests': len(value), 'average_regret': round(sum(r['cost_regret'] for r in value)/len(value), 4)} for key, value in by_segment.items()}
    return {'ok': not findings, 'average_cost_regret': round(average_regret, 4), 'segments': segments, 'requests': rows, 'findings': findings}


def main():
    if len(sys.argv) < 2 or sys.argv[1] not in ('demo', 'check'):
        raise SystemExit('usage: tool.py demo | check REQUESTS.json')
    path = Path(__file__).parent / 'examples/requests.json' if sys.argv[1] == 'demo' else Path(sys.argv[2])
    result = check(json.loads(path.read_text()))
    print(json.dumps(result, indent=2))
    return 0 if sys.argv[1] == 'demo' or result['ok'] else 1

if __name__ == '__main__':
    raise SystemExit(main())
