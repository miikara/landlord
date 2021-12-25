# Architecture
## Layered structure

The application is structured into:
1. Main landlord service (service.py)
2. Database service (database.py)
3. Entities representing the classes
4. Repositories for all entities that account for class specific database operations
5. The user interface

<img src="https://raw.githubusercontent.com/miikara/landlord/master/documentation/pictures/architecture.png">

## Class diagram

The application has (will have) six entities or classes:
1. User
2. Unit, which is a property (usually an apartment) belonging to a user
3. Lease, which represents a contract with the tenant and includes all its relevant detail
4. Rent, which represents a rent agreed to be paid for a given period. Initial rent is determined in the lease contract but it can change during the validity perido of a lease contract
5. Charge, which is a fee levied by the apartment building usually for the maintenance of the common areas and the unit
 
<img src="https://raw.githubusercontent.com/miikara/landlord/master/documentation/pictures/class diagram_new.png">

## Sequence diagram for accunt creation

The user can create an account from the signup screen with the following sequence:
<img src="https://raw.githubusercontent.com/miikara/landlord/master/documentation/pictures/sequence_chart_sign_up.png">
