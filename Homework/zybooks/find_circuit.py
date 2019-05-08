# Determines whether a graph has a circuit or not 
""" 
Find a vertex w, that is not an isolated vertex.
Select any edge {w, x} incident to w. (Since w is not isolated, 
there is always at least one such edge.)
Current trail T := ⟨
w, x⟩
last := x
While there is an edge {last, y} that has not been used in T:
          Add y to the end of T
          last := y """
