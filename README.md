# RushHour

Done:
+ rushhour.py werkt
+ main.py werkt
+ willekeurig algoritme werkt
+ 'grote moves' werkt
+ visualisatie is af
+ won functie aanpassen zodat rode autotje een forced move maakt als de weg vrij is naar de uitgang

To do list:

+ importeren met een init.py bestand ipv met sys.path.append(blabla)
+ niet meer rushhour.py runnen, maar alles vanuit main.py

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
