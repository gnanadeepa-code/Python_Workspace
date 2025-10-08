#String functions
s="hello world"
print(s)
print(len(s)) #length of string --11
print(s.upper()) #uppercase --HELLO WORLD
print(s.lower()) #lowercase --hello world
print(s.title()) #title case   --Hello World
print(s.capitalize()) #first letter capital --Hello world
print(s.count('o')) #count of character --2
print(s.find('o')) #first occurrence of character --4
print(s.rfind('o')) #last occurrence of character --7
print(s.replace('world','Deepa')) #replace substring --hello Deepa
print(s.split()) #split string into list --['hello', 'world']
print(s.split('o')) #split string at 'o' --['hell', ' w
print(s[0]) #first character  --h
print(s[-1]) #last character    --d
print(s[0:5]) #substring from index 0 to 4  --hello
print(s[6:]) #substring from index 6 to end --world
print(s[:5]) #substring from start to index 4 --hello
print(s[::2]) #substring with step 2 --hlool
print(s[::-1]) #reverse string  --dlrow olleh
print(s.strip()) #remove leading and trailing spaces    --hello world
print(s.lstrip()) #remove leading spaces  --hello world
print(s.isalpha()) #check if all characters are alphabetic --False because of space
print(s.isdigit()) #check if all characters are digits  --False
print(s.isalnum()) #check if all characters are alphanumeric    --False because of space
print(s.startswith('h')) #check if string starts with 'h'   --True
print(s.endswith('d')) #check if string ends with 'd'   --True
print(s.index('o')) #index of first occurrence of 'o'   --4
print(s.rindex('o')) #index of last occurrence of 'o'   --7
print(s.swapcase()) #swap case of characters    --HELLO WORLD
print(s.center(20,'*')) #center string with padding     --****hello world*****
print(s.ljust(20,'*')) #left justify string with padding    --hello world*********
print(s.rjust(20,'*')) #right justify string with padding   --*********hello world
print(s.encode()) #encode string to bytes   --b'hello world'
print(s.format()) #format string    --hello world
print(s.islower()) #check if all characters are lowercase   --True
print(s.isupper()) #check if all characters are uppercase   --False
print(s.isspace()) #check if all characters are whitespace  --False because of letters
print(s.partition(' ')) #partition string at first occurrence of space  --('hello', ' ', 'world')
print(s.rpartition(' ')) #partition string at last occurrence of space  --('hello', ' ', 'world')
print(s.zfill(20)) #pad string with zeros on the left   --0000000000hello world
print(s.maketrans('h','H')) #create translation table   --{104: 72}
print(s.translate(s.maketrans('h','H'))) #translate string using translation table  --Hello world
print(s.removeprefix('hello')) #remove prefix 'hello'   -- world
print(s.removesuffix('world')) #remove suffix 'world'   --hello
#String interpolation
name="Deepa"
age=25
print(f"Hello {name}, you are {age} years old") #f-string   --Hello Deepa, you are 25 years old
print("Hello {}, you are {} years old".format(name,age)) #format method --Hello Deepa, you are 25 years old
print("Hello %s, you are %d years old"%(name,age)) #% formatting    --Hello Deepa, you are 25 years old
#Escape characters
print("Hello\tWorld") #tab  space --Hello   World
print("Hello\nWorld") #new line --Hello
                     #World
print("Hello\\World") #backslash    --Hello\World
print("Hello\'World") #single quote --Hello'World
print("Hello\"World") #double quote     --Hello"World
print("Hello\rWorld") #carriage return  --World     
print("Hello\bWorld") #backspace    --HellWorld
print("Hello\fWorld") #form feed    --Hello
print("Hello\vWorld") #vertical tab --Hello
print("Hello\aWorld") #alert    --HelloWorld (with a beep sound)
#Raw string
print(r"Hello\tWorld") #raw string ignores escape characters    --Hello\tWorld
#String slicing
s="Hello World"
#String membership
print('H' in s) #check if 'H' is in string ---True  
print('h' not in s) #check if 'h' is not in string  ---True case sensitive
#String comparison
s1="Hello"
s2="World"
print(s1==s2) #check if strings are equal ---False
print(s1!=s2) #check if strings are not equal   --True
print(s1>s2) #check if s1 is greater than s2    --False
print(s1<s2) #check if s1 is less than s2   --True
print(s1>=s2) #check if s1 is greater than or equal to s2  --False
print(s1<=s2) #check if s1 is less than or equal to s2 --True
#String concatenation
s3=s1+s2    #--concatenation without space 
print(s3) #HelloWorld   
s4=s1+" "+s2
print(s4) #Hello World
#String replication
s5=s1*3
print(s5) #HelloHelloHello
#String methods
print(s1.lower()) #hello
print(s1.upper()) #HELLO
print(s1.title()) #Hello
print(s1.capitalize()) #Hello
print(s1.count('l')) #2
print(s1.find('l')) #2
print(s1.replace('l','L')) #HeLLo
print(s1.split('e')) #['H', 'llo']
print(s1.strip('H')) #ello
print(s1.isalpha()) #True
print(s1.isdigit()) #False
print(s1.isalnum()) #True
print(s1.startswith('H')) #True
print(s1.endswith('o')) #True
print(s1.index('e')) #1
print(s1.rindex('l')) #3
print(s1.swapcase()) #hELLO
print(s1.center(20,'*')) #*******Hello********
print(s1.ljust(20,'*')) #Hello***************
print(s1.rjust(20,'*')) #***************Hello
print(s1.encode()) #b'Hello'
print(s1.format()) #Hello
print(s1.islower()) #False
print(s1.isupper()) #False
print(s1.isspace()) #False
print(s1.partition('e')) #('H', 'e', 'llo')
print(s1.rpartition('l')) #('Hel', 'l', 'o')
print(s1.zfill(20)) #000000000000000Hello
print(s1.maketrans('H','h')) #{72: 104}
print(s1.translate(s1.maketrans('H','h'))) #hello
print(s1.removeprefix('He')) #llo
print(s1.removesuffix('lo')) #Hello
#End of code
