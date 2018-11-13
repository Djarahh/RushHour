# RushHour

qvdpost@gmail.com - 0634123112

Done:
+ rushhour.py werkt
+ main.py werkt
+ willekeurig algoritme werkt
+ 'grote moves' werkt

To do list:
+ visualisatie
+ wat gaan we opslaan uit elk algoritme en hoe visualiseren we dit?
+ won functie aanpassen zodat rode autotje een forced move maakt als de weg vrij is naar de uitgang

Exploration:
Upper Bound:
- Om mee te beginnen zeggen we dat er voor een spel van 6x6, 36 vakjes zijn die
kunnen worden ingevuld door auto's. Dus 36! als upperbound. 3.72 x 10^41.
In andere woorden: voor een bord van nxn, UB = n^2!
- Wanneer de we kijken naar de staat van de auto's op een bord van 6x6 en zo de
upperbound uitrekenen gaat dat als volgt:
De auto's zelf hebben voor lengte 2 een bewegingsvrijheid van 5, voor een
auto met lengte van 3 heeft een bewegingsvrijheid van 4. Afhankelijk van de
hoeveelheid auto's op het spelbord kun je de statespace uitrekenen:
(bewegingsvrijheid auto lengte 2)^aantal auto's lengte 2 * (bewegingsvrijheid
auto lengte 3)^aantal auto's lengte 3.
In andere woorden: voor een bord van lengte n met x auto's van lengte 2 en y auto's
met lengte 3. Wordt de UB = (n- 1)^x * (m-2)^y


update 05/11
1. move werkt! je kan de stukken op het board als volgt bewegen:
in de command line (< in je terminal)"MOVE coordinaten van beweegrichting car_id"
voorbeeld: MOVE 1,2 1
(als je alleen in x richting kan bewegen dan worden de x coordinaten vervangen door [][1, y], [2, y]])
2. bij het renderen van het board wordt nu de id van de juiste auto geprint.

update 04/11
Hoi!
ik heb een aantal kleine updates gemaakt.
1. als je het programma runt en op ENTER drukt zal een representatie van het
bord gemaakt worden.
2. autos en bord worden nu geladen
3. coordinaten nog niet helemaal handig geimplementeerd denk ik. Zijn nu lijsten
met integers (voorbeeld: [2,4]), zowel van het bord als van de autos.
4. begonnen met het implementeren van de move funtie: alleen nog goeie structuur
vinden voor commandos doorgeven (zie rushhour voor voorbeeld)
5. current_bord.py wordt nog niet gebruikt.
6. data in apparte file gedaan voor makkelijker overzicht.
7. kleine weizigingen in block, bord en car.

QUOTES:

Yara over Stan: hij heeft z'n appel en z'n peer door elkaar gehaald.
