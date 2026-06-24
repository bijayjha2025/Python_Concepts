
it_companies = {"Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"}

print(it_companies)
print(len(it_companies)) #This returns length of the set

#Add 'Twitter' to it_companies
it_companies.add("Twitter")
print(it_companies, len(it_companies))

#Insert multiple IT companies at once to the set it_companies
it_companies.update(["LinkedIn", "Snapchat", "TikTok"])
print(it_companies, len(it_companies))

#Remove one of the companies from the set it_companies
it_companies.remove("Snapchat")
print(it_companies, len(it_companies))

#What is the difference between remove and discard?
# remove() will raise a KeyError if the specified element is not found in the set, while discard() will not raise an error and will simply do nothing if the element is not found.

A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

#Join A and B
C = A.union(B)
print("Union of A and B:", C)

#Find A intersection B
D = A.intersection(B)
print("Intersection of A and B:", D)

#Is A subset of B
isSubset = A.issubset(B)
print("Is A a subset of B?", isSubset)

#Are A and B disjoint sets
areDisjoint = A.isdisjoint(B)
print("Are A and B disjoint sets?", areDisjoint)

#Join A with B and B with A
unionAB = A.union(B)
unionBA = B.union(A)
print("Union of A and B:", unionAB)
print("Union of B and A:", unionBA)


#What is the symmetric difference between A and B
symmetricDifference = A.symmetric_difference(B)
print("Symmetric difference between A and B:", symmetricDifference)

#Delete the sets completely
del A
del B
print(A, B) # This will raise an error since A and B have been deleted