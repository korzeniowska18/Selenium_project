I.Test Case - Registration with empty data

ID: 001

Title: Registration of the new user without input any required data on the shop web page.

Environment: Chrome version 80.0.3987.163, PyCharm 2019.3.3

Precondition: Open browser. The user is not logged.


Steps:

1. Open web page „https://centrumamis.pl/pl”
2. Click "Registartion"
3. No input any data, all fields are empty
4. Click "Registartion" button 
5. Appears the error about mistake during registartion
6. Click "Close"
7. Close browser

II.Test Case - Test Google Search

ID: 002

Title: Search in GOOGLE.COM using keyword and open first link

Environment: Chrome version 80.0.3987.163, PyCharm 2019.3.3

Precondition: Open browser. 

1.Open web page „https:google.com”
2.Click in the "SEARCH" field
3. Input keyword "APPLE" 
4. Click "SEARCH BUTTON"
5. Select first found link
6. Open this page
7. Get PAGE TITLE - "Apple(Polska)"
8. Assert PAGE TITLE
9. Confirm that assertion done correctly
10. Close browser





III.Test Case - Test Search Product

ID: 003

Title: Search and add the product to the cart on the web page of the shop CENTRUMAMIS.PL

Environment: Chrome version 80.0.3987.163, PyCharm 2019.3.3

Precondition: Open browser. The user is not logged.

1.Open web page „https://centrumamis.pl/pl”
2.Click in the "SEARCH" field
3. Input keyword "WAGA" 
4. Click "SEARCH BUTTON"
5. Select first found product
6. Add first found product in the cart
7. Get "ALERT MESSAGE ABOUT ADDING THE PRODUCT TO THE CART"(Alert message is: "Produkt dodany do koszyka.")
8. Confirm taht ALERT MESSAGE displayed correctly on the web page
9. Close browser



