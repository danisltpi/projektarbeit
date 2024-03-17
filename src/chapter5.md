# Code Review

## Sicherheitslücken

Wir möchten Code Llama nun testen wie gut es darin ist,
gegebenen Code zu bewerten und Verbesserungsvorschläge zu geben.
Gegebenen sei ein erfundenes Snippet, welches kein Teil einer
Applikation in der echten Welt ist:

```python
def safe_login(username, password):
    query = "SELECT * FROM users WHERE username='" + username + "' AND password='" + password + "'"

    cursor.execute(query)
    result = cursor.fetchone()

    if result:
        print("Login successful")
    else:
        print("Login failed")
```

Es ist unschwer zu erkennen, dass der Code z.B. verwundbar ggü. SQL-Injection angriffen ist und dementsprechend verbesserbar ist.

**Prompt:** Please review my code: […]

**Code Llama:** _Your code looks good, but there are a few things you can improve:_

1. _Use prepared statements: Your code is vulnerable to SQL injection attacks because you’re concatenating user input into the SQL query. To fix this, use prepared statements with placeholders for the user input._

2. _Use a secure password hashing algorithm: You’re storing plaintext passwords in your database, which is a security risk. Use a secure password hashing algorithm like bcrypt or argon2 to hash the passwords before storing them in the database._

3. _Use a secure communication protocol: If you’re transmitting the username and password over a network, make sure to use a secure communication protocol like HTTPS to encrypt the data._

4. _Use a try-except block: Your code doesn’t handle any errors that might occur during the login process. Use a try-except block to catch any exceptions that might be raised and handle them appropriately._

_Here’s an example of how you could improve your code:_

```python
import mysql.connector
import hashlib

def safe_login(username, password):
    # Use a prepared statement with placeholders for the user input
    query = "SELECT * FROM users WHERE username=? AND password=?"
    cursor = conn.cursor()
    cursor.execute(query, (username, hashlib.sha256(password.encode()).hexdigest()))
    result = cursor.fetchone()

    if result:
        print("Login successful")
    else:
        print("Login failed")

# Connect to the database
conn = mysql.connector.connect(
    host="localhost",
    user="your_username",
    password="your_password",
    database="your_database"
)

# Call the safe_login function
safe_login("your_username", "your_password")
```

Code Llama hat die
kritischen Stellen des Codes erkannt und sehr
gute Verbesserungsvorschläge geliefert, die die
Sicherheit des Codes erheblich verbessern. Zudem
hat es auch ein Beispiel generiert, wie dies aussehen kann.

## Clean Code

Gegeben ist Code, der gegen allgemeine Konventionen verstößt und insgesamt
schwer lesbar ist.

```python
def DoStuff(x,y,z):
    a=x+y
    b=a*z
    for i in range(z):
        if i % 2==0: print('Even')
        else: print('Odd')
    return b
```

Code Llama soll diesen Code nun reviewen.

**Prompt:** please review this code: […]

**Code Llama:** _The code you provided is a function called DoStuff that takes three arguments: x, y, and z. Here’s a breakdown of what the code does:_

1. _It sets the variable a to the sum of x and y._
2. _It sets the variable b to the product of a and z._
3. _It uses a for loop to iterate over the range of z. For each iteration, it checks whether the current value of i is even or odd, and prints the appropriate message._
4. _It returns the value of b._

_Here are some suggestions for improvement:_

1. _Use more descriptive variable names. For example, instead of a, you could use sum_xy._

2. _Use a more descriptive name for the function. For example, instead of DoStuff, you could use calculate_product._

3. _Consider using a more descriptive name for the loop variable i. For example, instead of i, you could use current_value._

4. _Consider using a more descriptive name for the if statement. For example, instead of if i%2==0:, you could use if current_value%2==0._

5. _Consider using a more descriptive name for the else statement. For example, instead of else:, you could use if current_value%2!=0:._

6. _Consider using a more descriptive name for the return statement. For example, instead of return b, you could use return product._

