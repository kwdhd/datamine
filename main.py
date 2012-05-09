# -*- coding:UTF-8 -*-

import twitter
import json
import nltk

def main():
    twitter_search = twitter.Twitter(domain="search.twitter.com")
    search_result = []
    
    for page in range(1,6):
        search_result.append(twitter_search.search(q="SNL",rpp=100,page=page))
        
    #===========================================================================
    # for res in search_result:
    #    print res
    #===========================================================================
    
    #print json.dumps(search_result, sort_keys=True, indent=1)
    
    tweets = [ r for result in search_result  for r in result]
    
    words = []
    for t in tweets:
        words += [w for w in t.split()]
    print len(words)
    print len(set(words))
    print 1.0*len(set(words))/len(words)
    print 1.0*sum([len(t.split()) for t in tweets])/len(tweets)
    pass
if __name__ == "__main__":
    main()
    print "main"