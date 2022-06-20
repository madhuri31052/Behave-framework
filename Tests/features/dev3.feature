Feature: This is for Dev3 environment 

    Scenario: Login and logout on Safework Dashboard with valid credentials
        Given Launch Chrome Browser
        When Go to Safework login page
        And Enter Email_DB and Pass_DB
        And Click on login button
        Then User should be logged in