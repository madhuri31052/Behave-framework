Feature: Test cases for testing dev3 environment 

    Scenario Outline: Test login to dev3 Dashboard with invalid credentials
        Given Launch Chrome Browser
        When Go to dev3 login page
        And Enters "<Email>" and "<Password>"
        And Click on login button
        Then User should not be able to login
        Examples: dummy data
        | Email | Password |
        | email1 | pwd1@123 |
        | email2 | pwd2@123 |


    Scenario: Login and logout on dev3 Dashboard with valid credentials
        Given Launch Chrome Browser
        When Go to dev3 login page
        And Enter DEV3_CRED_EMAIL and DEV3_CRED_PASS
        And Click on login button
        And Click on Multibox tab
        And Click on Signout tab
        Then User should be signed out

    Scenario: Check user is able to select an Athlete before selecting Warehouse
        Given Launch Chrome Browser
        When Go to dev3 login page
        And Enter DEV3_CRED_EMAIL and DEV3_CRED_PASS
        And Click on login button
        And Select Analytics tab
        And On Ergonomic Safety Dashboard click on Select Athlete dropdown
        Then User should not be able to Select an Athlete before selecting Warehouse


    Scenario: Check sorting icon is enabled to corporate report
        Given Launch Chrome Browser
        When Go to dev3 login page
        And Enter DEV3_CRED_EMAIL and DEV3_CRED_PASS
        And Click on login button
        And Select Analytics tab
        And Click on Fuse Dashboard tab
        And Select corporate report tab
        And Click on sort icon of Warehouse
        Then User should be able to sort