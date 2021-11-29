# Architecture
## Layered structure

The application is structured into:
1. Main landlord service (service.py)
2. Database service (database.py)
3. Entities representing the classes
4. Repositories for all entities that account for class specific database operations
5. The user interface

## Class diagram

The application has (will have) six entities or classes:
1. User
2. Unit, which is a property belonging to a user or a listing which has been bought
3. Listing, which represents an advertisement for a unit 
4. Loan, representing the bank loan(s) to finance a purchase of a unit
5. Contract, for the leasing terms of a unit for a certain period
6. Tenant, who is the counterparty for a contract and the dweller of the unit

<img src="https://raw.githubusercontent.com/miikara/landlord/master/documentation/pictures/ui.png">