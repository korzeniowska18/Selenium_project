## Projekt Selenium

![Selenium Web Driver](./image/images.jpg)

PRACA ZALICZENIOWA z automatyzacji funkcjonalnych aplikacji internetowych z użyciem Selenium Web Driver w Wyższej Szkole Bankowej we Wrocławiu.

Przygotowałam automatyczne testy dotyczące ważnych funkcjonalności internetowego sklepu zielarskiego "CENTRUMAMIS.PL" oraz wyszukiwanie w Google.

## Repozytorium zawiera cztery przypadki testowe wykonane z użyciem Selenium Web Driver:

* [Aktualizacja danych w profilu płatności użytkownika](#Aktualizacja-danych-w-profilu-płatności-użytkownika)
* [Wyszukiwanie w Google według słowa kluczowego](#[Wyszukiwanie-w-Google-według-słowa-kluczowego)
* [Wyszukiwanie produktu używając filtrów i dodawanie produktu do koszyka](#Wyszukiwanie-produktu-używając-filtrów-i-dodawanie-produktu-do-koszyka)
* [Poprawne i nieudane logowanie na konto użytkownika](#Poprawne-i-nieudane-logowanie-na-konto-użytkownika)

Testy, które wykonałam były oparte o przypadki testowe zawarte w folderze "Test Cases".

## Przypadki testowe wykonane z wykorzystaniem wzorca Page Object Pattern:

* [Wyszukiwanie w Google według słowa kluczowego](#[Wyszukiwanie-w-Google-według-słowa-kluczowego)
* [Wyszukiwanie produktu używając filtrów i dodawanie produktu do koszyka](#Wyszukiwanie-produktu-używając-filtrów-i-dodawanie-produktu-do-koszyka)

Folder "Requirements" zawiera wykorzystane i wymagane biblioteki Selenium do wykonania testów oraz ścieżki do Page Objects.

Każdy Test case zawiera nie tylko poszczególnie opisane kroki przypadku testowego oraz rzeczywiste i oczekiwane wyniki, wraz z podsumowaniem.


# Selenium_project

This project includes four Test Cases using Selenium Web Driver. 

In the folder "Test Cases" you can find every test case with details steps which were used during tests.
You can find also expected result and really result of every test case with summary about tests. 

In the folder "Test Cases with Page Objects" you can find my test cases about searching on the web page, also about adding product to the cart and assertion of the alert message. In these cases I used Page Objects with some parts of the case and that generally test case could be more compact. Every Page includes some function which we can to use more times in next cases. This is useful. 

Next test cases about Passed and Failed login on the web page of the store and update Billing Address for Account. Every test case includes Assertion which confirms that User logged successful or User could not login and appeared appropriate Error about Incorrect login details. Also confirmation about update data of the Account. 

Tests with Page Objects were done by using PyCharm 2019.3.3. Other tests by using Ubuntu 18.04.4 LTS

