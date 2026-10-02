# Labo dbt : où vont `description` et `config` des data tests

## Installation
    pip install dbt-duckdb
    python setup_db.py
    dbt build --profiles-dir .          # attendu : 2 WARN (statut vide, montant négatif)

## Lire les résultats
    dbt parse --profiles-dir .
    python -c "import json;m=json.load(open('target/manifest.json'));[print(k,v['config'].get('severity'),v['config'].get('tags'),v['config'].get('meta'),v.get('description')) for k,v in m['nodes'].items() if k.startswith('test.')]"

## Scénarios à rejouer (un changement à la fois, puis `dbt test --profiles-dir .`)
Défaut de dbt : severity = error (FAIL). Un WARN prouve donc qu'une config a été appliquée.
1. Singular : retire le config() du .sql et mets `severity: warn` dans tests/_schema.yml -> WARN (YAML accepté).
   Mets config() = error dans le .sql et `warn` en YAML -> FAIL (le SQL gagne).
2. Générique : précédence YAML instance > config() du bloc {% test %} > dbt_project.yml.
3. data_tests: en clé racine dans models/staging/_stg__models.yml (décommente, supprime tests/_schema.yml).
4. dbt_project.yml : décommente `data_tests: +severity: warn` (supprime les config() pour voir l'effet).
5. macros/schema.yml : `config: docs/meta` pris en compte ; `severity` sous macros est ignoré en silence.
6. Déplace macros/schema.yml vers tests/generic/_schema.yml : la description est quand même lue.

Note : dbt affiche un warning "number of arguments in the yaml for macro test_not_empty_string
does not match the jinja definition" : cause non élucidée, sans effet.
Testé avec dbt 1.12.5 + dbt-duckdb 1.11.0.
