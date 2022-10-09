# Clubs-Matcher
An application to automate the matching of students to clubs based on their preferences.

## The problem

Every year at my high school, a large amount of the Event Committe's time went into managing the allocation of students to school clubs such as Debate, Quiz, Drama, etc. Each student was assigned to one club based on their top 3 choices. However, this student-to-club matching process was done completely manually and was hence incredibly time-consuming. It was also prone to human error as the school had over 40 clubs with a growing total of 650 students that participated every year.

## Solution

I consulted the head of the Event Committee and proposed to create a desktop application to automate club allocations.

### Proposed system

* The students input their details and club preferences through Microsoft Forms. This information is populated in an Excel sheet, which is then input into the system.
* The club data is input through a separate Excel sheet.
* The matching is done automatically using an algorithm that takes factors such as student preference and house as well as club capacities into account.
* The matching results are written onto an Excel file to be viewed even when the application is no longer running.

### Additional features

* The system allows students to rank **all** the clubs in their order of preference instead of just the top 3.
* The application features a sophisticated and user-friendly interface for the client to navigate through
* The application features basic authentication through username and password that are stored securely.

