#1 Practice all Methods
#string methods
#upper()
name="mouni"
print(name.upper())

#strip()
print(name.strip())

#startswith()
name="mouni"
print(name.startswith("M"))

#endswith()
name="mouni"
print(name.endswith("m"))

#find()
string="p for apple"
print(string.find("Y"))

#swapcase()
name="mouni"
name.swapcase()
print(name)

#zfill()
name="mouni"
req=5
name=name.zfill(req)
print(name)

#isalpha()
string="hello"
print(string.isalpha())

#center()
name="hello"
print("hello".center(3," "))

#split()
string="hello world from python"
print(string.split("separator"))

#join()
L=["hello world"]
print("".join(L))

#isdigit()
mob="9177538762"
print(mob.isdigit())

#isalnum()
password="hello"
print(password.isalnum())

#2 Take a string it contains both upper and lower case ,print the no of vowels and consonants present in the string
def count_vowels_consonents(s):
    vowels='aeiouAEIOU'
    vowel_count=0
    consonent_count=0
    for char in s:
        if char.isalpha():
            if char in vowels:
                vowel_count+=1
            else:
                consonent_count+=1
    print("vowels:",vowel_count)
    print("consonents:",consonent_count)
string="hello world"
count_vowels_consonents(string)