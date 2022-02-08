# Cartesian Crosses

## Example Applications

They are useful in many aspects of programming, especially in conditional logic.

```python

for element_a in array_a:
    for element_b in array_b:
        print((element_a, element_b))
```

There are many other places where they exist, like graph theory, sql and so many other places!

## Clarifying a point from class

when crossing multiple sets, this is the formula:

<!-- &#8712;
&ElementOf; &Epsilon; &epsilon;
&Theta; -->

```
Let A and B and C be sets
A x B = {(a,b) | a ∈ A, b ∈ B}

A x B x C = {(a,b,c) | a ∈ A, b ∈ B, c ∈ C}

```

What this means is that when crossing multiple sets, they assume the form of a single parenthesis tuple **(a,b,c)** and not something like **((a,b),c)**.

You should note that technically, **((a,b),c)** is in fact correct and in some use cases is the correct answer. In a sense, **((a,b),c)** is more technically correct, however for this class, please use the single parenthesis tuple **(a,b,c)** notation.
