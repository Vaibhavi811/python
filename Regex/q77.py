# wap that uses named groups in regular expressions to extract a username and domain from an email address
import re
email= "vaibhavi123@gmail.com"

pattern= r"(?P<username>[a-zA-Z0-9]+)@(?P<domain>[a-zA-Z0-9]+\.[a-z]+)"
match= re.search(pattern,email)

if match:
    print(match.group("username"))
    print(match.group("domain"))
