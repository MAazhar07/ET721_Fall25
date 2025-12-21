Mohammed Azhar  
Professor Huixin Wu  
ET721  
December 20, 2025  

# Report: The Benefits of Comprehensive Testing in Software Development

## Before and After: Results Summary

Initially, the project had partial test coverage of around 85% overall, 
with app/models.py at about 92%. After completing the unit tests, 
I achieved 96% coverage on app/models.py (only 2 lines missed) 
and 65% overall (due to untested routes). 
I wrote 13 passing unit tests.

## Untested Code: Effects

Before adding tests, I struggled to understand all features and edge cases. 
The validations on name and quantity in the Fruit model were not obvious 
without running the code manually.Testing the API manually with curl or Postman 
was time-consuming and error-prone. I had to repeatedly start the server, send requests, 
and check responses.With few tests, my understanding of the API was incomplete. 
I lacked confidence that changes wouldn’t break something unexpected.

## Adding Tests

I started by reviewing the existing tests in test_models.py 
and analyzing app/models.py to understand the Fruit model 
and FruitMetrics class.I used pytest fixtures to set up an in-memory database 
for each test. I completed missing tests (average quantity, most common fruit, 
negative/non-integer quantity) and added new ones for search, 
serialize, and edge cases.Unit tests focus on individual 
components like model validations. API tests verify full endpoints and 
HTTP responses. Unit tests are faster and catch logic errors early; 
API tests ensure real-world behavior. Both are valuable, 
but this project focused on unit tests.

## Automation

Automating tests with GitHub Actions ensures every commit 
or pull request runs the test suite automatically. 
This catches bugs early, saves time, and builds confidence 
in the codebase. It also enforces quality standards for the team.

## New Features

Adding new features on a well-tested codebase felt much safer. 
I could refactor or extend the Fruit model without fear 
of breaking existing functionality. The tests acted as a safety net 
so any regression was caught immediately. This gave me a strong sense 
of security and reduced stress during development.

## Extra Credit
For extra credit, I added an optional expiration_date field to the Fruit model, 
updated the search method to filter expired fruits, added a new endpoint /api/fruits/expired, a
nd wrote unit tests for the new feature.

## Future

This project taught me the importance of testing from the start. 
Writing tests early saves time and prevents technical debt.
I plan to adopt test-driven development (TDD) — writing tests 
before or alongside new code. I also want to add API tests 
and aim for 100% coverage. This experience changed my perspective 
which is that testing is essential 
for building stable, professional software.

