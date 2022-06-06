# Behave-framework

Install: Python, selenium, behave, allure-behave

To run on terminal just type: behave

To run all feature files: behave ./features

To generate reports

    - create reports folder
    
    - on terminal type: behave -f allure_behave.formatter:AllureFormatter -o reports/ features/
    
    - download allure-behave and add environment varaible path
    
    - on terminal type: allure serve reports/
