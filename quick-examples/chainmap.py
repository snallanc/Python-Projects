"""
ChainMap:
Used for combining mappings from multiple dictionaries in a more efficient way than regular dictionary updates.
Combines mappings from last to first ie., mappings appear from last dict arg to first dict arg.

EXAMPLE:
"""
import collections

numberToAsciiMappings = {0:48, 1:49, 2:50, 3:51, 4:52, 5:53, 6:64, 7:55, 8:56, 9:57}
letterToAsciiMappings = {"A":65, "B":66, "C":67, "D":68, "E":69, "F":70}
punctuationToExtAsciiMappings = {"'":145, '"':147, ".":149, "-":150, "_":151, "~":152}

# mappings of punctuationToAsciiMappings appear first followed by letterToAsciiMappings and numberToAsciiMappings
cm = collections.ChainMap(numberToAsciiMappings, letterToAsciiMappings, punctuationToExtAsciiMappings)
print(list(cm))
print(0 in cm)
print("a" in cm, "\n")

# Update the mappings of punctuations from Extended ASCII table to ASCII table and add a few new ones
cm['"']=34
cm["&"]=38
cm["'"]=39
cm[","]=44
cm["."]=46
cm["-"]=45
for k in ['"', ",", "&", ".", "$"]:
    print(cm.get(k))
