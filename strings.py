# Task 1 — String methods
# Given text = "  hello, qa world!  ". Remove the whitespace on both sides, capitalize the first letter,
# and print the result.

text = "  hello, qa world!  "
nex_text = text.strip().capitalize()
print(nex_text)


# Task 2 — Upper, lower, replace
# Given email = "Denis.Berg@Company.COM". Print it in all lowercase. Then replace @company.com with @gmail.com.

email = "Denis.Berg@Company.COM"
new_email = email.lower().replace("@company.com", "@gmail.com")
print(new_email)


#Task 3 — Split and join
# Given tags = "smoke,regression,api,ui". Split it into a list and print each tag on a new line. Then join them back
# with | separator and print.

tags = "smoke,regression,api,ui"
new_tags = tags.split(",")

for tag in new_tags:
    print(tag)

print(" | ".join(new_tags))


# Task 4 — String contains and startswith
# Given url = "https://customs.finland.gov/api/v1/users". Check and print:
#
# does it start with https
# does it contain api
# does it end with users

url = "https://customs.finland.gov/api/v1/users"

print(f"Starts with https: {url.startswith('https')}")
print(f"Contains api: {'api' in url}")
print(f"Ends with users: {url.endswith('users')}")


# Task 5 — Slicing
# Given error_code = "ERR-404-NOT_FOUND". Extract and print using slicing:
#
# just the error number 404
# everything after the second dash NOT_FOUND

error_code = "ERR-404-NOT_FOUND"
print(error_code[4:7])
print(error_code[-9:])
