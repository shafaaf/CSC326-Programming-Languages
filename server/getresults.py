import redis


def getResults(searchWord):
    
    r_conn = redis.Redis()

    word_id = r_conn.get(searchWord)

    doc_id_list = r_conn.smembers("inverted_"+word_id)

    for doc_id in doc_id_list:
        r_conn.zadd("results_"+searchWord, doc_id, r_conn.zscore("pageranks",
        doc_id))

    url_list_ids = r_conn.zrevrangebyscore("results_"+searchWord, "+inf", "-inf")
    url_list = [r_conn.hget("doc_id_"+x, "url") for x in url_list_ids]

    return url_list


def getResults_multiword(searchWord_list):
    
    r_conn = redis.Redis()
    results = {}

    for word in searchWord_list:
        word_id = r_conn.get(word)
        if word_id is not None:
            doc_id_list = r_conn.smembers("inverted_"+word_id)

            for doc_id in doc_id_list:
                if doc_id not in results:
                    results[doc_id] = r_conn.zscore("pageranks", doc_id)
                else:
                    results[doc_id] += r_conn.zscore("pageranks", doc_id)
    results_list = [(a,b) for a,b in results.items()]
    results_list_sorted = sorted(results_list, key=lambda a: a[1], reverse=True)

    url_list = [r_conn.hget("doc_id_"+x[0], "url") for x in results_list_sorted]

    return url_list

if __name__ == "__main__":
    wordToSearch = "toronto"
    getResults(wordToSearch)
    print getResults_multiword(["toronto", "research"])
    
