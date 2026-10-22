# temporal-leakage-split

## Français

Séparer les jeux temporels en respectant les lignées et les délais.

Données fictives ; aucun accès réseau ni secret requis.

```sh
python -m temporal_leakage_split examples/demo.json --lang fr
python -m unittest discover -s tests -v
```

### Méthode et différence

Découpage temporel avec disponibilité réelle des données/labels, embargo et composantes de lignées partagées. Les liens transitifs vers le test purgent seulement les observations d’entraînement ; aucune donnée future n’est déplacée dans le passé.

### Limites

Graphe et dates déclarés, 10 000 lignes maximum ; pas de détection sémantique de doublons cachés, de calibration ou de garantie statistique.

### Validation

Tests de domaine, cas limites et interface FR/EN/ES. La CI teste Python 3.11/3.13 et exécute la wheel installée hors du checkout. JSON conserve les identifiants techniques et les données fournis. Erreur d’entrée : code de sortie 2.

## English

Split temporal datasets respecting lineages and delays.

Synthetic data; no network access or secret required.

```sh
python -m temporal_leakage_split examples/demo.json --lang en
python -m unittest discover -s tests -v
```

### Method and difference

Temporal split respects actual data/label availability, embargo and shared-lineage components. Transitive links to test purge training observations only; future data is never moved into the past.

### Limits

Declared graph and timestamps, at most 10,000 rows; no semantic detection of hidden duplicates, calibration or statistical guarantee.

### Validation

Domain tests, boundary cases and FR/EN/ES interface. CI tests Python 3.11/3.13 and runs the installed wheel outside the checkout. JSON preserves technical identifiers and supplied data. Invalid input exits with code 2.

## Español

Dividir datos temporales respetando linajes y retrasos.

Datos sintéticos; no requiere red ni secretos.

```sh
python -m temporal_leakage_split examples/demo.json --lang es
python -m unittest discover -s tests -v
```

### Método y diferencia

División temporal con disponibilidad real de datos/etiquetas, embargo y componentes de linaje compartido. Los enlaces transitivos a test purgan solo entrenamiento; nunca trasladan datos futuros al pasado.

### Límites

Grafo y tiempos declarados, máximo 10.000 filas; sin detección semántica de duplicados ocultos, calibración ni garantía estadística.

### Validación

Pruebas de dominio, casos límite e interfaz FR/EN/ES. CI prueba Python 3.11/3.13 y ejecuta la wheel instalada fuera del repositorio. JSON conserva identificadores técnicos y datos proporcionados. Entrada inválida termina con código 2.

## Sources / Fuentes

- https://github.com/gbesse/autonomy-meter
- https://csrc.nist.gov/projects/automated-combinatorial-testing-for-software
