import re
Mystr='''Since March 8, 1990, Woman’s Day is being observed by SAARC (South Asian Association for Regional Cooperation) 
consisting of seven countries, namely, India, Pakistan, Nepal, Bhutan, Bangladesh, Sri Lanka, and the Maldives. 
The day was marked to focus on the problems of girl children in these countries. 
It is a pity that girl children especially in +919339043398
underdeveloped countries are victims of extreme negligence and dishonour. The birth of a girl child is looked upon 
by the parents as a cause of pity. They are deprived of proper nutrition, education, economic facilities, and social status or honour.'''
#pattern = re.compile(r"girl")#re.compile function is used to compile a regular expression pattern into a regex pattern object which can be later used to find the pattern object in a target string 
pattern = re.compile(r'.cia')
#pattern = re.compile(r'^Si')
#pattern = re.compile(r'our.$')
#pattern = re.compile(r'all*')#to find the number of occurances of 'l' after 'al'
#pattern = re.compile(r'al{2}')#to find the cases of exact occurance of 'l' twice after 'a'
#pattern = re.compile(r'al+')
#pattern = re.compile(r'(al){2}')#to form and capture the groups
#pattern = re.compile(r'al{1}|India')#it will capture either al or India
#Special sequences
#pattern = re.compile(r'\ASince')
#pattern = re.compile(r'\bPak')
#pattern = re.compile(r'tan\b')
#pattern = re.compile(r'\Bir')
#pattern = re.compile(r'\d')
#pattern = re.compile(r'\d{4}') #to search special pattern
#task(find a 10 digit phone no. wwith +91 code)
#pattern = re.compile(r'[+91]\d{10}')
matches = pattern.finditer(Mystr)
for mat in matches:
    print(mat)
#print(Mystr[272:276])#example
#other functions in RE
#findall,search,split,sub