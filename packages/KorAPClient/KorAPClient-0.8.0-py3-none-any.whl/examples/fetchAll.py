from KorAPClient import KorAPConnection

kcon = KorAPConnection(verbose=True)

q = kcon.corpusQuery("Ameisenplage", metadataOnly = False).fetchNext()

df = q.slots['collectedMatches']
print(df)

q = kcon.corpusQuery("Ameisenplage", metadataOnly = False).fetchNext()

df = q.slots['collectedMatches']
print(df)
