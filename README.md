# Typed (name TBD)
*The most type-safe language*

You will never use the wrong type again. Why? Because in Typed (name TBD), everything is types!

## Features
* Type-safety
* ADTs (Algebraic Data Types)
  * Sum: union types
  * Product: tuple and intersection types
* Generic types
* Multiple inheritance (TODO)

## Examples
Terminal type declarations; these are your "root" types:
```ts
@A
@B
@C
```

Operators
```ts
// Type union
A | B

// Type intersection
A & B

// Parentheses for precedence
(A | B) & (B | C)
```

Type definitions
```ts
MyType = A | B

// Parameterized!
Box[X] = X

// Types are accepted as arguments to parameterized types too
Apply[F, X] = F[X]
```
