import re

"""
highlight_doc
INPUT: doc-The blurb of text that query is suppose to find text within
     : query-The subset of text that you want to look for
OUTPUT: result-The useful snippet of text that will be printed out. Assume that the webpage will do a simple bolding of the query
               Assume a snippet size is 140 chars. (Helps for texts =P)

In terms of implementation, offer a relevancy score for the result.
Relevency Score is compiled through
1) How many words of the query is matched in the doc
2) How many suitable metadata words are taken
3) How many pronouns are used

Find the string with the best "goodness", and output the snippet
"""
def highlight_doc(doc, query):
    #sanity check on the query

    #split the doc and query
    docarray = re.split(' ', doc)
    queryarray = re.split(' ', query)
    counter = 0
    #according to stats, an average word size is about 5 characters, and so if we want 140, 18 words is the range we want. Choose 17 to be on the safe side
    (maxcounter, minv, maxv) = (0, 0, 17)
    vlist = []

    if (len(docarray) < 17):
        snippet = doc
    else:
        for i in xrange(1,17):
            for queryword in query:
                if (docarray[i] == queryword and i != 17):
                    counter += 1
                    maxcounter = counter
        #iterate through all the words of the document. Find the range of a snippet of text from document that has the most amount of words from the query
        for i,j in zip(range(0,len(docarray)-17), range(17,len(docarray))):
            currentcounter = counter
            for queryword in query:
                if (docarray[j] == queryword):
                    counter += 1

            if counter > maxcounter:
                maxcounter = counter
                pos = "{0},{1}".format(i, j)
                vlist = [pos]
            elif currentcounter == maxcounter and currentcounter == counter:
                vlist.append("{0},{1}".format(i, j))

            for queryword in query:
                if (docarray[i] == queryword):
                    counter -= 1

        #substring
        snippetlist = []
        for val in vlist:
            valspl = val.split(',')
            snippetlist.append(" ".join(docarray[int(valspl[0]):int(valspl[1])]))

        #value of a dictionary of useful metadata keywords
        snippet = snippetlist[0]
    return snippet

#TEST CASESSSSSSS




