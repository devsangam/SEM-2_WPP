# tokenize punctuations, dates, urls, emails, numbers (in all different forms such as “33.15”,
# “3,22,243”, “313/77”), social media usernames/user handles. Use regular expressions to design
# this. [Hint: Use unicode blocks for your language, check wikipedia pages]
# """EN_PATTERNS = {
#     "url": r"https?://\S+|www\.\S+",  # Matches URLs
#     "email": r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",  # Matches Emails
#     "date": r"\b(?:\d{1,2}[-/]\d{1,2}[-/]\d{2,4}|\d{4}[-/]\d{1,2}[-/]\d{1,2}|\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]* \d{1,2}, \d{4})\b",
#     "number": r"\b\d{1,3}(?:,\d{3})*\.\d+|\b\d+(?:/\d+)?|\b\d{1,3}(?:,\d{3})*\b",  # Matches decimals, fractions, and comma-separated numbers
#     "username": r"@\w+",  # Matches @usernames
#     "punctuation": r"[.,!?;:()\"']",  # Matches common punctuation
#     "word": r"\b\w+\b",  # Matches words
# }"""
# months=r"\d{1,2},?\s(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*,?\s\d{2,4}"
import re
expressions={
'date':r"\b(\d{1,2}[-\/\.]\d{1,2}[-\/\.]\d{2,4})|(\d{2,4}[-\/\.]\d{1,2}[-\/\.]\d{1,2})|(\d{2,4}[-\/\.]\d{1,2}[-\/\.]\d{1,2})|(\d{1,2},?\s(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*,?\s\d{2,4})/",
'numbers':r"(\d+([,\/\.]\d+)?)",
'url':r"(?:(?:https?:\/\/)|(?:www\.))\w+.\w+/gm",
'email':r"[\w._%+-]+@[\w.-]+.[a-zA-Z]+",
'username':r"@[\w+_\-\.?:]+",                                                                                                                                                                           
'puntuations':r"[.,!?;:()\"']+",
'word':r"\b[a-zA-Z]+\b",
}
final_expression=""
k=expressions.keys()
# for key in k:
#     final_expression = final_expression +"("+expressions[key]+")|"
# final_expression=final_expression[0:-1]
# tokenizer=re.compile(final_expression, re.IGNORECASE)
string=input("enter text:\t")
for key in k:
    list=re.finditer(expressions[key],string, re.IGNORECASE)
    print(key+":\n")
    for l in list:
        if(l):
            print(end="\t")
            print(l.group())

# for t in tokenizer.finditer(string):
    # grp=t.lastgroup
    # print(grp)
    # token=t.group()
    # print(token)
    # print(k[grp-1]+" = "+token)


