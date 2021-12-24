# Requirements
## Application description

The purpose of the application is to allow landlords to keep track of their operations and properties on the market.

## Functional capabilities
User not logged in:
* User can create a username and password TEHTY
    * Username has to be unique
    * Password has a minimum length of five characters
* User can log in
    * A notification is issued when a username doesn't exists
    * A notification is issued when password is incorrect

User logged in:
* User can insert new listings, units (properties owned), lease contracts and charges
    * Details include compulsory fields (such as address of unit) and optional fields
* User can add a new rent level to existing lease due to intra-contact price change
* User can mark a unit as sold on a particular date which will remove it from list of properties
* User can see currently held properties using "get unit level statistics" and retrieve unit-level KPIs by selecting a unit.
    * KPIs for units include
        * Current tenant
        * Current cap rate as: (rent - charges)/ tax-inclusive purchase price
        * Current 12-month net operating income as rent - charges
* User can retrieve time series graphs for
    * Total portfolio size
    * Total portfolio occupancy rate
* User can log out

## User roles
Only one standard user role is supported for all users

## User interface
The application has a graphical user interface and the first view is the login (and register) view.

<img src="https://raw.githubusercontent.com/miikara/landlord/master/documentation/pictures/new_ui.png">

## Potential future functional capabilities
* User can recover his/her password
* User can retrieve cash flow yield for each unit based on contract and loan details
* Total portfolio cap rate time series
* Total portfolio net operating income time series
* Listings data for units not owned (scraped from Oikotie)
* Tenant table to enable storing and showing more tenant details such as contact information
