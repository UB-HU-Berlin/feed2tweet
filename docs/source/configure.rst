Configure Feed2tweet
====================

As a prerequisite to use Feed2tweet, you need a Twitter app. Log in Twitter, go to https://apps.twitter.com, create an app and generate the access token.

In order to configure Feed2tweet, you need to create a feed2tweet.ini file (or any name you prefer, finishing with the extension .ini) with the following parameters::

    [twitter]
    consumer_key=ml9jaiBnf3pmU9uIrKNIxAr3v
    consumer_secret=8Cmljklzerkhfer4hlj3ljl2hfvc123rezrfsdctpokaelzerp
    access_token=213416590-jgJnrJG5gz132nzerl5zerwi0ahmnwkfJFN9nr3j
    access_token_secret=3janlPMqDKlunJ4Hnr90k2bnfk3jfnwkFjeriFZERj32Z

    [cache]
    cachefile=/home/user/feed2tweet/cache.db
    cache_limit=10000

    [rss]
    uri: https://www.journalduhacker.net/rss
    uri_list: /home/user/feed2tweet/rsslist.txt
    tweet: {title} {link}
    title_pattern: Open Source
    title_pattern_case_sensitive: true
    no_uri_pattern_no_global_pattern=true

    [hashtaglist]
    several_words_hashtags_list: /home/user/feed2tweet/hashtags.txt

For the [twitter] section:

- consumer_key: the Twitter consumer key (see your apps.twitter.com webpage)
- consumer_secret: the Twitter consumer secret key (see your apps.twitter.com webpage)
- access_token: the Twitter access token key (see your apps.twitter.com webpage)
- access_token_secret: the Twitter access token secret key (see your apps.twitter.com webpage)

For the [cache] section:

- cachefile: the path to the cache file storing ids of already tweeted links. Absolute path is mandatory. This file should always use the .db extension.
- cache_limit: length of the cache queue. defaults to 100.

For the [rss] section:

- uri: the url of the rss feed to parse
- uri_list: a path to a file with several adresses of rss feeds, one by line. Absolute path is mandatory.
- tweet: format of the tweet you want to post. It should use existing entries of the RSS fields like {title} or {link}. Launch it with this field empty to display all available entries.
- {one field of the rss feed}_pattern: takes a string representing a pattern to match for a specified field of each rss entry of the rss feed, like title_pattern or summary_pattern.
- {one field of the rss feed}_pattern_case_sensitive: either the pattern matching for the specified field should be case sensitive or not. Default to true if not specified.
- no_uri_pattern_no_global_pattern: don't apply global pattern (see above) when no pattern-by-uri is defined in the uri_list. Allows to get all entries of a rss in the uri_list because no pattern is defined so we match them all. Defaults to false, meaning the global patterns will be tried on every rss in the uri_list NOT HAVING specific patterns and so ONLY entries from the specific uri in the uri_list matching the global patterns will be considered.

For the [hashtaglist] section:

- several_words_hashtags_list: a path to the file containing hashtags in two or more words. Absolute path is mandatory. By default Feed2tweet adds a # before every words of a hashtag.

List of rss feeds
=================
Simple list of rss feeds
------------------------
With the parameter **uri_list**, you can define a list of uri to use. Starting from 0.10, Feed2tweet is now able to match specific patterns for each of the rss feeds from this list. Consider the following rss section of the configuration file::

    [rss]
    uri_list=/home/john/feed2tweet/rsslist.txt
    tweet={title} {link}

Now let's have a look at the =/home/john/feed2tweet/rsslist.txt file::

    https://www.journalduhacker.net/rss
    https://carlchenet.com/feed

Each line of this file is a url to a rss feed. Pretty simple.

Match specific patterns of rss feeds in the uri_list files
----------------------------------------------------------
Starting with Feed2tweet 0.10, you can now use specific pattern matching for uri in the uri_list file to filter some of the rss entries of a rss feed. Lets modify the previous file::

https://www.journalduhacker.net/rss|title|hacker,psql
https://carlchenet.com/feed|title|gitlab

Each line of this file starts with an uri, followed by a pipe (|), followed by the name of the available section to parse (see below), again followed by a pipe (|), followed by patterns, each pattern being separated from the other one by a semi-colon (,).

In the example file above wee get every rss entries from the feed available at https://www.journalduhacker.net/rss where a substring in the title section of this entry matches either "hacker" or "psql". Specific patterns are not case sensitive. For the second line, we match every rss entries from the feed available at https://carlchenet.com/feed where a substring in the title section of this entry matches "gitlab".

Consider every entries of a rss feed from a uri in the uri_list file
--------------------------------------------------------------------
Starting from Feed2tweet 0.10, it is now possible to get all entries from a rss feed available in the uri_list file. You need an option to deactivate the global pattern matching for uri in the uri_list NOT having specific patterns::

    [rss]
    ...
    no_uri_pattern_no_global_pattern=true

In you rsslist.txt, just don't give anything else than the needed feed url to get all the entries::

https://www.journalduhacker.net/rss|title|hacker,psql
https://carlchenet.com/feed|title|gitlab
https://blog.linuxjobs.fr/feed.php?rss

The last line of the file above only has the url of a rss feed. All entries from this feed will be tweeted.

How to display available sections of the rss feed
=================================================
Starting from 0.8, Feed2tweet offers the **--rss-sections** command line option to display the available section of the rss feed and exits::

    $ feed2tweet --rss-sections -c feed2tweet.ini
    The following sections are available in this RSS feed: ['title', 'comments', 'authors', 'link', 'author', 'summary', 'links', 'tags', id', 'author_detail', 'published'].
