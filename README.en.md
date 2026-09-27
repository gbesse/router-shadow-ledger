# router-shadow-ledger

Measures routing-policy regret using supplied counterfactual outcomes.

[Français](README.md) · [English](README.en.md) · [Español](README.es.md)

## Related projects

- [Magpie — multi-provider gateway](https://github.com/yetone/magpie)
- [openJiuwen model-router — model routing](https://github.com/openJiuwen-ai/model-router)
- [model-swap-ci — fixed model-swap comparison](https://github.com/gbesse/model-swap-ci)

These projects document the need or cover part of the problem. No affiliation or integration with them is claimed.

## Quick start

```bash
python3 tool.py demo
python3 tool.py check examples/requests.json
```

Python 3.11+; no external package required. / Python 3.11+ ; aucune dépendance externe. / Python 3.11+; sin dependencias externas.

## Current scope

The ledger requires observed counterfactual outcomes for each compared model. It finds minimum cost among outcomes satisfying quality and latency limits; it does not infer missing outcomes.

## Tests

```bash
python3 -m unittest discover -s tests -v
```

## License

MIT.