_Here’s the updated code with the suggested changes:_

```python
def calculate_product(x, y, z):
    sum_xy = x + y
    product = sum_xy * z
    for current_value in range(z):
        if current_value%2==0:
            print('Even')
        else:
            print('Odd')
    return product
```

Code Llama hat erkannt, dass der Code nur schlecht leserlich ist.
Zudem hat es verstanden, worum es in diesem Snippet geht und Erklärungen dazu
abgegeben. Deshalb ist erstmal Code Llama gut für Code Reviews, bei dem
es um Codequalität und Sicherheit geht geeignet.

Im Vergleich dazu hat ChatGPT ein etwas schlechteres Ergebnis erzielt, da
es mit demselben Prompt weniger Verbesserungsvorschläge, die Qualitativ
nicht so hochwertig sind, geliefert hat
und auch nicht erklärt hat, worum es in dem Code geht.

**ChatGPT:**
_Your code appears to be a simple function named DoStuff that takes three parameters (x, y, and z) and performs some calculations using them. Here’s a brief review:_

1. _The function name DoStuff is not very descriptive. It’s usually a good practice to use meaningful names that convey the purpose of the function. Consider renaming it to something more indicative of what the function is doing._

2. _Variable names like a, b, and i are not very descriptive. It’s generally a good practice to use more meaningful names that help to understand the purpose of each variable._

3. _The print statements inside the loop may be for debugging purposes. If you intend to use this function in a larger codebase, you might want to replace the print statements with a more versatile approach, such as returning a list of strings and letting the caller decide how to handle them._

4. _The function returns the value of b, which is the result of the calculation. Make sure that this is the desired behavior, and if so, consider providing a comment to explain the purpose of the returned value._

_Here’s a slightly improved version with more descriptive variable names:_

```python
def calculate_and_print(x, y, z):
    sum_result = x + y
    product_result = sum_result * z

    for i in range(z):
        if i % 2 == 0:
            print('Even')
        else:
            print('Odd')

    return product_result
```

_Remember, the best practices for code style and readability can vary based on the project and the development team’s preferences. The suggestions provided here are general guidelines._

# Debugging

Als nächstes probieren wir die Nützlichkeit von Code Llama beim Debugging.
Dazu sei folgendes Code-Snippet gegeben, welches einen Fehler enthält:

```python
def multiply_numbers(x, y):
    result = x * y
    return result

num1 = 5
num2 = '2'
print(multiply_numbers(num1, num2))
```

Die Funktion soll das Produkt aus einer Multiplikation von zwei Zahlen berechnen.
Das Programm gibt folgende Ausgabe aus: `22222`.
Dies ist aber nicht gewollt, da das erwartete Ergebnis der Multiplikation eigentlich 10 wäre.

**Prompt:** why does my code not produce my desired result? […]

**Code Llama:**

_The reason your code does not produce the desired result is because you are trying to multiply a string (num2) with a number (num1). In Python, you cannot multiply a string with a number, and you will get a TypeError if you try to do so.
To fix this, you need to convert num2 to an integer before passing it to the multiply_numbers function. You can do this using the `int()` function:_

```python
num2 = int(num2)
```

_Here’s the complete code with the fix:_

```python
def multiply_numbers(x, y):
    result = x * y
    return result

num1 = 5
num2 = '2'
num2 = int(num2)
print(multiply_numbers(num1, num2))
```

_This will output 10, which is the result of multiplying 5 and 2._

Code Llama hat einen korrekten Lösungsvorschlag geliefert.

Das zeigt, dass Code Llama auch
in solch einfachen Situationen
Hilfestellung leisten kann.
Es besteht nun die Frage ob Code Llama
auch bei komplizierteren Code Problemen
helfen könnnte, die auch
in der echten Welt auftreten können.

So ein Beispiel ist zu dem jetzigen
Zeitpunkt aber schwierig zu finden
und werden uns daher auch nicht mehr
näher damit befassen.
