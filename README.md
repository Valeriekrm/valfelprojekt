<H1>SPAMHINATOR</H1>
Dieser Spamfilter wurde im Rahmen eines DHBW-Projektes, für Neue Konzepte, ein Modul des Kurses WWI15AMB entwickelt. 
Dieser Spamfilter soll maximal im Privaten genutzt werden. 
Verbesserungen sind möglich.

Die Hauptdatei ist FertigesProjektKrommMäder.py
Der Spamfilter wurde in Python entwickelt mit dem Hintergrund dessen, dass zum einen die Wahl der Programmiersprache frei war und zum anderen nützliche Packages bereits vorhanden waren, wodurch umständliche Entwicklungen, besonders die benötigten Algorithmen betreffend, nicht notwendig waren. Weitere vorhandene Dateien sind klasse.txt, welche sogenannte classifier beinhaltet. Dieses sind einzelne Wörter welche auf Spam-Emails hinweisen. Weiterhin gibt es im MeineHam und MeineSpam Ordner entsprechende Training- und Testsets zum einspeisen des classifiers. Die Auswahl 

Der angesprochene Algorithmus ist der NaiveBayes Algorithmus. Dieser ordnet, zumindest in Bezug auf Emails die ausgewählten Mails anhand der Trefferzahlen (Statistiken) in Ham (Kein Spam) oder Spam. 

Zur Nutzung dieses Codes müssen zuvor einige Anpassungen am Code erfolgen. Besonders die Pfade müssen angepasst werden. Um den Spamfilter individueller zu gestalten können die genutzten Testsets um eigene Mails erweitert werden. Diese sollten das Dateiformat .txt oder .rtf benutzen. Andere Formate könnten eventuell nicht erkannt werden.
Weiterhin kann durch den Originalcode nur Gmail verwendet werden. Die API wurde nicht eingebunden, da sie äußerst viele Fehlermeldungen, welche nicht auf Dauer behoben werden konnte ausgeworfen hat. Die hier genutzte Lösung ist für den Privatzweck jedoch mehr als ausreichend. 

Um den Spamfilter erfolgreich nutzen zu können muss Python 3 installiert werden. Ebenso ein Editor für Python da die Datei bearbeitet werden muss. Zu empfehlen ist Idle. Falls bereits Python installiert ist sollte ein Upgrade durchgeführt werden.

Für den Bayer Spamfilter mittels Python werden im Normalfall Sklearn oder NLTK genutzt. Hier wurde NLTK genutzt.

Sollte es nicht ausführbar sein muss die Python Version überprüft werden.

Zusätzlich wurde im Rahmen des Projektes ein Dockerfile erstellt.

Zu beachten ist, dass die Sets lediglich beim erstmaligen Gebrauch genutzt werden müssen. Im Anschluss kann der Code zum initialisieren auskommentiert werden. Jedoch sollte der Code, welcher die Datei klasse.txt aufruft nicht auskommentiert werden, da andernfalls keine Spam oder Ham Einordnung stattfinden kann.

<H2>Anleitung</H2>

Die einfachste Nutzung dieses Spamfilters ist die Ausführungs mittels eines Editors, z.B. Idle. 
Andernfalls kann es ebenfalls durch Docker ausgeführt werden.

Zunächst muss dafür Docker installiert werden. Sämtliche Dateien, inklusive des Dockerfile sollen bitte in einen Ordner lokal heruntergeladen werden. 

Anschließend wird mittels de Dockerfiles ein Dockerimage erstellt. Dazu muss zunächst das Terminal geöffnet werden, anschließend der Ordner mittels 'cd' ausgewählt werden und folgender Befehl eingegeben werden:

  <p align="center">docker build -t <deine namensgebung>:<versionsnummer> .<p align="center">
  
  <p align="center">Bsp: docker build -t meinimage:1.0 .<p align="center">
  
Sollte es nicht funktionieren bitte folgenden Befehl ausführen und den oberen nochmals ausführen:

  <p align="center">docker pull python3 (oder python)<p align="center">
  
Nach erfolgreichem erstellen des Images kann ein Container erstellt und zum laufen gebracht werden.
Hierzu folgende Befehle ausführen:

  <p align="center">docker run --name <mein toller containername> -p <>:<> <deine namensgebung>:<versionsnummer> (Vgl. oben)<p align="center">
  
  <p align="center">Bsp: docker run --name containername -p 80:80 meinimage:1.0<p align="center">

Um die Ausführung des Containers zu beenden kann folgender Befehl genutzt werden:

  <p align="center">docker stop <mein toller containername><p align="center">
  
Und für die Löschung des Container:

  <p align="center">docker rm <mein toller containername><p align="center">
