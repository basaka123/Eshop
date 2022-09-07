
class UniqueSubsets:
    def __init__(self, set_of_integers):
        self.set_of_integers = set_of_integers
        
    def getUniqueSubsets(self):
        numOfSubset = int(pow(2, len(self.set_of_integers))) 
        self.set_of_integers = sorted(self.set_of_integers) 
        subset = set()
        
        for i in range(numOfSubset):
            subset_list = []
            for j in range(len(self.set_of_integers)):
                if i & (1 << j):
                   subset_list.append(self.set_of_integers[j])
                
        
            subset.add(tuple(subset_list))
            
        print(subset)
 
 
num = {3,2,1,5,7,1,2}
get_elem = UniqueSubsets(num)

get_elem.getUniqueSubsets()