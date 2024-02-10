Feature: Test the add new button on Client page


    Scenario: Test add new button for adding new client
        Given user is on client page
        When  user clicks on add new button
        And   user enters client_name as "appletech22" and  status as "PILOT" and ActiveInactive_date as "02/22/2022  " and  no_of_contractedusers as "5" and  sub_domain as ""and user click on next button and user selects first name/last name format
        And   user click on confirm button
        Then  user should see new client added successfully message.

