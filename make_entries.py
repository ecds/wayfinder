import re
from bs4 import BeautifulSoup as bs

data = open('bib_raw.txt')

lines = data.readlines()

line_dict = {}
for index, line in enumerate(lines):
    id_pattern = '^[\d]+\s'
    match = re.match(id_pattern, line)
    if match:
        status = "match"
        num = int(match.group(0).strip())
    else:
        status = "no match"
        num = "NA"
    line_dict[index] = {"status":status,
                        "num": num,
                        "line": line}
counter = 0
for i in sorted(line_dict.keys()):
    if line_dict[i]["status"] == "match":
        counter += 1
        if line_dict[i]["num"] == counter:
            line_dict[i]["line"] = '</div><div num="'+str(line_dict[i]['num'])+'">'+line_dict[i]["line"]
        else:
            counter -= 1

with open('bib_entries.xml', 'w') as outfile:
    outfile.write("<xml>")
    for i in sorted(line_dict.keys()):
        outfile.write(line_dict[i]["line"])
    outfile.write("</xml>")
    outfile.close()

data = open('bib_entries.xml')
soup = bs(data, 'lxml')
divs = soup.findAll('div')

# Print out the number of entries generated. Should be 6562.
print(len(divs))
