# -*- coding:UTF-8 -*-

import twitter

def main():
    twitter_search = twitter.Twitter(domain="search.twitter.com")
    search_result = []
    
    for page in range(1,6):
        search_result.append(twitter_search.search(q="SNL",rpp=100,page=page))
        
    print search_result
    pass
if __name__ == "__main__":
    main()
    print "main"