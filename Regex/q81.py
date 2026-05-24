# wap demonstrating re.compile() function
import re
text= "Java is a programming language. java is a high level programming language. Java is better then python."

pattern= r"[Jj]ava"
comp= re.compile(pattern)

match= comp.findall(text)

for i in match:
    print(i)