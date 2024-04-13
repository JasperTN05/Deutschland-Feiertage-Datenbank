# Deutsche Feiertage Datenbank
## Intention:
Auf der Suche nach historischen deutschen Feiertagsdaten für eine BI Analyse wurde ich sehr davon überrascht, dass nach mittellange Suche nirgendswo im Internet Feiertagsdaten für alle Bundesländer zu finden waren, die weiter als 2021 zurückgehen. Daher musste ich einen anderen Weg finden, um an diese Daten zu kommen und möchte mit diesen Projekt, anderen Menschen ein bisschen Zeit sparen, so dass sie selbst schnell an Daten zu alten und zukünftigen Feiertagen gelangen.

## Beschreibung:
Dieses Projekt stellt eine umfassende Datenbank aller deutschen Feiertage von 2000 bis 2030 in einem leicht zugänglichen CSV-Format bereit. Die Datenbank umfasst alle Feiertage für jedes Bundesland in Deutschland. Die Datenbank wird mithilfe einer öffentlich zugänglichen API erstellt, die Feiertagsinformationen für verschiedene Bundesländer und Jahre basierend auf folgendem Wikipedia Eintrag (https://de.wikipedia.org/wiki/Gesetzliche_Feiertage_in_Deutschland) bereitstellt. Der Python-Code in diesem Projekt ruft die API auf, sammelt die Daten, führt sie logisch zusammen und speichert sie in einem CSV-Format ab.

## Nutzung der API:
Die API (https://feiertage-api.de/) bietet einen kostenlosen Webservice zur Abfrage von Feiertagen in Deutschland. Sie unterstützt verschiedene Parameter, darunter das Jahr und das Bundesland, und liefert die entsprechenden Feiertagsdaten im JSON-Format zurück. Allerdings können immer nur Daten für ein Bundesland und ein Jahr aufeinmal abgerufen werden.

## Projektstruktur:
Python-Skript: Der Python-Code nutzt die requests-Bibliothek, um die API aufzurufen, und die pandas-Bibliothek, um die Daten zu verarbeiten, zu entwickeln, zusammenzuführen und in ein CSV-Format zu konvertieren.
CSV-Datei: Die generierte CSV-Datei enthält alle Feiertagsinformationen, einschließlich des Feiertagsnamens, des Datums und eventueller Hinweise, für die Jahre 2000 bis 2030. Die Daten sind nach Bundesländern und Jahren strukturiert.

## Hinweise:
Die API wird kostenlos angeboten und kann auch für kommerzielle Zwecke verwendet werden.
Der Code kann angepasst werden, um die Jahreszahlen zu ändern oder sich auf bestimmte Bundesländer zu fokussieren.
Wenn sich ein Wert in der Spalte Hinweis befindet, handelt es sich bei dem Feiertag, um einen Tag der nur in bestimmten Regionen des Bundeslandes gefeiert wird (z.B. Augsburg oder nur in Schulen). Um welche Region es sich in solchen Fällen genau handelt steht dann in der Hinweis Spalte.

## Bundesländer Abkürungen:
- NATIONAL Bundesweite Feiertage
- BW	Baden-Württemberg 
- BY	Bayern
- BE	Berlin
- BB	Brandenburg
- HB	Bremen
- HH	Hamburg
- HE	Hessen
- MV  Mecklenburg-Vorpommern
- NI	Niedersachsen
- NW	Nordrhein-Westfalen
- RP	Rheinland Pfalz
- SL	Saarland
- SN	Sachsen
- ST	Sachsen	Sachen-Anhalt
- SH	Schleswig Holstein
- TH Thüringen

## Wann und warum kann dieses Projekt nützlich sein?
1. Umfassende Datenabdeckung:
Die Datenbank enthält Informationen zu allen Feiertagen von 2000 bis 2030 für alle Bundesländer Deutschlands. Dies ermöglicht eine vollständige und zuverlässige Analyse vergangener und zukünftiger Feiertage.

2. Vielseitige Anwendungsmöglichkeiten:
Die Datenbank kann in verschiedenen Anwendungen und Projekten verwendet werden, darunter:
- Erstellung von Kalendern und Planungstools
- Integration in Unternehmens- und Schulplanungssysteme
- Analyse von Feiertagstrends und -mustern
- Entwicklung von Anwendungen für die Ferienplanung und Feiertagsinformationen

3. Leichte Integration:
Die Daten sind im CSV-Format verfügbar, was eine einfache Integration in verschiedene Programmiersprachen und Anwendungen ermöglicht. Dadurch können Entwickler und Analysten die Feiertagsdaten problemlos in ihre Projekte einbinden.

## Ausführung
- Entweder kann die CSV-Datei aus diesem Repository (mit Daten von 2000-2030) direkt heruntergeladen und benutzt werden oder der Code kann abgeändert werden und so eine neue csv generiert werden, um sich auf andere Zeiträume und bestimmte Bundesländer zu fokussieren.
- Für letzteres müssen alle Python Biblitheken aus der requirements.txt Datei im Environment installiert sein.
- Zusätzlich können - wenn benötigt - im Script "feiertage_fetch" die "years" und "states" Listen auf die benötigten Informationen ergänzt oder gekürzt werden.
- Danach muss das Script nur noch einmal ausgeführt werden und schon kann mit den neuen Daten analysiert werden :) 
