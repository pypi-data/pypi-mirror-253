teststring = "Analytics PMNdataLayer verification for detail page #1;Analytics PMNdataLayer verification for detail page #1 C147334: The data layer keys are added in PMNdataLayer for the articles page 1 (example #1)"
suitename = teststring.split(';')[0]
teststring = teststring.replace(suitename, "")
teststring = teststring.replace(';','',1)
teststring = teststring.strip()
print(teststring)
if "(example #" in teststring:
    teststring = teststring.split("(example #")[0]
    teststring = teststring.strip()
print(teststring)