# Vežbe - Računarske mreže

> **Note**
> 
> All instructions and materials are written in Serbian.

## Zadaci sa radionice

1.zadatak: Napisati TCP server i TCP klijenta sa sledećim funkcionalnostima:
 - TCP server: Prima konekcije sve dok ne prekinemo izvršavanje programa. Kada primi konekciju od strane nekog klijenta, šalje mu poruku, a zatim zatvara konekciju.
 - TCP klijent: Uspostavlja vezu sa serverom, a zatim prima poruku od servera i ispisije je na standardni izlaz.
 
2.zadatak: Napisati TCP server i TCP klijenta sa sledećim funkcionalnostima:
 - TCP server: Prima konekcije sve dok ne prekinemo izvršavanje programa. Kada primi konekciju od strane nekog klijenta, čeka da klijent pošalje poruku, a zatim mu šalje potvrdu o primljenoj poruci i zatvara konekciju.
 - TCP klijent: Uspostavlja vezu sa serverom. Sa standarnog ulaza učitava poruku koja će se poslati serveru. Nakon što se unese tekst poruke, poruka se šalje. Klijent zatim čeka da primi potvrdu o potvrdi i ispisuje je na standardni izlaz.

3.zadatak: Napisati TCP server i TCP klijenta sa sledećim funkcionalnostima:
 - TCP server: Prima konekcije sve dok ne prekinemo izvršavanje programa. Kada primi konekciju od strane nekog klijenta, bez blokiranja čeka da klijent pošalje poruku, a zatim mu šalje potvrdu o primljenoj poruci i zatvara konekciju.
 - TCP klijent: Uspostavlja vezu sa serverom. Sa standarnog ulaza učitava poruku koja će se poslati serveru. Nakon što se unese tekst poruke, poruka se šalje. Klijent zatim čeka da primi potvrdu o potvrdi i ispisuje je na standardni izlaz.
 
4.zadatak: Napisati TCP server i TCP klijenta sa sledećim funkcionalnostima:
 - TCP server: Prima konekcije sve dok ne prekinemo izvršavanje programa. Kada primi konekciju od strane nekog klijenta, bez blokiranja čeka da korisnik pošalje sliku i njen naslov. Kada server primi celu sliku, ona se prikazuje.
 - TCP klijent: Uspostavlja vezu sa serverom. Sa standarnog ulaza učitava putanju slike koja će se poslati, kao i njen naslov. Slika se učitava sa fajl sistema. Slika i naslov se šalju serveru.
