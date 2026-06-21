# Use index or find to find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'

sentence = 'You cannot end a sentence with because because because is a conjunction'
first_occurrence = sentence.find('because')
print(f"The first occurrence of 'because' is at index: {first_occurrence}")

# Use rindex to find the position of the last occurrence of the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
position_last_occurrence = sentence.rindex('because')
print(f"The last occurrence of 'because' is at index: {position_last_occurrence}")



# Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
print(sentence[31:54])


# Find the position of the first occurrence of the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
position_first_occurrence = sentence.find('because')
print(f"The first occurrence of 'because' is at index: {position_first_occurrence}")



#Slice out the phrase 'because because because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
sliced_phrase = sentence[31:54]
print(f"Sliced phrase: '{sliced_phrase}'")