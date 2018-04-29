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

Zu beachten ist, dass die Sets lediglich beim erstmaligen gebrauch genutzt werden müssen. Im Anschluss kann der Code zum initialisieren auskommentiert werden. Jedoch sollte der Code, welcher die Datei klasse.txt aufruft nicht auskommentiert werden. 
