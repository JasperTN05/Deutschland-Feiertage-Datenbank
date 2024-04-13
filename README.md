# Projektname: Deutsche Feiertage Datenbank
## Beschreibung:
Dieses Projekt erstellt eine umfassende Datenbank aller deutschen Feiertage von 2000 bis 2030. Die Datenbank wird mithilfe einer öffentlich zugänglichen API erstellt, die Feiertagsinformationen für verschiedene Bundesländer und Jahre bereitstellt. Der Python-Code in diesem Projekt ruft die API auf, sammelt die Daten und speichert sie in einem CSV-Format ab.

## Nutzung der API:
Die API (https://feiertage-api.de/) bietet einen kostenlosen Webservice zur Abfrage von Feiertagen in Deutschland. Sie unterstützt verschiedene Parameter, darunter das Jahr und das Bundesland, und liefert die entsprechenden Feiertagsdaten im JSON-Format zurück.

## Projektstruktur:
Python-Skript: Der Python-Code nutzt die requests-Bibliothek, um die API aufzurufen, und die pandas-Bibliothek, um die Daten zu verarbeiten, zusammenzuführen und in ein CSV-Format zu konvertieren.
CSV-Datei: Die generierte CSV-Datei enthält alle Feiertagsinformationen, einschließlich des Feiertagsnamens, des Datums und eventueller Hinweise, für die Jahre 2000 bis 2030. Die Daten sind nach Bundesländern und Jahren strukturiert.

## Anleitung zur Verwendung:
Stellen Sie sicher, dass Python installiert ist.
Führen Sie das Python-Skript aus. Dieses ruft automatisch die API auf, sammelt die Daten und speichert sie in einer CSV-Datei.
Die generierte CSV-Datei kann in verschiedenen Anwendungen und Datenbanken verwendet werden, um Feiertagsdaten für Deutschland zu analysieren und zu nutzen.

## Hinweise:
Die API wird kostenlos angeboten und kann auch für kommerzielle Zwecke verwendet werden.
Der Code kann angepasst werden, um die Jahreszahlen zu ändern oder sich auf bestimmte Bundesländer zu fokussieren

## Bundesländer Abkürungen:
- NATIONAL - Bundesweite Feiertage
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
