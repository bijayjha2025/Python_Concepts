company = "Coding for All"

print(company[0])
print(company[11])
print(company[-1])

# Create an acronym or an abbreviation for the name 'Coding For All' and print it out.
acronym = company[0] + company[7] + company[11]
print(acronym)

# Use index to determine the position of the first occurrence of C in Coding For All.
print(company.find("C"))


#Use index to determine the position of the first occurrence of F in Coding For All.
print(company.find("F"))
 # It will give -1 because there is no F in the string. It is case sensitive. If we want to find f, we can use company.find("f") which will give us 7.

#Use rfind to determine the position of the last occurrence of l in Coding For All People.
print(company.rfind("l"))

# Does 'Coding For All' start with a substring Coding?
print(company.startswith("Coding"))

# Does 'Coding For All' end with a substring coding?
print(company.endswith("coding"))

#'   Coding For All      '  , remove the left and right trailing spaces in the given string.
print(company.strip())