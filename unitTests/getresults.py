import sqlite3 as lite

searchedWords = {}

def getResults(db_file, searchWord):
    
    # If word previously searched, return the word
    if searchWord in searchedWords:
        return searchedWords[searchWord]
    
    con = lite.connect("dbFile.db")
    curs = con.cursor()

    
    queryString = "CREATE TABLE word_id AS SELECT distinct lexicon.wordid FROM lexicon WHERE lexicon.word = '%s';" % searchWord
    curs.execute(queryString) 

    curs.execute("CREATE TABLE docid_list AS SELECT distinct invertedIndex.docid from word_id inner join invertedIndex ON word_id.wordid = invertedIndex.wordid;")

    curs.execute("SELECT * FROM docid_list;")
    for row in curs:
        print row

    print "\n\npage ranks"
    curs.execute("SELECT * FROM pageRanks;")
    for row in curs:
        print row

    curs.execute("CREATE TABLE result_id_list AS SELECT distinct docid_list.docid, pageRanks.pagerank FROM docid_list inner join pageRanks ON docid_list.docid = pageRanks.docid order by pageRanks.pagerank desc;")


    urlListObject = curs.execute("SELECT distinct documentIndex.url FROM result_id_list inner join documentIndex on result_id_list.docid = documentIndex.docid;")
    urlList = []
    for row in urlListObject:
        urlList.append(row[0])

    # Remove temporary tables
    curs.execute("DROP TABLE IF EXISTS word_id;")
    curs.execute("DROP TABLE IF EXISTS docid_list;")
    curs.execute("DROP TABLE IF EXISTS result_id_list;")

    # Add to dictionary of searched words
    searchedWords[searchWord] = urlList

    return urlList



if __name__ == "__main__":
    wordToSearch = "department"
    print getResults("dbFile.db", wordToSearch)

    
