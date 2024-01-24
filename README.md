# Python URL Shortener

This project aims to create a URL shortener with some additional features to enhance its functionality. The program will be developed in Python and include features such as custom short URLs, URL analytics, short URL expiration, and user authentication.

## Features

1. **URL Shortening:**
   - Generate a short URL for a given long URL.
   - Ensure the short URL is unique and redirects to the original long URL.

2. **Custom Short URLs:**
   - Allow users to specify custom short URLs.
   - Validate the uniqueness of custom short URLs and handle conflicts.

3. **URL Analytics:**
   - Track the number of times each short URL is accessed (clicked).
   - Provide a function to retrieve and display analytics for a given short URL.

4. **Expiration of Short URLs:**
   - Add an optional expiration feature for short URLs.
   - Short URLs should become invalid after the specified expiration date.

5. **User Authentication:**
   - Implement a simple authentication system.
   - Allow users to log in, view their created short URLs, and delete them if needed.

6. **User Interface:**
   - Create a command-line or web-based interface for users to interact with the URL shortener.
   - Display messages for successful URL shortening, analytics retrieval, and user authentication.

7. **Error Handling:**
   - Implement error handling for cases such as invalid URLs, duplicate custom short URLs, expired short URLs, etc.

## Running the project

1. **Installation:**
   - Clone the repository.
   - Install the following dependencies:
 ```
pip install mysql-connector-python 
pip install termcolor
pip install questionary
pip install bcrypt
```
  - Import the sql file named `url_shortener.sql`

2. **Usage:**
   - Run `main.py`
   - Interact with the URL shortener through the provided interface.

## Contributor

- Mashiat Hasin Rodoshi
