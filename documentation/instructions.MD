# Instructions
## Accessing and launching the application

Applications releases can be found and downloaded by visiting
[List of Releases](https://github.com/miikara/landlord/releases) and choosing the first one on the top for the latest release. 

Two comman line commans are enough to launch the application

Install dependencies using:
```
poetry install
```
Start application using:
```
poetry run invoke start
```
## Creating an account and logging in

The application's starting screen is the login screen which allows a pre-existing user the login by providing his/her username and password:
 
<img src="https://raw.githubusercontent.com/miikara/landlord/master/documentation/pictures/login_screen.png">

When using the application for the first time, the user has to first create an account by clicking "Sign up" on the login screen. This opens the sign up screen where the user must select his/her unique username and password. The application will raise an error in case the username already exists.

<img src="https://raw.githubusercontent.com/miikara/landlord/master/documentation/pictures/signup_screen.png">

## Navigating the menu

The main menu is organised into a top pane and two sections named "Manage portfolio information" and "Portfolio statistics". The first section allows the user to add and modify stored information about his/her portfolio. The latter section enablees the user to get selected statistics about the whole portfolio or the an invidial unit.

<img src="https://raw.githubusercontent.com/miikara/landlord/master/documentation/pictures/menu_screen.png">

For example if the user wishes to insert a new unit, he/she should click on "Insert unit" and provide information on the screen that appears similar to the example below.

<img src="https://raw.githubusercontent.com/miikara/landlord/master/documentation/pictures/insert_units_screen.png">

Accessing unit level statistics works via clicking "Get unit level statistics" under "Portfolio statistics" section. Once the screen open the user will see the top unit on the list pre-selected. To access a specific unit's details the user must choose the unit on the list and click on "Show statistics" which will make the statistics appear on the bottom of the screen as in the picture below.

<img src="https://raw.githubusercontent.com/miikara/landlord/master/documentation/pictures/unit_level_statistics_screen.png">

The portfolio level statistics (time series for portfolio size and average occupancy rates) are accessed directly by clicking either "Graph portfolio unit amount" or "Graph portfolio occupancy". An example of the latter graph is below.

<img src="https://raw.githubusercontent.com/miikara/landlord/master/documentation/pictures/occupancy_window.png">