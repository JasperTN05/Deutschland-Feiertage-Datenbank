# Deutsche Feiertage Datenbank
## Beschreibung:
Dieses Projekt stellt eine umfassende Datenbank aller deutschen Feiertage von 2000 bis 2030 in einem leicht zugänglichen CSV-Format bereit. Die Datenbank umfasst alle Feiertage für jedes Bundesland in Deutschland. Die Datenbank wird mithilfe einer öffentlich zugänglichen API erstellt, die Feiertagsinformationen für verschiedene Bundesländer und Jahre basierend auf folgendem Wikipedia Eintrag (https://de.wikipedia.org/wiki/Gesetzliche_Feiertage_in_Deutschland) bereitstellt. Der Python-Code in diesem Projekt ruft die API auf, sammelt die Daten, führt sie logisch zusammen und speichert sie in einem CSV-Format ab.

## Nutzung der API:
Die API (https://feiertage-api.de/) bietet einen kostenlosen Webservice zur Abfrage von Feiertagen in Deutschland. Sie unterstützt verschiedene Parameter, darunter das Jahr und das Bundesland, und liefert die entsprechenden Feiertagsdaten im JSON-Format zurück. Allerdings können immer nur Daten für ein Bundesland und ein Jahr aufeinmal abgerufen werden.

## Projektstruktur:
Der Python-Code nutzt die requests-Bibliothek, um die API aufzurufen, und die pandas-Bibliothek, um die Daten zu verarbeiten, zu entwickeln, zusammenzuführen und in ein CSV-Format zu konvertieren.
CSV-Datei: Die generierte CSV-Datei enthält alle Feiertagsinformationen, einschließlich des Feiertagsnamens, des Datums und eventueller Hinweise, für die Jahre 2000 bis 2030. Die Daten sind nach Bundesländern und Jahren strukturiert.

## Hinweise:
Die API wird kostenlos angeboten und kann auch für kommerzielle Zwecke verwendet werden.
Der Code kann angepasst werden, um die Jahreszahlen zu ändern oder sich auf bestimmte Bundesländer zu fokussieren.
Wenn sich ein Wert in der Spalte Hinweis befindet, handelt es sich bei dem Feiertag, um einen Tag der nur in bestimmten Regionen des Bundeslandes gefeiert wird (z.B. Augsburg oder nur in Schulen). Um welche Region es sich in solchen Fällen genau handelt steht dann in der Hinweis Spalte.

## Ausführung
- Entweder kann die CSV-Datei aus diesem Repository (mit Daten von 2000-2030) direkt heruntergeladen und benutzt werden oder der Code kann abgeändert werden und so eine neue csv generiert werden, um sich auf andere Zeiträume und bestimmte Bundesländer zu fokussieren.
- Für letzteres müssen alle Python Biblitheken aus der requirements.txt Datei im Environment (pip install -r requirements.txt ) installiert sein.
- Zusätzlich können - wenn benötigt - im Script "feiertage_fetch" die "years" und "states" Listen auf die benötigten Informationen ergänzt oder gekürzt werden.
- Danach muss das Script nur noch einmal ausgeführt werden (python feiertage_fetch.py) und schon kann mit den neuen Daten analysiert werden :) 
