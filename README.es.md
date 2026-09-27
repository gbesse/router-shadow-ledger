# router-shadow-ledger

Mide el arrepentimiento de una política de enrutamiento con resultados contrafactuales aportados.

[Français](README.md) · [English](README.en.md) · [Español](README.es.md)

## Proyectos relacionados

- [Magpie — pasarela de múltiples proveedores](https://github.com/yetone/magpie)
- [openJiuwen model-router — enrutamiento de modelos](https://github.com/openJiuwen-ai/model-router)
- [model-swap-ci — comparación de un cambio fijo de modelo](https://github.com/gbesse/model-swap-ci)

Estos proyectos documentan la necesidad o cubren parte del problema. No se afirma ninguna afiliación ni integración con ellos.

## Inicio rápido

```bash
python3 tool.py demo
python3 tool.py check examples/requests.json
```

Python 3.11+; no external package required. / Python 3.11+ ; aucune dépendance externe. / Python 3.11+; sin dependencias externas.

## Alcance actual

El registro exige resultados contrafactuales observados para cada modelo comparado. Encuentra el coste mínimo entre resultados que cumplen límites de calidad y latencia; no infiere resultados ausentes.

## Pruebas

```bash
python3 -m unittest discover -s tests -v
```

## Licencia

MIT.
