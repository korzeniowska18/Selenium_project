II.Test Case - Passed and Failed Login to User Account

ID: 002

Title: Passed and Failed Login to User Account on the web page of the store CENTRUMAMIS.PL

Environment: Chrome version 81.0.4044.138, Ubuntu 18.04.4 LTS
Precondition: Open browser. The user is not logged.

Test Case №1 'TestLoginPassed'

STEPS:

1. Open web page „https://centrumamis.pl/pl”
2. Open LOGIN PAGE by click on "ZALOGUJ SIĘ"
3. Input in E-MAIL field correct email
4. Input in PASSWORD field correct password
5. Click button "ZALOGUJ SIĘ"
6. Confirm by assertion that User Logged because appeared tab "WYLOGUJ"
7. Confirm by assertion that User Logged because appeared greeting "Witaj {USERNAME}"

Result:

After login with correct email and password User logged to Account correctly.
Appeared greeting "Witaj {USERNAME}" and tab "WYLOGUJ". Assertion confirmed that User logged.

Expected result(behaviour):

After login with correct email and password User logged to Account correctly. 
Also should appear appropriate greeting for User. 

Summary:

Done Login to Account with correct email and password successfully. 
Appeared appropriate confirmation such as greeting "Witaj {USERNAME}" and tab "WYLOGUJ".

Test Case №2 'testLoginFailedWrongEmail'

STEPS:

1. Open web page „https://centrumamis.pl/pl”
2. Open LOGIN PAGE by click on "ZALOGUJ SIĘ"
3. Input in E-MAIL field email without "@"
4. Input in PASSWORD field correct password
5. Click button "ZALOGUJ SIĘ"
6. Confirm by assertion that User not Logged because appeared error message: "Niepoprawne dane logowania."

Result:

After login with incorrect email without "@" and correct password User not logged to Account. Login failed.
Appeared error message: "Niepoprawne dane logowania." Assertion confirmed that User not logged.

Expected result(behaviour):

After login with incorrect email without "@" and correct password Login should be failed.
Also should appear appropriate error message about wrong login details. 

Summary:

Login with incorrect email without "@" and correct password failed. 
Appeared error message about wrong login details. 
This is appropriate behavior but would be better if error will be with more details.
When error will indicate what exactly is wrong. 
For example: The email address that you've entered does not match any account. Please create Account.
This could be more usefull for User. 

Test Case №3 'testLoginFailedNotRegisteredEmail'

STEPS:

1. Open web page „https://centrumamis.pl/pl”
2. Open LOGIN PAGE by click on "ZALOGUJ SIĘ"
3. Input in E-MAIL field wrong email which was not registered on this page and is not really
4. Input in PASSWORD field correct password
5. Click button "ZALOGUJ SIĘ"
6. Confirm by assertion that User not Logged because appeared error message: "Niepoprawne dane logowania."

Result:

After login with wrong email which was not registered on this page also is not really and correct password User not logged to Account. 
Login failed. Appeared error message: "Niepoprawne dane logowania." Assertion confirmed that User not logged.

Expected result(behaviour):

After login with wrong email which was not registered on this page also is not really and correct password Login should be failed.
Also should appear appropriate error message about wrong login details. 

Summary:

Login with wrong email which was not registered on this page also is not really and correct password failed. 
Appeared error message about wrong login details. 
This is appropriate behavior but would be better if error will be with more details.
When error will indicate what exactly is wrong. 
For example: The email address that you've entered does not match any account. Please create Account.
This could be more usefull for User. 

Test Case №4 'testLoginFailedWrongPassword'

STEPS:

1. Open web page „https://centrumamis.pl/pl”
2. Open LOGIN PAGE by click on "ZALOGUJ SIĘ"
3. Input in E-MAIL field correct email
4. Input in PASSWORD field wrong password
5. Click button "ZALOGUJ SIĘ"
6. Confirm by assertion that User not Logged because appeared error message: "Niepoprawne dane logowania."

Result:

After login with correct email and wrong password User not logged to Account. Login failed.
Appeared error message: "Niepoprawne dane logowania." Assertion confirmed that User not logged.

Expected result(behaviour):

After login with correct email and wrong password Login should be failed.
Also should appear appropriate error message about wrong login details. 

Summary:

Login with correct email and wrong password failed. 
Appeared error message about wrong login details. 
This is appropriate behavior but would be better if error will be with more details.
When error will indicate what exactly is wrong. 
For example: "The password that you've entered is incorrect. Forgot password?" Also add link for reset password in this error.
This could be more usefull for User. 
