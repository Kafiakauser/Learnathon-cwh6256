sentence = input("Enter a sentence : ")

# check if sentence has at least 10 characters
if len(sentence) >= 10: 
    extracted_substring = sentence[4:10]
    print("Extracted Substring: ",extracted_substring)
else:
    print("Input sentence should have at least 10 characters.")



#reverse of a string
str = "Kafia"
Reverse_str = str[::-1]
print("Reverse : ",Reverse_str)

#Check the alphanumeric characters 
Str = "Kafia50170"
print(str.isalnum())




#to check the count of a character

str = "abracadabracobra"
print(str.count("abra"))