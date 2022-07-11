Feature: Test cases for testing qa environment 

    # Scenario Outline: Test login to Safework Dashboard with invalid credentials
    #     Given Launch Chrome Browser
    #     When Go to Safework login page
    #     And Enters "<Email>" and "<Password>"
    #     And Click on login button
    #     Then User should not be able to login
    #     Examples: dummy data
    #     |       Email      | Password |
    #     | email1@gmail.com | pwd1@123 |
    #     | email2@gmail.com | pwd2@123 |

    Scenario: Login and logout on Safework Dashboard with valid credentials
        Given Launch Chrome Browser
        When Go to Safework login page
        And Enter QA_CRED_EMAIL and QA_CRED_PASS
        And Click on login button
        And Click on Multibox tab
        And Click on Signout tab
        Then User should be signed out

    # Scenario: Check user is able to select an Athlete before selecting Warehouse in Ergonomic report
    #     Given Launch Chrome Browser
    #     When Go to Safework login page
    #     And Enter QA_CRED_EMAIL and QA_CRED_PASS
    #     And Click on login button
    #     And Select Analytics tab
    #     And On Ergonomic Safety Dashboard click on Select Athlete dropdown
    #     Then User should not be able to Select an Athlete before selecting Warehouse

    # Scenario: Check Highest Risk Tenure Group tile is present
    #     Given Launch Chrome Browser
    #     When Go to Safework login page
    #     And Enter QA_CRED_EMAIL and QA_CRED_PASS
    #     And Click on login button
    #     And Select Analytics tab
    #     And Click on Fuse Dashboard tab
    #     And Select New Hire Tenure Analysis 
    #     Then User should be able to see Highest Risk Tenure Group tile

    # Scenario: Check sorting icon is enabled to corporate report
    #     Given Launch Chrome Browser
    #     When Go to Safework login page
    #     And Enter QA_CRED_EMAIL and QA_CRED_PASS
    #     And Click on login button
    #     And Select Analytics tab
    #     And Click on Fuse Dashboard tab
    #     And Select corporate report tab
    #     And Click on sort icon of Warehouse
    #     Then User should be able to sort in qa env