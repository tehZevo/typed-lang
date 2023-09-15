# Typed (name TBD)
*The most type-safe language*

You will never use the wrong type again. Why? Because in Typed (name TBD), everything is types!

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
