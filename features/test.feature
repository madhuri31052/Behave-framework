Feature: workin on Automation  

    Scenario: Login to Safework Dashboard with valid parameters
        Given Launch Chrome Browser
        When Go to Safework login page
        And Enter Email_DB and Pass_DB
        And Click on login button
        And Click on Multibox tab
        And Click on Signout tab
        Then User should be signed out
    
    Scenario: Check corporate report sorting icon
        Given Launch Chrome Browser
        When Go to Safework login page
        And Enter Email_DB and Pass_DB
        And Click on login button
        And Select Analytics tab
        And Click on Fuse Dashboard tab
        And Select corporate report tab
        And Click on sort icon of Warehouse
        Then User should be able to sort
