import re

quote = "There's only one thing I hate more than lying: skim milk. Which is water that's lying about being milk. - Ron Swanson"

match = re.search("milk", quote)
if match:
    print(match.group())

found = re.findall("milk", quote)
print(found)

count = len(re.findall("milk", quote))
print(count)

split = re.split(r"\.", quote)
print(split)

sub = re.sub("milk", "dairy", quote, count=1)
print(sub)