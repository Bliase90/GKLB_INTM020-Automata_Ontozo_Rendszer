# GKLB_INTM020-Automata_Ontozo_Rendszer
Projekt Feladat - Mikroelektromechanikai rendszerek (GKLB_INTM020)

########### Alapvető Információk ###########


----- A. Projekt Célja 
 
- A projekt arra irányul, hogy Raspberry PI használatával létrehozzunk egy automata öntöző rendszert.
- Ez az öntöző rendszer jelenlegi megvalosításában egy prototípus, ami kisebb cserepes szobanövények öntözésére szolgál.
- Jelenleg egyszerre csak 1db növény szerepel a megvalósításban.
- Különböző plusz alkatrészek "csapok", "szenzorok" segítségével alapul szolgálhat egy több növényt is ellátni képes, smart watering rendszerhez.

----- B. Szükséges Eszközök
|:sorszám:|db szám | Megnevezés | Link
|:-------------:|-------------|---------

- |:1:| 1db | Raspberry Pi 3 B+ |	[Link](https://www.amazon.de/-/en/Raspberry-1373331-Model-Motherboard-1GB/dp/B07BFH96M3/ref=sr_1_2?crid=MX10MM81RM3H&keywords=raspberry+pi+3b%2B&qid=1639915724&sprefix=raspberry+pi+3b%2B%2Caps%2C154&sr=8-2)|
- |:2:| 1db | 4 vonallal rendelkező Relés Panel |[Link](https://www.amazon.co.uk/dp/B0057OC5O8/ref=as_at?slotNum=3&ie=UTF8&linkCode=gs2&linkId=79128c0fb9efa41048a1490b5007a164&imprToken=8aetm8z5QJ4fvAjzwZJJ0g&creativeASIN=B0057OC5O8&tag=thecybome-21&creative=9325&camp=1789) |
- |:3:| 1db | 5V Elektro motoros kis méretű búvár szivattyú |[Link](https://www.amazon.co.uk/dp/B075JHL9CC/ref=as_at?slotNum=4&ie=UTF8&linkCode=gs4&linkId=bbb6764dfd57c0775e909dbad50ba711&imprToken=8aetm8z5QJ4fvAjzwZJJ0g&creativeASIN=B01LWQCXEL&tag=thecybome-21&creative=9325&camp=1789) |
- |:4:| 1db | SparkFun Soil Moisture Sensor (nedvesség érzékelő szenzor)|[Link](https://www.sparkfun.com/products/13637) |	
- |:5:| 1db | megfelelő hosszuságú flexibilis cső |[Link](https://www.invitalpet.hu/egyeb-osszekoto-elemek-csovek/invital-nagynyomasu-tomlo-10-meter?gclid=Cj0KCQiAzfuNBhCGARIsAD1nu-8OYM1Z07GT0zlfZfbim2RMiIW-HyBwdpWlgQM-I3xOAeZMvGaMxj0aAldlEALw_wcB) |
- |:6:| 1db | módosított külső 5V-os táp |[Link](https://tok-shop.hu/Halozati-tolto-adapter-5V-2000-mAh-USB-aljzat-microUSB-kabellel-Forever-feher-TC-01?gclid=Cj0KCQiAzfuNBhCGARIsAD1nu-9Ao94l3MWwPny78SevyivQl2zEzVdAjxRE2uBA29dB63XQ9SVi310aAhCAEALw_wcB) |
- |:7:| 1db | Potentiométer (10kOhm) |[Link](https://hu.farnell.com/tt-electronics-bi-technologies/p160kn-0qd15b10k/rotary-potentiometer-10kohm-16mm/dp/1782728?gclid=Cj0KCQiAzfuNBhCGARIsAD1nu--AaJTQH_BDBb4y6vAlDmec82BW9SiFY-LAyryHNM-SzqTraqJCZekaAlPdEALw_wcB&mckv=svgGb5eyG_dc|pcrid|513928396223|plid||kword||match||slid||product|1782728|pgrid|120785174877|ptaid|aud-910428655609:pla-327846201734|&CMP=KNC-GHU-GEN-SHOPPING-Whoop-14-April-2021&gross_price=true) |
- |:8:| 3db | LED (2db piros vagy sárga, és 1db Zöld) |[Link_Red_LED](https://hu.farnell.com/multicomp-pro/mp008247/led-red-4mcd-629nm-5mm/dp/3796273?st=led%20diode) |[Link_Green_LED](https://hu.farnell.com/multicomp-pro/mp008248/led-green-2-5mcd-572nm-5mm/dp/3796274?st=led%20diode)|
- |:9:| 1db | Ellenállás (180 Ohm) |<br>[Link:] https://hu.farnell.com/multicomp/mf25-180r/res-180r-1-250mw-axial-metal-film/dp/9341420 |
- |:10:| x db | forrasztáshoz, átkötéshez vezetékek |[Link Nem Elérhető]|
- |:11:| 1db | Forrasztó állomás  vagy forrasztó páka |[Link](https://www.tme.eu/hu/details/zd-8936/forrasztoallomasok/solder-peak/?brutto=1&currency=HUF&gclid=Cj0KCQiAzfuNBhCGARIsAD1nu-_ZVF3PJP1aslpOpv1mBtR50LPO2CGGuKM38K7FnIKPUt6Sswdix6oaAqurEALw_wcB) |
- |:12:| 1 tekercs | Forrasztó ón |[Link](https://www.forrasztastechnologia.hu/forrasz-anyagok/forraszto-on) |
- |:13:| 1db | kis méretű csillag csavarhúzó |[Link Nem Elérhető]|
