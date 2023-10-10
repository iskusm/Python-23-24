In Python, **operators** are special symbols, combinations of symbols, or keywords that designate some type of computation. You can combine objects and operators to build **expressions** that perform the actual computation. So, operators are the building blocks of expressions, which you can use to manipulate your data. Therefore, understanding how operators work in Python is essential for you as a programmer.

In this tutorial, you’ll learn about the operators that Python currently supports. You’ll also learn the basics of how to use these operators to build expressions.

**In this tutorial, you’ll:**

- Get to know Python’s **arithmetic operators** and use them to build **arithmetic expressions**
- Explore Python’s **comparison**, **Boolean**, **identity**, and **membership** operators
- Build **expressions** with comparison, Boolean, identity, and membership operators
- Learn about Python’s **bitwise** operators and how to use them
- Combine and repeat sequences using the **concatenation** and **repetition** operators
- Understand the **augmented assignment** operators and how they work

To get the most out of this tutorial, you should have a basic understanding of Python programming concepts, such as [variables](https://realpython.com/python-variables/), [assignments](https://realpython.com/python-assignment-operator/), and built-in [data types](https://realpython.com/python-data-types/).

## Getting Started With Operators and Expressions[](https://realpython.com/python-operators-expressions/#getting-started-with-operators-and-expressions "Permanent link")

In programming, an **operator** is usually a symbol or combination of symbols that allows you to perform a specific operation. This operation can act on one or more **operands**. If the operation involves a single operand, then the operator is **unary**. If the operator involves two operands, then the operator is **binary**.

For example, in Python, you can use the minus sign (`-`) as a unary operator to declare a negative number. You can also use it to subtract two numbers:

\>>>

```python
>>> -273.15
-273.15

>>> 5 - 2
3
```

In this code snippet, the minus sign (`-`) in the first example is a unary operator, and the number `273.15` is the operand. In the second example, the same symbol is a binary operator, and the numbers `5` and `2` are its left and right operands.

Programming languages typically have operators built in as part of their syntax. In many languages, including Python, you can also create your own operator or modify the behavior of existing ones, which is a powerful and advanced feature to have.

In practice, operators provide a quick shortcut for you to manipulate data, perform mathematical calculations, compare values, run [Boolean](https://realpython.com/python-boolean/) tests, assign values to variables, and more. In Python, an operator may be a symbol, a combination of symbols, or a [keyword](https://realpython.com/python-keywords/), depending on the type of operator that you’re dealing with.

For example, you’ve already seen the subtraction operator, which is represented with a single minus sign (`-`). The equality operator is a double equal sign (`==`). So, it’s a combination of symbols:

In this example, you use the Python equality operator (`==`) to compare two numbers. As a result, you get [`True`](https://docs.python.org/3/library/constants.html#True), which is one of Python’s Boolean values.

Speaking of Boolean values, the Boolean or logical operators in Python are keywords rather than signs, as you’ll learn in the section about [Boolean operators and expressions](https://realpython.com/python-operators-expressions/#boolean-operators-and-expressions-in-python). So, instead of the odd signs like `||`, `&&`, and `!` that many other programming languages use, Python uses `or`, `and`, and `not`.

Using keywords instead of odd signs is a really cool design decision that’s consistent with the fact that Python loves and encourages [code’s readability](https://pep20.org/#readability).

You’ll find several categories or groups of operators in Python. Here’s a quick list of those categories:

- **Assignment** operators
- **Arithmetic** operators
- **Comparison** operators
- **Boolean** or logical operators
- **Identity** operators
- **Membership** operators
- **Concatenation** and **repetition** operators
- **Bitwise** operators

All these types of operators take care of specific types of computations and data-processing tasks. You’ll learn more about these categories throughout this tutorial. However, before jumping into more practical discussions, you need to know that the most elementary goal of an operator is to be part of an [expression](https://docs.python.org/3/glossary.html#term-expression). Operators by themselves don’t do much:

\>>>

```python
>>> -
  File "<input>", line 1
    -
    ^
SyntaxError: incomplete input

>>> ==
  File "<input>", line 1
    ==
    ^^
SyntaxError: incomplete input

>>> or
  File "<input>", line 1
    or
    ^^
SyntaxError: incomplete input
```

As you can see in this code snippet, if you use an operator without the required operands, then you’ll get a [syntax error](https://realpython.com/invalid-syntax-python/). So, operators must be part of expressions, which you can build using Python objects as operands.

So, what is an expression anyway? Python has [simple](https://docs.python.org/3/reference/simple_stmts.html) and [compound](https://docs.python.org/3/reference/compound_stmts.html) statements. A simple statement is a construct that occupies a single [logical line](https://docs.python.org/3/reference/lexical_analysis.html#logical-lines), like an assignment statement. A compound statement is a construct that occupies multiple logical lines, such as a [`for` loop](https://realpython.com/python-for-loop/) or a [conditional](https://realpython.com/python-conditional-statements/) statement. An **expression** is a simple statement that produces and returns a value.

You’ll find operators in many expressions. Here are a few examples:

\>>>

```python
>>> 7 + 5
12

>>> 42 / 2
21.0

>>> 5 == 5
True
```

In the first two examples, you use the addition and division operators to construct two arithmetic expressions whose operands are integer numbers. In the last example, you use the equality operator to create a comparison expression. In all cases, you get a specific value after executing the expression.

Note that not all expressions use operators. For example, a bare [function call](https://realpython.com/defining-your-own-python-function/#function-calls-and-definition) is an expression that doesn’t require any operator:

\>>>

```python
>>> abs(-7)
7

>>> pow(2, 8)
256

>>> print("Hello, World!")
Hello, World!
```

In the first example, you call the built-in [`abs()`](https://realpython.com/python-absolute-value/) function to get the [absolute value](https://en.wikipedia.org/wiki/Absolute_value) of `-7`. Then, you compute `2` to the power of `8` using the built-in `pow()` function. These function calls occupy a single logical line and return a value. So, they’re expressions.

Finally, the call to the built-in [`print()`](https://realpython.com/python-print/) function is another expression. This time, the function doesn’t [return](https://realpython.com/python-return-statement/) a fruitful value, but it still returns `None`, which is the Python [null type](https://realpython.com/null-in-python/). So, the call is technically an expression.

Even though all expressions are statements, not all statements are expressions. For example, pure [assignment statements](https://realpython.com/python-operators-expressions/#the-assignment-operator-and-statements) don’t return any value, as you’ll learn in a moment. Therefore, they’re not expressions. The assignment operator is a special operator that doesn’t create an expression but a statement.

Okay! That was a quick introduction to operators and expressions in Python. Now it’s time to dive deeper into the topic. To kick things off, you’ll start with the assignment operator and statements.

## The Assignment Operator and Statements[](https://realpython.com/python-operators-expressions/#the-assignment-operator-and-statements "Permanent link")

The **assignment operator** is one of the most frequently used operators in Python. The operator consists of a single equal sign (`=`), and it operates on two operands. The left-hand operand is typically a [variable](https://realpython.com/python-variables/), while the right-hand operand is an expression.

The assignment operator allows you to _assign values to variables_. Strictly speaking, in Python, this operator makes variables or names refer to specific objects in your computer’s memory. In other words, an assignment creates a reference to a concrete object and attaches that reference to the target variable.

For example, all the statements below create new variables that hold references to specific objects:

\>>>

```python
>>> number = 42
>>> day = "Friday"
>>> digits = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
>>> letters = ["a", "b", "c"]
```

In the first statement, you create the `number` variable, which holds a reference to the [number](https://realpython.com/python-numbers/) `42` in your computer’s memory. You can also say that the name `number` [points](https://realpython.com/pointers-in-python/) to `42`, which is a concrete object.

In the rest of the examples, you create other variables that point to other types of objects, such as a [string](https://realpython.com/python-strings/), [tuple](https://realpython.com/python-lists-tuples/#python-tuples), and [list](https://realpython.com/python-list/), respectively.

You’ll use the assignment operator in many of the examples that you’ll write throughout this tutorial. More importantly, you’ll use this operator many times in your own code. It’ll be your forever friend. Now you can dive into other Python operators!

## Arithmetic Operators and Expressions in Python[](https://realpython.com/python-operators-expressions/#arithmetic-operators-and-expressions-in-python "Permanent link")

**Arithmetic operators** are those operators that allow you to perform _arithmetic operations_ on numeric values. Yes, they come from math, and in most cases, you’ll represent them with the usual math signs. The following table lists the arithmetic operators that Python currently supports:

| Operator | Type   | Operation                          | Sample Expression | Result                                                                        |
| -------- | ------ | ---------------------------------- | ----------------- | ----------------------------------------------------------------------------- |
| `+`      | Unary  | Positive                           | `+a`              | `a` without any transformation since this is simply a complement to negation  |
| `+`      | Binary | Addition                           | `a + b`           | The arithmetic sum of `a` and `b`                                             |
| `-`      | Unary  | Negation                           | `-a`              | The value of `a` but with the opposite sign                                   |
| `-`      | Binary | Subtraction                        | `a - b`           | `b` subtracted from `a`                                                       |
| `*`      | Binary | Multiplication                     | `a * b`           | The product of `a` and `b`                                                    |
| `/`      | Binary | Division                           | `a / b`           | The quotient of `a` divided by `b`, expressed as a float                      |
| `%`      | Binary | Modulo                             | `a % b`           | The remainder of `a` divided by `b`                                           |
| `//`     | Binary | Floor division or integer division | `a // b`          | The quotient of `a` divided by `b`, rounded to the next smallest whole number |
| `**`     | Binary | Exponentiation                     | `a**b`            | `a` raised to the power of `b`                                                |

Note that `a` and `b` in the _Sample Expression_ column represent numeric values, such as [integer](https://realpython.com/python-numbers/#integers), [floating-point](https://realpython.com/python-numbers/#floating-point-numbers), [complex](https://realpython.com/python-complex-numbers/), [rational](https://realpython.com/python-fractions/), and [decimal](https://docs.python.org/3/library/decimal.html#decimal.Decimal) numbers.

Here are some examples of these operators in use:

\>>>

```python
>>> a = 5
>>> b = 2

>>> +a
5
>>> -b
-2
>>> a + b
7
>>> a - b
3
>>> a * b
10
>>> a / b
2.5
>>> a % b
1
>>> a // b
2
>>> a**b
25
```

In this code snippet, you first create two new variables, `a` and `b`, holding `5` and `2`, respectively. Then you use these variables to create different arithmetic expressions using a specific operator in each expression.

Again, the standard division operator (`/`) always returns a floating-point number, even if the dividend is evenly divisible by the divisor:

\>>>

```python
>>> 10 / 5
2.0

>>> 10.0 / 5
2.0
```

In the first example, `10` is evenly divisible by `5`. Therefore, this operation could return the integer `2`. However, it returns the floating-point number `2.0`. In the second example, `10.0` is a floating-point number, and `5` is an integer. In this case, Python internally promotes `5` to `5.0` and runs the division. The result is a floating-point number too.

Finally, consider the following examples of using the floor division (`//`) operator:

\>>>

```python
>>> 10 // 4
2
>>> -10 // -4
2

>>> 10 // -4
-3
>>> -10 // 4
-3
```

Floor division always [rounds down](https://realpython.com/python-rounding/#rounding-down). This means that the result is the greatest integer that’s smaller than or equal to the quotient. For positive numbers, it’s as though the fractional portion is truncated, leaving only the integer portion.

## Comparison Operators and Expressions in Python[](https://realpython.com/python-operators-expressions/#comparison-operators-and-expressions-in-python "Permanent link")

The Python **comparison operators** allow you to _compare_ numerical values and any other objects that support them. The table below lists all the currently available comparison operators in Python:

| Operator            | Operation                | Sample Expression | Result                                                    |
| ------------------- | ------------------------ | ----------------- | --------------------------------------------------------- |
| `==`                | Equal to                 | `a == b`          | • `True` if the value of `a` is equal to the value of `b` |
| • `False` otherwise |                          |                   |                                                           |
| `!=`                | Not equal to             | `a != b`          | • `True` if `a` isn’t equal to `b`                        |
| • `False` otherwise |                          |                   |                                                           |
| `<`                 | Less than                | `a < b`           | • `True` if `a` is less than `b`                          |
| • `False` otherwise |                          |                   |                                                           |
| `<=`                | Less than or equal to    | `a <= b`          | • `True` if `a` is less than or equal to `b`              |
| • `False` otherwise |                          |                   |                                                           |
| `>`                 | Greater than             | `a > b`           | • `True` if `a` is greater than `b`                       |
| • `False` otherwise |                          |                   |                                                           |
| `>=`                | Greater than or equal to | `a >= b`          | • `True` if `a` is greater than or equal to `b`           |
| • `False` otherwise |                          |                   |                                                           |

The comparison operators are all binary. This means that they require left and right operands. These operators always return a Boolean value (`True` or `False`) that depends on the [truth value](https://en.wikipedia.org/wiki/Truth_value) of the comparison at hand.

Note that comparisons between objects of different data types often don’t make sense and sometimes aren’t allowed in Python. For example, you can compare a number and a string for equality with the `==` operator. However, you’ll get `False` as a result:

The integer `2` isn’t equal to the string `"2"`. Therefore, you get `False` as a result. You can also use the `!=` operator in the above expression, in which case you’ll get `True` as a result.

Non-equality comparisons between operands of different data types raise a `TypeError` exception:

\>>>

```python
>>> 5 < "7"
Traceback (most recent call last):
    ...
TypeError: '<' not supported between instances of 'int' and 'str'
```

In this example, Python raises a `TypeError` exception because a less than comparison (`<`) doesn’t make sense between an integer and a string. So, the operation isn’t allowed.

It’s important to note that in the context of comparisons, integer and floating-point values are compatible, and you can compare them.

You’ll typically use and find comparison operators in Boolean contexts like [conditional statements](https://realpython.com/python-conditional-statements/) and [`while` loops](https://realpython.com/python-while-loop/). They allow you to make decisions and define a program’s [control flow](https://en.wikipedia.org/wiki/Control_flow).

The comparison operators work on several types of operands, such as numbers, strings, tuples, and lists. In the following sections, you’ll explore the differences.

### Comparison of Integer Values[](https://realpython.com/python-operators-expressions/#comparison-of-integer-values "Permanent link")

Probably, the more straightforward comparisons in Python and in math are those involving integer numbers. They allow you to count real objects, which is a familiar day-to-day task. In fact, the non-negative integers are also called [natural numbers](https://en.wikipedia.org/wiki/Natural_number). So, comparing this type of number is probably pretty intuitive, and doing so in Python is no exception.

Consider the following examples that compare integer numbers:

\>>>

```python
>>> a = 10
>>> b = 20
>>> a == b
False
>>> a != b
True
>>> a < b
True
>>> a <= b
True
>>> a > b
False
>>> a >= b
False

>>> x = 30
>>> y = 30
>>> x == y
True
>>> x != y
False
>>> x < y
False
>>> x <= y
True
>>> x > y
False
>>> x >= y
True
```

In the first set of examples, you define two variables, `a` and `b`, to run a few comparisons between them. The value of `a` is less than the value of `b`. So, every comparison expression returns the expected Boolean value. The second set of examples uses two values that are equal, and again, you get the expected results.

### Comparison of Floating-Point Values[](https://realpython.com/python-operators-expressions/#comparison-of-floating-point-values "Permanent link")

Comparing floating-point numbers is a bit [more complicated](https://realpython.com/python-numbers/#make-python-lie-to-you) than comparing integers. The value stored in a `float` object may not be precisely what you’d think it would be. For that reason, it’s bad practice to compare floating-point values for exact equality using the `==` operator.

Consider the example below:

\>>>

```python
>>> x = 1.1 + 2.2
>>> x == 3.3
False

>>> 1.1 + 2.2
3.3000000000000003
```

Yikes! The internal representation of this addition isn’t exactly equal to `3.3`, as you can see in the final example. So, comparing `x` to `3.3` with the equality operator returns `False`.

To compare floating-point numbers for equality, you need to use a different approach. The preferred way to determine whether two floating-point values are equal is to determine whether they’re close to one another, given some tolerance.

The `math` module from the standard library provides a function conveniently called `isclose()` that will help you with `float` comparison. The function takes two numbers and tests them for approximate equality:

\>>>

```python
>>> from math import isclose

>>> x = 1.1 + 2.2

>>> isclose(x, 3.3)
True
```

In this example, you use the `isclose()` function to compare `x` and `3.3` for approximate equality. This time, you get `True` as a result because both numbers are close enough to be considered equal.

For further details on using `isclose()`, check out the [Find the Closeness of Numbers With Python `isclose()`](https://realpython.com/python-math-module/#find-the-closeness-of-numbers-with-python-isclose) section in [The Python `math` Module: Everything You Need to Know](https://realpython.com/python-math-module/).

### Comparison of Strings[](https://realpython.com/python-operators-expressions/#comparison-of-strings "Permanent link")

You can also use the comparison operators to compare Python strings in your code. In this context, you need to be aware of how Python internally compares string objects. In practice, Python compares strings character by character using each character’s [Unicode](https://realpython.com/python-encodings-guide/) **code point**. Unicode is Python’s [default character set](https://docs.python.org/3/howto/unicode.html#the-string-type).

You can use the built-in [`ord()`](https://docs.python.org/3/library/functions.html#ord) function to learn the Unicode code point of any character in Python. Consider the following examples:

\>>>

```python
>>> ord("A")
65
>>> ord("a")
97

>>> "A" == "a"
False
>>> "A" > "a"
False
>>> "A" < "a"
True
```

The uppercase `"A"` has a lower Unicode point than the lowercase `"a"`. So, `"A"` is less than `"a"`. In the end, Python compares characters using integer numbers. So, the same rules that Python uses to compare integers apply to string comparison.

When it comes to strings with several characters, Python runs the comparison character by character in a loop.

The comparison uses [lexicographical ordering](https://docs.python.org/3/tutorial/datastructures.html?highlight=lexicographical#comparing-sequences-and-other-types), which means that Python compares the first item from each string. If their Unicode code points are different, this difference determines the comparison result. If the Unicode code points are equal, then Python compares the next two characters, and so on, until either string is exhausted:

\>>>

```python
>>> "Hello" > "HellO"
True

>>> ord("o")
111
>>> ord("O")
79
```

In this example, Python compares both operands character by character. When it reaches the end of the string, it compares `"o"` and `"O"`. Because the lowercase letter has a greater Unicode code point, the first version of the string is greater than the second.

You can also compare strings of different lengths:

\>>>

```python
>>> "Hello" > "Hello, World!"
False
```

In this example, Python runs a character-by-character comparison as usual. If it runs out of characters, then the shorter string is less than the longer one. This also means that the empty string is the smallest possible string.

### Comparison of Lists and Tuples[](https://realpython.com/python-operators-expressions/#comparison-of-lists-and-tuples "Permanent link")

In your Python journey, you can also face the need to compare lists with other lists and tuples with other tuples. These data types also support the standard comparison operators. Like with strings, when you use a comparison operator to compare two lists or two tuples, Python runs an item-by-item comparison.

Note that Python applies specific rules depending on the type of the contained items. Here are some examples that compare lists and tuples of integer values:

\>>>

```python
>>> [2, 3] == [2, 3]
True
>>> (2, 3) == (2, 3)
True

>>> [5, 6, 7] < [7, 5, 6]
True
>>> (5, 6, 7) < (7, 5, 6)
True

>>> [4, 3, 2] < [4, 3, 2]
False
>>> (4, 3, 2) < (4, 3, 2)
False
```

In these examples, you compare lists and tuples of numbers using the standard comparison operators. When comparing these data types, Python runs an item-by-item comparison.

For example, in the first expression above, Python compares the `2` in the left operand and the `2` in the right operand. Because they’re equal, Python continues comparing `3` and `3` to conclude that both lists are equal. The same thing happens in the second example, where you compare tuples containing the same data.

It’s important to note that you can actually compare lists to tuples using the `==` and `!=` operators. However, you _can’t_ compare lists and tuples using the `<`, `>`, `<=`, and `>=` operators:

\>>>

```python
>>> [2, 3] == (2, 3)
False
>>> [2, 3] != (2, 3)
True

>>> [2, 3] > (2, 3)
Traceback (most recent call last):
    ...
TypeError: '>' not supported between instances of 'list' and 'tuple'

>>> [2, 3] <= (2, 3)
Traceback (most recent call last):
    ...
TypeError: '<=' not supported between instances of 'list' and 'tuple'
```

Python supports equality comparison between lists and tuples. However, it doesn’t support the rest of the comparison operators, as you can conclude from the final two examples. If you try to use them, then you get a `TypeError` telling you that the operation isn’t supported.

You can also compare lists and tuples of different lengths:

\>>>

```python
>>> [5, 6, 7] < [8]
True
>>> (5, 6, 7) < (8,)
True

>>> [5, 6, 7] == [5]
False
>>> (5, 6, 7) == (5,)
False

>>> [5, 6, 7] > [5]
True
>>> (5, 6, 7) > (5,)
True
```

In the first two examples, you get `True` as a result because `5` is less than `8`. That fact is sufficient for Python to solve the comparison. In the second pair of examples, you get `False`. This result makes sense because the compared sequences don’t have the same length, so they can’t be equal.

In the final pair of examples, Python compares `5` with `5`. They’re equal, so the comparison continues. Because there are no more values to compare in the right-hand operands, Python concludes that the left-hand operands are greater.

As you can see, comparing lists and tuples can be tricky. It’s also an expensive operation that, in the worst case, requires traversing two entire sequences. Things get more complex and expensive when the contained items are also sequences. In those situations, Python will also have to compare items in a value-by-value manner, which adds cost to the operation.

## Boolean Operators and Expressions in Python[](https://realpython.com/python-operators-expressions/#boolean-operators-and-expressions-in-python "Permanent link")

Python has three Boolean or logical operators: [`and`](https://realpython.com/python-and-operator/), [`or`](https://realpython.com/python-or-operator/), and [`not`](https://realpython.com/python-not-operator/). They define a set of operations denoted by the generic operators [`AND`](https://en.wikipedia.org/wiki/Logical_conjunction), [`OR`](https://en.wikipedia.org/wiki/Logical_disjunction), and [`NOT`](https://en.wikipedia.org/wiki/Negation). With these operators, you can create compound conditions.

In the following sections, you’ll learn how the Python Boolean operators work. Especially, you’ll learn that some of them behave differently when you use them with Boolean values or with regular objects as operands.

### Boolean Expressions Involving Boolean Operands[](https://realpython.com/python-operators-expressions/#boolean-expressions-involving-boolean-operands "Permanent link")

You’ll find many objects and expressions that are of Boolean type or `bool`, as Python calls this type. In other words, many objects evaluate to `True` or `False`, which are the Python Boolean values.

For example, when you evaluate an expression using a comparison operator, the result of that expression is always of `bool` type:

\>>>

```python
>>> age = 20

>>> is_adult = age > 18
>>> is_adult
True

>>> type(is_adult)
<class 'bool'>
```

In this example, the expression `age > 18` returns a Boolean value, which you store in the `is_adult` variable. Now `is_adult` is of `bool` type, as you can see after calling the built-in [`type()`](https://docs.python.org/3/library/functions.html#type) function.

You can also find Python built-in and custom functions that return a Boolean value. This type of function is known as a [predicate](https://realpython.com/python-return-statement/#returning-true-or-false) function. The built-in [`all()`](https://realpython.com/python-all/), [`any()`](https://realpython.com/any-python/), [`callable()`](https://docs.python.org/3/library/functions.html#callable), and [`isinstance()`](https://docs.python.org/3/library/functions.html?highlight=built#isinstance) functions are all good examples of this practice.

Consider the following examples:

\>>>

```python
>>> number = 42

>>> validation_conditions = (
...     isinstance(number, int),
...     number % 2 == 0,
... )

>>> all(validation_conditions)
True

>>> callable(number)
False
>>> callable(print)
True
```

In this code snippet, you first define a variable called `number` using your old friend the assignment operator. Then you create another variable called `validation_conditions`. This variable holds a tuple of expressions. The first expression uses `isinstance()` to check whether `number` is an integer value.

The second is a compound expression that combines the modulo (`%`) and equality (`==`) operators to create a condition that checks whether the input value is an even number. In this condition, the modulo operator returns the remainder of dividing `number` by `2`, and the equality operator compares the result with `0`, returning `True` or `False` as the comparison’s result.

Then you use the `all()` function to determine if all the conditions are true. In this example, because `number = 42`, the conditions are true, and `all()` returns `True`. You can play with the value of `number` if you’d like to experiment a bit.

In the final two examples, you use the `callable()` function. As its name suggests, this function allows you to determine whether an object is **callable**. Being callable means that you can call the object with a pair of parentheses and appropriate arguments, as you’d call any Python function.

The `number` variable isn’t callable, and the function returns `False`, accordingly. In contrast, the `print()` function is callable, so `callable()` returns `True`.

All the previous discussion is the basis for understanding how the Python logical operators work with Boolean operands.

Logical expressions involving `and`, `or`, and `not` are straightforward when the operands are Boolean. Here’s a summary. Note that `x` and `y` represent Boolean operands:

| Operator                   | Sample Expression | Result                                  |
| -------------------------- | ----------------- | --------------------------------------- |
| `and`                      | `x and y`         | • `True` if both `x` and `y` are `True` |
| • `False` otherwise        |                   |                                         |
| `or`                       | `x or y`          | • `True` if either `x` or `y` is `True` |
| • `False` otherwise        |                   |                                         |
| `not`                      | `not x`           | • `True` if `x` is `False`              |
| • `False` if `x` is `True` |                   |                                         |

This table summarizes the truth value of expressions that you can create using the logical operators with Boolean operands. There’s something to note in this summary. Unlike `and` and `or`, which are binary operators, the `not` operator is unary, meaning that it operates on one operand. This operand must always be on the right side.

Now it’s time to take a look at how the operators work in practice. Here are a few examples of using the `and` operator with Boolean operands:

\>>>

```python
>>> 5 < 7 and 3 == 3
True

>>> 5 < 7 and 3 != 3
False

>>> 5 > 7 and 3 == 3
False

>>> 5 > 7 and 3 != 3
False
```

In the first example, both operands return `True`. Therefore, the `and` expression returns `True` as a result. In the second example, the left-hand operand is `True`, but the right-hand operand is `False`. Because of this, the `and` operator returns `False`.

In the third example, the left-hand operand is `False`. In this case, the `and` operator immediately returns `False` and never evaluates the `3 == 3` condition. This behavior is called [short-circuit evaluation](https://realpython.com/python-boolean/#short-circuit-chain-evaluation). You’ll learn more about it in a moment.

In the final example, both conditions return `False`. Again, `and` returns `False` as a result. However, because of the short-circuit evaluation, the right-hand expression isn’t evaluated.

What about the `or` operator? Here are a few examples that demonstrate how it works:

\>>>

```python
>>> 5 < 7 or 3 == 3
True

>>> 5 < 7 or 3 != 3
True

>>> 5 > 7 or 3 == 3
True

>>> 5 > 7 or 3 != 3
False
```

In the first three examples, at least one of the conditions returns `True`. In all cases, the `or` operator returns `True`. Note that if the left-hand operand is `True`, then `or` applies short-circuit evaluation and doesn’t evaluate the right-hand operand. This makes sense. If the left-hand operand is `True`, then `or` already knows the final result. Why would it need to continue the evaluation if the result won’t change?

In the final example, both operands are `False`, and this is the only situation where `or` returns `False`. It’s important to note that if the left-hand operand is `False`, then `or` has to evaluate the right-hand operand to arrive at a final conclusion.

Finally, you have the `not` operator, which negates the current truth value of an object or expression:

\>>>

```python
>>> 5 < 7
True

>>> not 5 < 7
False
```

If you place `not` before an expression, then you get the inverse truth value. When the expression returns `True`, you get `False`. When the expression evaluates to `False`, you get `True`.

There is a fundamental behavior distinction between `not` and the other two Boolean operators. In a `not` expression, you always get a Boolean value as a result. That’s not always the rule that governs `and` and `or` expressions, as you’ll learn in the [Boolean Expressions Involving Other Types of Operands](https://realpython.com/python-operators-expressions/#boolean-expressions-involving-other-types-of-operands) section.

### Evaluation of Regular Objects in a Boolean Context[](https://realpython.com/python-operators-expressions/#evaluation-of-regular-objects-in-a-boolean-context "Permanent link")

In practice, most Python objects and expressions aren’t Boolean. In other words, most objects and expressions don’t have a `True` or `False` value but a different type of value. However, you can use any Python object in a Boolean context, such as a conditional statement or a `while` loop.

In Python, all objects have a specific truth value. So, you can use the logical operators with all types of operands.

Python has well-established rules to determine the truth value of an object when you use that object in a Boolean context or as an operand in an expression built with logical operators. Here’s what the documentation says about this topic:

> By default, an object is considered true unless its class defines either a [`__bool__()`](https://docs.python.org/3/reference/datamodel.html#object.__bool__) method that returns `False` or a [`__len__()`](https://docs.python.org/3/reference/datamodel.html#object.__len__) method that returns zero, when called with the object. Here are most of the built-in objects considered false:
> 
> - constants defined to be false: `None` and `False`.
> - zero of any numeric type: `0`, `0.0`, `0j`, `Decimal(0)`, `Fraction(0, 1)`
> - empty sequences and collections: `''`, `()`, `[]`, `{}`, `set()`, `range(0)`
> 
> ([Source](https://docs.python.org/3/library/stdtypes.html#truth-value-testing))

You can determine the truth value of an object by calling the built-in [`bool()`](https://docs.python.org/3/library/functions.html#bool) function with that object as an argument. If `bool()` returns `True`, then the object is **truthy**. If `bool()` returns `False`, then it’s **falsy**.

For numeric values, you have that a zero value is falsy, while a non-zero value is truthy:

\>>>

```python
>>> bool(0), bool(0.0), bool(0.0+0j)
(False, False, False)

>>> bool(-3), bool(3.14159), bool(1.0+1j)
(True, True, True)
```

Python considers the zero value of all numeric types falsy. All the other values are truthy, regardless of how close to zero they are.

When it comes to evaluating strings, you have that an empty string is always falsy, while a non-empty string is truthy:

\>>>

```python
>>> bool("")
False

>>> bool(" ")
True

>>> bool("Hello")
True
```

Note that strings containing white spaces are also truthy in Python’s eyes. So, don’t confuse empty strings with whitespace strings.

Finally, built-in container data types, such as lists, tuples, [sets](https://realpython.com/python-sets/), and [dictionaries](https://realpython.com/python-dicts/), are falsy when they’re empty. Otherwise, Python considers them truthy objects:

\>>>

```python
>>> bool([])
False
>>> bool([1, 2, 3])
True

>>> bool(())
False
>>> bool(("John", 25, "Python Dev"))
True

>>> bool(set())
False
>>> bool({"square", "circle", "triangle"})
True

>>> bool({})
False
>>> bool({"name": "John", "age": 25, "job": "Python Dev"})
True
```

To determine the truth value of container data types, Python relies on the `.__len__()` [special method](https://realpython.com/python-classes/#special-methods-and-protocols). This method provides support for the built-in [`len()`](https://realpython.com/len-python-function/) function, which you can use to determine the number of items in a given container.

In general, if `.__len__()` returns `0`, then Python considers the container a falsy object, which is consistent with the general rules you’ve just learned before.

All the discussion about the truth value of Python objects in this section is key to understanding how the logical operators behave when they take arbitrary objects as operands.

### Boolean Expressions Involving Other Types of Operands[](https://realpython.com/python-operators-expressions/#boolean-expressions-involving-other-types-of-operands "Permanent link")

You can also use any objects, such as numbers or strings, as operands to `and`, `or`, and `not`. You can even use combinations of a Boolean object and a regular one. In these situations, the result depends on the truth value of the operands.

You’ve already learned how Python determines the truth value of objects. So, you’re ready to dive into creating expressions with logic operators and regular objects.

To start off, below is a table that summarizes what you get when you use two objects, `x` and `y`, in an `and` expression:

| If `x` is | `x and y` returns |
| --------- | ----------------- |
| Truthy    | `y`               |
| Falsy     | `x`               |

It’s important to emphasize a subtle detail in the above table. When you use `and` in an expression, you don’t always get `True` or `False` as a result. Instead, you get one of the operands. You only get `True` or `False` if the returned operand has either of these values.

Here are some code examples that use integer values. Remember that in Python, the zero value of numeric types is falsy. The rest of the values are truthy:

\>>>

```python
>>> 3 and 4
4

>>> 0 and 4
0

>>> 3 and 0
0
```

In the first expression, the left-hand operand (`3`) is truthy. So, you get the right-hand operand (`4`) as a result.

In the second example, the left-hand operand (`0`) is falsy, and you get it as a result. In this case, Python applies the short-circuit evaluation technique. It already knows that the whole expression is false because `0` is falsy, so Python returns `0` immediately without evaluating the right-hand operand.

In the final expression, the left-hand operand (`3`) is truthy. Therefore Python needs to evaluate the right-hand operand to make a conclusion. As a result, you get the right-hand operand, no matter what its truth value is.

When it comes to using the `or` operator, you also get one of the operands as a result. This is what happens for two arbitrary objects, `x` and `y`:

| If `x` is | `x or y` returns |
| --------- | ---------------- |
| Truthy    | `x`              |
| Falsy     | `y`              |

Again, the expression `x or y` doesn’t evaluate to either `True` or `False`. Instead, it returns one of its operands, `x` or `y`.

As you can conclude from the above table, if the left-hand operand is truthy, then you get it as a result. Otherwise, you get the second operand. Here are some examples that demonstrate this behavior:

\>>>

```python
>>> 3 or 4
3

>>> 0 or 4
4

>>> 3 or 0
3
```

In the first example, the left-hand operand is truthy, and `or` immediately returns it. In this case, Python doesn’t evaluate the second operand because it already knows the final result. In the second example, the left-hand operand is falsy, and Python has to evaluate the right-hand one to determine the result.

In the last example, the left-hand operand is truthy, and that fact defines the result of the expression. There’s no need to evaluate the right-hand operand.

An expression like `x or y` is truthy if either `x` or `y` is truthy, and falsy if both `x` and `y` are falsy. This type of expression returns the first truthy operand that it finds. If both operands are falsy, then the expression returns the right-hand operand. To see this latter behavior in action, consider the following example:

In this specific expression, both operands are falsy. So, the `or` operator returns the right-hand operand, and the whole expression is falsy as a result.

Finally, you have the `not` operator. You can also use this one with any object as an operand. Here’s what happens:

| If `x` is | `not x` returns |
| --------- | --------------- |
| Truthy    | `False`         |
| Falsy     | `True`          |

The `not` operator has a uniform behavior. It always returns a Boolean value. This behavior differs from its sibling operators, `and` and `or`.

Here are some code examples:

\>>>

```python
>>> not 3
False

>>> not 0
True
```

In the first example, the operand, `3`, is truthy from Python’s point of view. So, the operator returns `False`. In the second example, the operand is falsy, and `not` returns `True`.

In summary, the Python `not` operator negates the truth value of an object and always returns a Boolean value. This latter behavior differs from the behavior of its sibling operators `and` and `or`, which return operands rather than Boolean values.

### Compound Logical Expressions and Short-Circuit Evaluation[](https://realpython.com/python-operators-expressions/#compound-logical-expressions-and-short-circuit-evaluation "Permanent link")

So far, you’ve seen expressions with only a single `or` or `and` operator and two operands. However, you can also create compound logical expressions with multiple logical operators and operands.

To illustrate how to create a compound expression using `or`, consider the following toy example:

```python
x1 or x2 or x3 or ... or xn
```

This expression returns the first truthy value. If all the preceding `x` variables are falsy, then the expression returns the last value, `xn`.

To help demonstrate short-circuit evaluation, suppose that you have an [identity function](https://en.wikipedia.org/wiki/Identity_function), `f()`, that behaves as follows:

- Takes a single argument
- Displays the function and its argument on the screen
- Returns the argument as its return value

Here’s the code to define this function and also a few examples of how it works:

\>>>

```python
>>> def f(arg):
...     print(f"-> f({arg}) = {arg}")
...     return arg
...

>>> f(0)
-> f(0) = 0
0

>>> f(False)
-> f(False) = False
False

>>> f(1.5)
-> f(1.5) = 1.5
1.5
```

The `f()` function displays its argument, which visually confirms whether you called the function. It also returns the argument as you passed it in the call. Because of this behavior, you can make the expression `f(arg)` be truthy or falsy by specifying a value for `arg` that’s truthy or falsy, respectively.

Now, consider the following compound logical expression:

\>>>

```python
>>> f(0) or f(False) or f(1) or f(2) or f(3)
-> f(0) = 0
-> f(False) = False
-> f(1) = 1
1
```

In this example, Python first evaluates `f(0)`, which returns `0`. This value is falsy. The expression isn’t true yet, so the evaluation continues from left to right. The next operand, `f(False)`, returns `False`. That value is also falsy, so the evaluation continues.

Next up is `f(1)`. That evaluates to `1`, which is truthy. At that point, Python stops the evaluation because it already knows that the entire expression is truthy. Consequently, Python returns `1` as the value of the expression and never evaluates the remaining operands, `f(2)` and `f(3)`. You can confirm from the output that the `f(2)` and `f(3)` calls don’t occur.

A similar behavior appears in an expression with multiple `and` operators like the following one:

```python
x1 and x2 and x3 and ... and xn
```

This expression is truthy if all the operands are truthy. If at least one operand is falsy, then the expression is also falsy.

In this example, short-circuit evaluation dictates that Python stops evaluating as soon as an operand happens to be falsy. At that point, the entire expression is known to be false. Once that’s the case, Python stops evaluating operands and returns the falsy operand that terminated the evaluation.

Here are two examples that confirm the short-circuiting behavior:

\>>>

```python
>>> f(1) and f(False) and f(2) and f(3)
-> f(1) = 1
-> f(False) = False
False

>>> f(1) and f(0.0) and f(2) and f(3)
-> f(1) = 1
-> f(0.0) = 0.0
0.0
```

In both examples, the evaluation stops at the first falsy term—`f(False)` in the first case, `f(0.0)` in the second case—and neither the `f(2)` nor the `f(3)` call occurs. In the end, the expressions return `False` and `0.0`, respectively.

If all the operands are truthy, then Python evaluates them all and returns the last (rightmost) one as the value of the expression:

\>>>

```python
>>> f(1) and f(2.2) and f("Hello")
-> f(1) = 1
-> f(2.2) = 2.2
-> f(Hello) = Hello
'Hello'

>>> f(1) and f(2.2) and f(0)
-> f(1) = 1
-> f(2.2) = 2.2
-> f(0) = 0
0
```

In the first example, all the operands are truthy. The expression is also truthy and returns the last operand. In the second example, all the operands are truthy except for the last one. The expression is falsy and returns the last operand.

### Idioms That Exploit Short-Circuit Evaluation[](https://realpython.com/python-operators-expressions/#idioms-that-exploit-short-circuit-evaluation "Permanent link")

As you dig into Python, you’ll find that there are some common idiomatic patterns that exploit short-circuit evaluation for conciseness of expression, performance, and safety. For example, you can take advantage of this type of evaluation for:

- Avoiding an exception
- Providing a default value
- Skipping a costly operation

To illustrate the first point, suppose you have two variables, `a` and `b`, and you want to know whether the division of `b` by `a` results in a number greater than `0`. In this case, you can run the following expression or condition:

\>>>

```python
>>> a = 3
>>> b = 1

>>> (b / a) > 0
True
```

This code works. However, you need to account for the possibility that `a` might be `0`, in which case you’ll get an [exception](https://realpython.com/python-exceptions/):

\>>>

```python
>>> a = 0
>>> b = 1

>>> (b / a) > 0
Traceback (most recent call last):
    ...
ZeroDivisionError: division by zero
```

In this example, the divisor is `0`, which makes Python raise a `ZeroDivisionError` exception. This exception breaks your code. You can skip this error with an expression like the following:

\>>>

```python
>>> a = 0
>>> b = 1

>>> a != 0 and (b / a) > 0
False
```

When `a` is `0`, `a != 0` is false. Python’s short-circuit evaluation ensures that the evaluation stops at that point, which means that `(b / a)` never runs, and the error never occurs.

Using this technique, you can implement a function to determine whether an integer is divisible by another integer:

```python
def is_divisible(a, b):
    return b != 0 and a % b == 0
```

In this function, if `b` is `0`, then `a / b` isn’t defined. So, the numbers aren’t divisible. If `b` is different from `0`, then the result will depend on the remainder of the division.

Selecting a default value when a specified value is falsy is another idiom that takes advantage of the short-circuit evaluation feature of Python’s logical operators.

For example, say that you have a variable that’s supposed to contain a country’s name. At some point, this variable can end up holding an empty string. If that’s the case, then you’d like the variable to hold a default county name. You can also do this with the `or` operator:

\>>>

```python
>>> country = "Canada"
>>> default_country = "United States"

>>> country or default_country
'Canada'

>>> country = ""
>>> country or default_country
'United States'
```

If `country` is non-empty, then it’s truthy. In this scenario, the expression will return the first truthy value, which is `country` in the first `or` expression. The evaluation stops, and you get `"Canada"` as a result.

On the other hand, if `country` is an empty [string](https://realpython.com/python-strings/), then it’s falsy. The evaluation continues to the next operand, `default_country`, which is truthy. Finally, you get the default country as a result.

Another interesting use case for short-circuit evaluation is to avoid costly operations while creating compound logical expressions. For example, if you have a costly operation that should only run if a given condition is false, then you can use `or` like in the following snippet:

```python
data_is_clean or clean_data(data)
```

In this construct, your `clean_data()` function represents a costly operation. Because of short-circuit evaluation, this function will only run when `data_is_clean` is false, which means that your data isn’t clean.

Another variation of this technique is when you want to run a costly operation if a given condition is true. In this case, you can use the `and` operator:

```python
data_is_updated and process_data(data)
```

In this example, the `and` operator evaluates `data_is_updated`. If this variable is true, then the evaluation continues, and the `process_data()` function runs. Otherwise, the evaluation stops, and `process_data()` never runs.

### Compound vs Chained Expressions[](https://realpython.com/python-operators-expressions/#compound-vs-chained-expressions "Permanent link")

Sometimes you have a compound expression that uses the `and` operator to join comparison expressions. For example, say that you want to determine if a number is in a given interval. You can solve this problem with a compound expression like the following:

\>>>

```python
>>> number = 5
>>> number >= 0 and number <= 10
True

>>> number = 42
>>> number >= 0 and number <= 10
False
```

In this example, you use the `and` operator to join two comparison expressions that allow you to find out if `number` is in the interval from `0` to `10`, both included.

In Python, you can make this compound expression more concise by chaining the comparison operators together. For example, the following chained expression is equivalent to the previous compound one:

\>>>

```python
>>> number = 5
>>> 0 <= number <= 10
True
```

This expression is more concise and readable than the original expression. You can quickly realize that this code is checking if the number is between `0` and `10`. Note that in most programming languages, this chained expression doesn’t make sense. In Python, it works like a charm.

In other programming languages, this expression would probably start by evaluating `0 <= number`, which is true. This true value would then be compared with `10`, which doesn’t make much sense, so the expression fails.

Python internally processes this type of expression as an equivalent `and` expression, such as `0 <= number and number <= 10`. That’s why you get the correct result in the example above.

## Conditional Expressions or the Ternary Operator[](https://realpython.com/python-operators-expressions/#conditional-expressions-or-the-ternary-operator "Permanent link")

Python has what it calls [conditional expressions](https://docs.python.org/3/reference/expressions.html#conditional-expressions). These kinds of expressions are inspired by the [ternary operator](https://en.wikipedia.org/wiki/Ternary_conditional_operator) that looks like `a ? b : c` and is used in other programming languages. This construct evaluates to `b` if the value of `a` is true, and otherwise evaluates to `c`. Because of this, sometimes the equivalent Python syntax is also known as the ternary operator.

However, in Python, the expression looks more readable:

```python
variable = expression_1 if condition else expression_2
```

This expression returns `expression_1` if the condition is true and `expression_2` otherwise. Note that this expression is equivalent to a regular conditional like the following:

```python
if condition:
    variable = expression_1
else:
    variable = expression_2
```

So, why does Python need this syntax? [PEP 308](https://peps.python.org/pep-0308/) introduced conditional expressions as an effort to avoid the prevalence of error-prone attempts to achieve the same effect of a traditional ternary operator using the `and` and `or` operators in an expression like the following:

```python
variable = condition and expression_1 or expression_2
```

However, this expression doesn’t work as expected, returning `expression_2` when `expression_1` is falsy.

Some Python developers would avoid the syntax of conditional expressions in favor of a regular conditional statement. In any case, this syntax can be handy in some situations because it provides a concise tool for writing two-way conditionals.

Here’s an example of how to use the conditional expression syntax in your code:

\>>>

```python
>>> day = "Sunday"
>>> open_time = "11AM" if day == "Sunday" else "9AM"
>>> open_time
'11AM'

>>> day = "Monday"
>>> open_time = "11AM" if day == "Sunday" else "9AM"
>>> open_time
'9AM'
```

When `day` is equal to `"Sunday"`, the condition is true and you get the first expression, `"11AM"`, as a result. If the condition is false, then you get the second expression, `"9AM"`. Note that similarly to the `and` and `or` operators, the conditional expression returns the value of one of its expressions rather than a Boolean value.

## Identity Operators and Expressions in Python[](https://realpython.com/python-operators-expressions/#identity-operators-and-expressions-in-python "Permanent link")

Python provides two operators, `is` and `is not`, that allow you to determine whether two operands have the same **identity**. In other words, they let you check if the operands refer to the same object. Note that identity isn’t the same thing as equality. The latter aims to check whether two operands contain the same data.

Here’s a summary of Python’s identity operators. Note that `x` and `y` are variables that point to objects:

| Operator                                                                | Sample Expression | Result                                                                           |
| ----------------------------------------------------------------------- | ----------------- | -------------------------------------------------------------------------------- |
| [`is`](https://docs.python.org/3/reference/expressions.html#is)         | `x is y`          | • `True` if `x` and `y` hold a reference to the same in-memory object            |
| • `False` otherwise                                                     |                   |                                                                                  |
| [`is not`](https://docs.python.org/3/reference/expressions.html#is-not) | `x is not y`      | • `True` if `x` points to an object different from the object that `y` points to |
| • `False` otherwise                                                     |                   |                                                                                  |

These two Python operators are keywords instead of odd symbols. This is part of Python’s goal of favoring readability in its syntax.

Here’s an example of two variables, `x` and `y`, that refer to objects that are equal but not identical:

\>>>

```python
>>> x = 1001
>>> y = 1001

>>> x == y
True

>>> x is y
False
```

In this example, `x` and `y` refer to objects whose value is `1001`. So, they’re equal. However, they don’t reference the same object. That’s why the `is` operator returns `False`. You can check an object’s identity using the built-in `id()` function:

\>>>

```python
>>> id(x)
4417772080

>>> id(y)
4417766416
```

As you can conclude from the `id()` output, `x` and `y` don’t have the same identity. So, they’re different objects, and because of that, the expression `x is y` returns `False`. In other words, you get `False` because you have two different instances of `1001` stored in your computer’s memory.

When you make an assignment like `y = x`, Python creates a second reference to the same object. Again, you can confirm that with the `id()` function or the `is` operator:

\>>>

```python
>>> a = "Hello, Pythonista!"
>>> b = a

>>> id(a)
4417651936
>>> id(b)
4417651936

>>> a is b
True
```

In this example, `a` and `b` hold references to the same object, the string `"Hello, Pythonista!"`. Therefore, the `id()` function returns the same identity when you call it with `a` and `b`. Similarly, the `is` operator returns `True`.

Finally, the `is not` operator is the opposite of `is`. So, you can use `is not` to determine if two names _don’t_ refer to the same object:

\>>>

```python
>>> x = 1001
>>> y = 1001
>>> x is not y
True

>>> a = "Hello, Pythonista!"
>>> b = a
>>> a is not b
False
```

In the first example, because `x` and `y` point to different objects in your computer’s memory, the `is not` operator returns `True`. In the second example, because `a` and `b` are references to the same object, the `is not` operator returns `False`.

Again, the `is not` operator highlights Python’s readability goals. In general, both identity operators allow you to write checks that read as plain English.

## Membership Operators and Expressions in Python[](https://realpython.com/python-operators-expressions/#membership-operators-and-expressions-in-python "Permanent link")

Sometimes you need to determine whether a value is present in a container data type, such as a list, tuple, or set. In other words, you may need to check if a given value _is_ or _is not_ a **member** of a collection of values. Python calls this kind of check a [membership test](https://docs.python.org/3/reference/expressions.html#membership-test-operations).

Membership tests are quite common and useful in programming. As with many other common operations, Python has dedicated operators for membership tests. The table below lists the **membership operators** in Python:

| Operator                                                                | Sample Expression         | Result                                                         |
| ----------------------------------------------------------------------- | ------------------------- | -------------------------------------------------------------- |
| [`in`](https://docs.python.org/3/reference/expressions.html#in)         | `value in collection`     | • `True` if `value` _is_ present in `collection`               |
| • `False` otherwise                                                     |                           |                                                                |
| [`not in`](https://docs.python.org/3/reference/expressions.html#not-in) | `value not in collection` | • `True` if `value` _is not_ present in `collection` of values |
| • `False` otherwise                                                     |                           |                                                                |

As usual, Python favors readability by using English words as operators instead of potentially confusing symbols or combinations of symbols.

The Python `in` and `not in` operators are binary. This means that you can create membership expressions by connecting two operands with either operator. However, the operands in a membership expression have particular characteristics:

- **Left operand**: The value that you want to look for in a collection of values
- **Right operand**: The collection of values where the target value may be found

To better understand the `in` operator, below you have two demonstrative examples consisting of determining whether a value is in a list:

\>>>

```python
>>> 5 in [2, 3, 5, 9, 7]
True

>>> 8 in [2, 3, 5, 9, 7]
False
```

The first expression returns `True` because `5` is in the list of numbers. The second expression returns `False` because `8` isn’t in the list.

The `not in` membership operator runs the opposite test as the `in` operator. It allows you to check whether an integer value _is not_ in a collection of values:

\>>>

```python
>>> 5 not in [2, 3, 5, 9, 7]
False

>>> 8 not in [2, 3, 5, 9, 7]
True
```

In the first example, you get `False` because `5` is in the target list. In the second example, you get `True` because `8` isn’t in the list of values. This may sound like a tongue twister because of the negative logic. To avoid confusion, remember that you’re trying to determine if the value _is not_ part of a given collection of values.

## Concatenation and Repetition Operators and Expressions[](https://realpython.com/python-operators-expressions/#concatenation-and-repetition-operators-and-expressions "Permanent link")

There are two operators in Python that acquire a slightly different meaning when you use them with sequence data types, such as lists, tuples, and strings. With these types of operands, the `+` operator defines a **concatenation operator**, and the `*` operator represents the **repetition operator**:

| Operator | Operation     | Sample Expression | Result                                                          |
| -------- | ------------- | ----------------- | --------------------------------------------------------------- |
| `+`      | Concatenation | `seq_1 + seq_2`   | A new sequence containing all the items from both operands      |
| `*`      | Repetition    | `seq * n`         | A new sequence containing the items of `seq` repeated `n` times |

Both operators are binary. The concatenation operator takes two sequences as operands and returns a new sequence of the same type. The repetition operator takes a sequence and an integer number as operands. Like in regular multiplication, the order of the operands doesn’t alter the repetition’s result.

Here are some examples of how the concatenation operator works in practice:

\>>>

```python
>>> "Hello, " + "World!"
'Hello, World!'

>>> ("A", "B", "C") + ("D", "E", "F")
('A', 'B', 'C', 'D', 'E', 'F')

>>> [0, 1, 2, 3] + [4, 5, 6]
[0, 1, 2, 3, 4, 5, 6]
```

In the first example, you use the concatenation operator (`+`) to join two strings together. The operator returns a completely new string object that combines the two original strings.

In the second example, you concatenate two tuples of letters together. Again, the operator returns a new tuple object containing all the items from the original operands. In the final example, you do something similar but this time with two lists.

When it comes to the repetition operator, the idea is to repeat the content of a given sequence a certain number of times. Here are a few examples:

\>>>

```python
>>> "Hello" * 3
'HelloHelloHello'
>>> 3 * "World!"
'World!World!World!'

>>> ("A", "B", "C") * 3
('A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C')

>>> 3 * [1, 2, 3]
[1, 2, 3, 1, 2, 3, 1, 2, 3]
```

In the first example, you use the repetition operator (`*`) to repeat the `"Hello"` string three times. In the second example, you change the order of the operands by placing the integer number on the left and the target string on the right. This example shows that the order of the operands doesn’t affect the result.

The next examples use the repetition operators with a tuple and a list, respectively. In both cases, you get a new object of the same type containing the items in the original sequence repeated three times.

## The Walrus Operator and Assignment Expressions[](https://realpython.com/python-operators-expressions/#the-walrus-operator-and-assignment-expressions "Permanent link")

Regular assignment statements with the `=` operator don’t have a return value, as you already learned. Instead, the assignment operator creates or updates variables. Because of this, the operator can’t be part of an expression.

Since [Python 3.8](https://realpython.com/python38-new-features/), you have access to a new operator that allows for a new type of assignment. This new assignment is called **assignment expression** or **named expression**. The new operator is called the **walrus operator**, and it’s the combination of a colon and an equal sign (`:=`).

Unlike regular assignments, assignment expressions do have a return value, which is why they’re _expressions_. So, the operator accomplishes two tasks:

1. Returns the expression’s result
2. Assigns the result to a variable

The walrus operator is also a binary operator. Its left-hand operand must be a variable name, and its right-hand operand can be any Python expression. The operator will evaluate the expression, assign its value to the target variable, and return the value.

The general syntax of an assignment expression is as follows:

This expression looks like a regular assignment. However, instead of using the assignment operator (`=`), it uses the walrus operator (`:=`). For the expression to work correctly, the enclosing parentheses are required in most use cases. However, in certain situations, you won’t need them. Either way, they won’t hurt you, so it’s safe to use them.

Assignment expressions come in handy when you want to reuse the result of an expression or part of an expression without using a dedicated assignment to grab this value beforehand. It’s particularly useful in the context of a conditional statement. To illustrate, the example below shows a toy function that checks the length of a string object:

\>>>

```python
>>> def validate_length(string):
...     if (n := len(string)) < 8:
...         print(f"Length {n} is too short, needs at least 8")
...     else:
...         print(f"Length {n} is okay!")
...

>>> validate_length("Pythonista")
Length 10 is okay!

>>> validate_length("Python")
Length 6 is too short, needs at least 8
```

In this example, you use a conditional statement to check whether the input string has fewer than `8` characters.

The assignment expression, `(n := len(string))`, computes the string length and assigns it to `n`. Then it returns the value that results from calling `len()`, which finally gets compared with `8`. This way, you guarantee that you have a reference to the string length to use in further operations.

## Bitwise Operators and Expressions in Python[](https://realpython.com/python-operators-expressions/#bitwise-operators-and-expressions-in-python "Permanent link")

**Bitwise operators** treat operands as sequences of [binary](https://realpython.com/python-bitwise-operators/#binary-system-in-five-minutes) digits and operate on them bit by bit. Currently, Python supports the following bitwise operators:

| Operator                                                               | Operation                  | Sample Expression | Result                                                                                                              |
| ---------------------------------------------------------------------- | -------------------------- | ----------------- | ------------------------------------------------------------------------------------------------------------------- |
| `&`                                                                    | Bitwise AND                | `a & b`           | • Each bit position in the result is the logical AND of the bits in the corresponding position of the operands.     |
| • `1` if both bits are `1`, otherwise `0`.                             |                            |                   |                                                                                                                     |
| `                                                                      | `                          | Bitwise OR        | `a                                                                                                                  |
| • `1` if either bit is `1`, otherwise `0`.                             |                            |                   |                                                                                                                     |
| `~`                                                                    | Bitwise NOT                | `~a`              | • Each bit position in the result is the logical negation of the bit in the corresponding position of the operand.  |
| • `1` if the bit is `0` and `0` if the bit is `1`.                     |                            |                   |                                                                                                                     |
| `^`                                                                    | Bitwise XOR (exclusive OR) | `a ^ b`           | • Each bit position in the result is the logical **XOR** of the bits in the corresponding position of the operands. |
| • `1` if the bits in the operands are different, `0` if they’re equal. |                            |                   |                                                                                                                     |
| `>>`                                                                   | Bitwise right shift        | `a >> n`          | Each bit is shifted right `n` places.                                                                               |
| `<<`                                                                   | Bitwise left shift         | `a << n`          | Each bit is shifted left `n` places.                                                                                |

As you can see in this table, most bitwise operators are binary, which means that they expect two operands. The bitwise NOT operator (`~`) is the only unary operator because it expects a single operand, which should always appear at the right side of the expression.

You can use Python’s bitwise operators to manipulate your data at its most granular level, the bits. These operators are commonly useful when you want to write low-level algorithms, such as compression, encryption, and others.

Here are some examples that illustrate how some of the bitwise operators work in practice:

\>>>

```python
>>> # Bitwise AND
>>> #   0b1100    12
>>> # & 0b1010    10
>>> # --------
>>> # = 0b1000     8
>>> bin(0b1100 & 0b1010)
'0b1000'
>>> 12 & 10
8

>>> # Bitwise OR
>>> #   0b1100    12
>>> # | 0b1010    10
>>> # --------
>>> # = 0b1110    14
>>> bin(0b1100 | 0b1010)
'0b1110'
>>> 12 | 10
14
```

In the first example, you use the bitwise AND operator. The commented lines begin with `#` and provide a visual representation of what happens at the bit level. Note how each bit in the result is the logical AND of the bits in the corresponding position of the operands.

The second example shows how the bitwise OR operator works. In this case, the resulting bits are the logical OR test of the corresponding bits in the operands.

In all the examples, you’ve used the built-in `bin()` function to display the result as a binary object. If you don’t wrap the expression in a call to `bin()`, then you’ll get the integer representation of the output.

## Operator Precedence in Python[](https://realpython.com/python-operators-expressions/#operator-precedence-in-python "Permanent link")

Up to this point, you’ve coded sample expressions that mostly use one or two different types of operators. However, what if you need to create compound expressions that use several different types of operators, such as comparison, arithmetic, Boolean, and others? How does Python decide which operation runs first?

Consider the following math expression:

There might be ambiguity in this expression. Should Python perform the addition `20 + 4` first and then multiply the result by `10`? Should Python run the multiplication `4 * 10` first, and the addition second?

Because the result is `60`, you can conclude that Python has chosen the latter approach. If it had chosen the former, then the result would be `240`. This follows a standard algebraic rule that you’ll find in virtually all programming languages.

All operators that Python supports have a [precedence](https://docs.python.org/3/reference/expressions.html#operator-precedence) compared to other operators. This precedence defines the order in which Python runs the operators in a compound expression.

In an expression, Python runs the operators of highest precedence first. After obtaining those results, Python runs the operators of the next highest precedence. This process continues until the expression is fully evaluated. Any operators of equal precedence are performed in left-to-right order.

Here’s the order of precedence of the Python operators that you’ve seen so far, from highest to lowest:

| Operators                                                        | Description                                                                                        |
| ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| `**`                                                             | Exponentiation                                                                                     |
| `+x`, `-x`, `~x`                                                 | Unary positive, unary negation, bitwise negation                                                   |
| `*`, `/`, `//`, `%`                                              | Multiplication, division, floor division, [modulo](https://realpython.com/python-modulo-operator/) |
| `+`, `-`                                                         | Addition, subtraction                                                                              |
| `<<`, `>>`                                                       | Bitwise shifts                                                                                     |
| `&`                                                              | Bitwise AND                                                                                        |
| `^`                                                              | Bitwise XOR                                                                                        |
| `                                                                | `                                                                                                  |
| `==`, `!=`, `<`, `<=`, `>`, `>=`, `is`, `is not`, `in`, `not in` | Comparisons, identity, and membership                                                              |
| `not`                                                            | Boolean NOT                                                                                        |
| `and`                                                            | Boolean AND                                                                                        |
| `or`                                                             | Boolean OR                                                                                         |
| `:=`                                                             | Walrus                                                                                             |

Operators at the top of the table have the highest precedence, and those at the bottom of the table have the lowest precedence. Any operators in the same row of the table have equal precedence.

Getting back to your initial example, Python runs the multiplication because the multiplication operator has a higher precedence than the addition one.

Here’s another illustrative example:

\>>>

```python
>>> 2 * 3 ** 4 * 5
810
```

In the example above, Python first raises `3` to the power of `4`, which equals `81`. Then, it carries out the multiplications in order from left to right: `2 * 81 = 162` and `162 * 5 = 810`.

You can override the default operator precedence using parentheses to group terms as you do in math. The subexpressions in parentheses will run before expressions that aren’t in parentheses.

Here are some examples that show how a pair of parentheses can affect the result of an expression:

\>>>

```python
>>> (20 + 4) * 10
240

>>> 2 * 3 ** (4 * 5)
6973568802
```

In the first example, Python computes the expression `20 + 4` first because it’s wrapped in parentheses. Then Python multiplies the result by `10`, and the expression returns `240`. This result is completely different from what you got at the beginning of this section.

In the second example, Python evaluates `4 * 5` first. Then it raises `3` to the power of the resulting value. Finally, Python multiplies the result by `2`, returning `6973568802`.

There’s nothing wrong with making liberal use of parentheses, even when they aren’t necessary to change the order of evaluation. Sometimes it’s a good practice to use parentheses because they can improve your code’s readability and relieve the reader from having to recall operator precedence from memory.

Consider the following example:

Here the parentheses are unnecessary, as the comparison operators have higher precedence than `and`. However, some might find the parenthesized version clearer than the version without parentheses:

On the other hand, some developers might prefer this latter version of the expression. It’s a matter of personal preference. The point is that you can always use parentheses if you feel that they make your code more readable, even if they aren’t necessary to change the order of evaluation.

## Augmented Assignment Operators and Expressions[](https://realpython.com/python-operators-expressions/#augmented-assignment-operators-and-expressions "Permanent link")

So far, you’ve learned that a single equal sign (`=`) represents the assignment operator and allows you to assign a value to a variable. Having a right-hand operand that contains other variables is perfectly valid, as you’ve also learned. In particular, the expression to the right of the assignment operator can include the same variable that’s on the left of the operand.

That last sentence may sound confusing, so here’s an example that clarifies the point:

\>>>

```python
>>> total = 10
>>> total = total + 5
>>> total
15
```

In this example, `total` is an **accumulator** variable that you use to _accumulate_ successive values. You should read this example as _`total` is equal to the current value of `total` plus `5`_. This expression effectively increases the value of `total`, which is now `15`.

Note that this type of assignment only makes sense if the variable in question already has a value. If you try the assignment with an undefined variable, then you get an error:

\>>>

```python
>>> count = count + 1
Traceback (most recent call last):
    ...
NameError: name 'count' is not defined. Did you mean: 'round'?
```

In this example, the `count` variable isn’t defined before the assignment, so it doesn’t have a current value. In consequence, Python raises a [`NameError`](https://realpython.com/python-traceback/#nameerror) exception to let you know about the issue.

This type of assignment helps you create accumulators and counter variables, for example. Therefore, it’s quite a common task in programming. As in many similar cases, Python offers a more convenient solution. It supports a shorthand syntax called [augmented assignment](https://realpython.com/python-assignment-operator/#augmented-assignment-operators-in-python):

\>>>

```pyt
>>> total = 10
>>> total += 5
>>> total
15
```

In the highlighted line, you use the augmented addition operator (`+=`). With this operator, you create an assignment that’s fully equivalent to `total = total + 5`.

Python supports many augmented assignment operators. In general, the syntax for this type of assignment looks something like this:

Note that the dollar sign (`$`) isn’t a valid Python operator. In this example, it’s a placeholder for a generic operator. The above statement works as follows:

1. Evaluate `expression` to produce a value.
2. Run the operation defined by the operator that prefixes the assignment operator (`=`), using the current value of `variable` and the return value of `expression` as operands.
3. Assign the resulting value back to `variable`.

The table below shows a summary of the augmented operators for arithmetic operations:

| Operator | Description                                                                                                                                                               | Sample Expression | Equivalent Expression |
| -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------- | --------------------- |
| `+=`     | Adds the right operand to the left operand and stores the result in the left operand                                                                                      | `x += y`          | `x = x + y`           |
| `-=`     | Subtracts the right operand from the left operand and stores the result in the left operand                                                                               | `x -= y`          | `x = x - y`           |
| `*=`     | Multiplies the right operand with the left operand and stores the result in the left operand                                                                              | `x *= y`          | `x = x * y`           |
| `/=`     | Divides the left operand by the right operand and stores the result in the left operand                                                                                   | `x /= y`          | `x = x / y`           |
| `//=`    | Performs [floor division](https://docs.python.org/3/glossary.html#term-floor-division) of the left operand by the right operand and stores the result in the left operand | `x //= y`         | `x = x // y`          |
| `%=`     | Finds the remainder of dividing the left operand by the right operand and stores the result in the left operand                                                           | `x %= y`          | `x = x % y`           |
| `**=`    | Raises the left operand to the power of the right operand and stores the result in the left operand                                                                       | `x **= y`         | `x = x**y`            |

As you can conclude from this table, all the arithmetic operators have an augmented version in Python. You can use these augmented operators as a shortcut when creating accumulators, counters, and similar objects.

Did the augmented arithmetic operators look neat and useful to you? The good news is that there are more. You also have augmented bitwise operators in Python:

| Operator | Operation                                                                                   | Example                                                                                 | Equivalent   |
| -------- | ------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------- | ------------ |
| `&=`     | Augmented bitwise AND ([conjunction](https://en.wikipedia.org/wiki/Logical_conjunction))    | `x &= y`                                                                                | `x = x & y`  |
| `        | =`                                                                                          | Augmented bitwise OR ([disjunction](https://en.wikipedia.org/wiki/Logical_disjunction)) | `x           |
| `^=`     | Augmented bitwise XOR ([exclusive disjunction](https://en.wikipedia.org/wiki/Exclusive_or)) | `x ^= y`                                                                                | `x = x ^ y`  |
| `>>=`    | Augmented bitwise right shift                                                               | `x >>= y`                                                                               | `x = x >> y` |
| `<<=`    | Augmented bitwise left shift                                                                | `x <<= y`                                                                               | `x = x << y` |

Finally, the concatenation and repetition operators have augmented variations too. These variations behave differently with mutable and immutable data types:

| Operator                                                                                             | Description                                                         | Example |
| ---------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------- |
| `+=`                                                                                                 | • Runs an augmented concatenation operation on the target sequence. |         |
| • Mutable sequences are updated in place.                                                            |                                                                     |         |
| • If the sequence is immutable, then a new sequence is created and assigned back to the target name. | `seq_1 += seq_2`                                                    |         |
| `*=`                                                                                                 | • Adds `seq` to itself `n` times.                                   |         |
| • Mutable sequences are updated in place.                                                            |                                                                     |         |
| • If the sequence is immutable, then a new sequence is created and assigned back to the target name. | `seq *= n`                                                          |         |

Note that the augmented [concatenation operator](https://realpython.com/python-string-concatenation/#doing-string-concatenation-with-pythons-plus-operator) works on two sequences, while the augmented [repetition operator](https://realpython.com/python-string-concatenation/#doing-repeated-concatenation-with-the-star-operator) works on a sequence and an integer number.

## Conclusion[](https://realpython.com/python-operators-expressions/#conclusion "Permanent link")

Now you know what **operators** Python supports and how to use them. Operators are symbols, combinations of symbols, or keywords that you can use along with Python objects to build different types of **expressions** and perform computations in your code.

**In this tutorial, you’ve learned:**

- What Python’s **arithmetic operators** are and how to use them in **arithmetic expressions**
- What Python’s **comparison**, **Boolean**, **identity**, **membership** operators are
- How to write **expressions** using comparison, Boolean, identity, and membership operators
- Which **bitwise** operators Python supports and how to use them
- How to combine and repeat sequences using the **concatenation** and **repetition** operators
- What the **augmented assignment** operators are and how they work

In other words, you’ve covered an awful lot of ground! If you’d like a handy cheat sheet that can jog your memory on all that you’ve learned, then click the link below:

With all this knowledge about operators, you’re better prepared as a Python developer. You’ll be able to write better and more robust expressions in your code.