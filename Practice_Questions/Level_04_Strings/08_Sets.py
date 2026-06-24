
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

