## Projekt Selenium

![Selenium Web Driver](./image/images.jpg)

PRACA ZALICZENIOWA z automatyzacji funkcjonalnych aplikacji internetowych z użyciem Selenium Web Driver w Wyższej Szkole Bankowej we Wrocławiu.

Przygotowałam automatyczne testy dotyczące ważnych funkcjonalności internetowego sklepu zielarskiego "CENTRUMAMIS.PL" oraz wyszukiwanie w Google.

## Repozytorium zawiera cztery przypadki testowe wykonane z użyciem Selenium Web Driver:

* [Aktualizacja danych w profilu płatności użytkownika](#Aktualizacja-danych-w-profilu-płatności-użytkownika)
* [Poprawne i nieudane logowanie na konto użytkownika](#Poprawne-i-nieudane-logowanie-na-konto-użytkownika)
* [Wyszukiwanie produktu używając filtrów i dodawanie produktu do koszyka](#Wyszukiwanie-produktu-używając-filtrów-i-dodawanie-produktu-do-koszyka)
* [Wyszukiwanie w Google według słowa kluczowego](#[Wyszukiwanie-w-Google-według-słowa-kluczowego)

Testy, które wykonałam były oparte o przypadki testowe zawarte w folderze "Test Cases".

## Przypadki testowe wykonane z wykorzystaniem wzorca Page Object Pattern:

* [Wyszukiwanie produktu używając filtrów i dodawanie produktu do koszyka](#Wyszukiwanie-produktu-używając-filtrów-i-dodawanie-produktu-do-koszyka)
* [Wyszukiwanie w Google według słowa kluczowego](#[Wyszukiwanie-w-Google-według-słowa-kluczowego)


Folder "Requirements" zawiera wykorzystane i wymagane biblioteki Selenium do wykonania testów oraz ścieżki do Page Objects.

Każdy Test case zawiera nie tylko poszczególnie opisane kroki przypadku testowego oraz rzeczywiste i oczekiwane wyniki, wraz z podsumowaniem.


## Przed uruchamieniem testu przygotowujemy środowisko:
```
$ pip3 --version
$ sudo apt install python3-pip
```

Pakiet Selenium do współpracy z przeglądarką potrzebuje także sterowników
```
Linki do wybranych sterowników:
```
* [Chrome: https://sites.google.com/a/chromium.org/chromedriver/downloads](https://sites.google.com/a/chromium.org/chromedriver/downloads)
* [Opera: https://github.com/operasoftware/operachromiumdriver/releases](https://github.com/operasoftware/operachromiumdriver/releases)
* [Firefox: https://github.com/mozilla/geckodriver/releases](Firefox: https://github.com/mozilla/geckodriver/releases)
* [Safari: https://webkit.org/blog/6900/webdriver-support-in-safari-10/](https://webkit.org/blog/6900/webdriver-support-in-safari-10/)
* [Internet Explorer:(Windows)https://selenium-release.storage.googleapis.com/index.html](https://selenium-release.storage.googleapis.com/index.html)
```(
• Firefox korzysta ze sterownika o nazwie geckodriver. 
Po ściągnięciu archiwum dostosowanego do architektury naszego procesora oraz systemu operacyjnego,
rozpakowujemy je:

$ tar -xvf geckodriver-v0.26.0-linux64.tar.gz

Następnie przenosimy rozpakowany plik do katalogu /usr/local/bin/ :

$ mv geckodriver /usr/local/bin
```
## Testy uruchomiamy za pomocą komendy:
```
$ python3 NAZWA_PLIKU_Z_TESTEM.py
```
# Selenium_project

This project includes four Test Cases using Selenium Web Driver. 

In the folder "Test Cases" you can find every test case with details steps which were used during tests.
You can find also expected result and really result of every test case with summary about tests. 

In the folder "Test Cases with Page Objects" you can find my test cases about searching on the web page, also about adding product to the cart and assertion of the alert message. In these cases I used Page Objects with some parts of the case and that generally test case could be more compact. Every Page includes some function which we can to use more times in next cases. This is useful. 

Next test cases about Passed and Failed login on the web page of the store and update Billing Address for Account. Every test case includes Assertion which confirms that User logged successful or User could not login and appeared appropriate Error about Incorrect login details. Also confirmation about update data of the Account. 

Tests with Page Objects were done by using PyCharm 2019.3.3. Other tests by using Ubuntu 18.04.4 LTS

