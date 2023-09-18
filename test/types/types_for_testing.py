from typed_lang.types import TypedType, TypedUnion, TypedIntersection, TypedTuple

A = TypedType("A")
B = TypedType("B")
C = TypedType("C")
D = TypedType("D")

A_or_B = TypedUnion([A, B])
A_and_B = TypedIntersection([A, B])

B_or_C = TypedUnion([B, C])
B_and_C = TypedIntersection([B, C])

C_or_D = TypedUnion([C, D])
C_and_D = TypedIntersection([C, D])

AB = TypedTuple([A, B])
BA = TypedTuple([B, A])
