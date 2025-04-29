# # Terminal type declarations
# @A
# @B
# @C

# # Type definitions
# MyType = A

# # Type union
# Union = A | B

# # Parameterized type definitions
# Identity[T] = T

# # Parameterized types can be arguments of other parameterized types
# Apply[F, X] = F[X]

# Apply[Identity, A]

# #@A

# #Apply[X, F] = F[X]
# #Identity[X] = X

# #Apply[Identity, A]

@A
@B

# X = (A, A | B, B)
# Y = (A, A, A)

@Animal
@Robot
@Quack
@DuckWalk

RealDuck = Animal & Quack & DuckWalk
RoboDuck = Robot & Quack & DuckWalk
RealDuck ^ RoboDuck

Animal & Animal

#TODO: reduce A & A to A and A | A to A during construction