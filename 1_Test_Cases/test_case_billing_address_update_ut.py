I.Test Case - Billing Address update for Account

ID: 001

Title: Billing Address update for Account on the web page of the store CENTRUMAMIS.PL

Environment: Chrome version 81.0.4044.138, Ubuntu 18.04.4 LTS
Precondition: Open browser. The user is not logged.

STEPS:

1. Open web page „https://centrumamis.pl/pl”
2. Open LOGIN PAGE by click on "ZALOGUJ SIĘ"
3. Input in E-MAIL field correct email
4. Input in PASSWORD field correct password
5. Click button "ZALOGUJ SIĘ"
6. Click tab "MOJE KONTO"
7. Click button "PRZEJDŹ DO EDYCJI ADRESÓW"
8. Click "EDIT" button 
9. Input in field "IMIĘ" FIRST NAME
10. Input in field "NAZWISKO" LAST NAME
11. Input in field "NAZWA FIRMY" COMPANY NAME
12. Input in field "TELEFON" PHONE NUMBER
13. Input in field "ULICA i NUMER DOMU" STREET AND HOUSE NUMBER
14. Input in field "KOD POCZTOWY" ZIP CODE
15. Input in field "MIASTO" CITY
16. Input in field "KRAJ" COUNTRY
17. Click "ZAPISZ" and save it
18. Assert appered alert message "Adres został zapisany." which confirms that address was saved

Result:

After input new address data in appropriate fields in Edit option appears alert with confirmation that updated data saved.
Alert message: "Adres został zapisany." Assertion confirmed it. 

Expected result(behaviour):

After input new address data in appropriate fields in Edit option all data saved correctly.
Appears alert with confirmation that updated data saved.  

Summary:

Option "Edit" for update billing address works correctly. 
