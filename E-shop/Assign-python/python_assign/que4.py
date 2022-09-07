def pascals_tri(n):
   nrow = [4]
   y = [2]
   for n in range(max(n,0)):
      print(nrow) # the variable should be nrow
      # parameter in the zip function should be nrow and the variable to be added is y and not q.
      nrow=[l+4 for l,r in zip(nrow+y, y+nrow)]
   return n>=1
pascals_tri(8) # The function call is missing an "s"