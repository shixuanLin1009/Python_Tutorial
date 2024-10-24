\ Model facility_location
\ LP format - for model browsing. Use MPS format to capture full model detail.
Minimize
  11 x(1,1) + 27 x(1,2) + 38 x(1,3) + 22 x(2,1) + 17 x(2,2) + 50 x(2,3)
   + 30 y(1) + 17 y(2)
Subject To
 R0: x(1,1) + x(1,2) + x(1,3) - 30 y(1) <= 0
 R1: x(2,1) + x(2,2) + x(2,3) - 25 y(2) <= 0
 R2: x(1,1) + x(2,1) = 16
 R3: x(1,2) + x(2,2) = 11
 R4: x(1,3) + x(2,3) = 16
Bounds
Binaries
 y(1) y(2)
End
