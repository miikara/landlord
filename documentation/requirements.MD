# Requirements
## Application description

The purpose of the application is to allow landlords to keep track of their operations and properties on the market.

## Functional capabilities
User not logged in:
* User can create a username and password
    * Username has to be unique and have a minimum length of five characters
    * Password has a minimum length of five character
* User can log in
    * A notification is issued when a username doesn't exists
    * A notification is issued when password is incorrect

User logged in:
* User can insert details of listings, units (properties owned), tenants, rental contracts and bank loans
    * Details include compulsory fields (such as address of unit) and optional fields (such as renovation dates)
* User can edit details apart from unique identifiers such as unit id of a particular unit
* User can retrieve current and historical information regarding the inserted fields
    * User can retrieve listings based on location, asking price and renovation needs
    * User can retrieve unit details based on unit name
    * User can retrieve unit's tenant, contract or loan history based on unit name
* User can retrieve a calculated rental yield for each listing based on estimated rent level, renovations, asking price and taxes. 

## User roles
Only one standard user role is supported for all users

## User interface
The application has a graphical user interface and the first view is the login (and register) view.

<img src="https://raw.githubusercontent.com/miikara/landlord/master/documentation/pictures/ui.png">

## Potential future functional capabilities
* User can recover his/her password
* User can retrieve cash flow yield for each unit based on contract and loan details
* Listings data can automatically scraped from Oikotie
* Inbound payments can be inserted or fetched (via API for example)
* Outbound payments can be insered or fetched