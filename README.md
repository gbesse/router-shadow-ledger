# router-shadow-ledger

Mesure le regret d’une politique de routage sur des résultats contrefactuels fournis.

[Français](README.md) · [English](README.en.md) · [Español](README.es.md)

## Projets voisins

- [Magpie — passerelle multi-fournisseurs](https://github.com/yetone/magpie)
- [openJiuwen model-router — routage de modèles](https://github.com/openJiuwen-ai/model-router)
- [model-swap-ci — comparaison d’un swap fixe](https://github.com/gbesse/model-swap-ci)

Ces projets documentent le besoin ou couvrent une partie du problème. Aucun lien d’affiliation ni intégration avec eux n’est revendiqué.

## Démarrer

```bash
python3 tool.py demo
python3 tool.py check examples/requests.json
```

Python 3.11+; no external package required. / Python 3.11+ ; aucune dépendance externe. / Python 3.11+; sin dependencias externas.

## Portée actuelle

Le journal exige des résultats contrefactuels observés pour chaque modèle comparé. Il mesure le coût minimal parmi les résultats respectant les seuils de qualité et latence ; il ne devine pas les résultats manquants.

## Tests

```bash
python3 -m unittest discover -s tests -v
```

## Licence

MIT.
