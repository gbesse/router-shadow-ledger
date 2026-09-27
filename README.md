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

## Démo liée à Magpie

Le second contrôle utilise une configuration de groupe et des observations de routage fournies par l’utilisateur. Pour la politique [`routing=order`, `stays=off` de Magpie](https://github.com/yetone/magpie#routing-groups), il vérifie que le premier modèle disponible a été choisi :

```bash
python3 tool.py magpie-demo
python3 tool.py audit-magpie examples/magpie-order-events.json
```

La fixture est synthétique ; aucun journal Magpie ni secret local n’est lu. Pour `smart`, `usage`, `rotate` ou une conversation épinglée, le rapport indique les événements dont la politique n’a pas pu être vérifiée, sans inférer les quotas manquants.

## Tests

```bash
python3 -m unittest discover -s tests -v
```

## Licence

MIT.
