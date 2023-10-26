import praw

# initialize Reddit instance
reddit = praw.Reddit(client_id='GHpiiV9U3s65QMsh3oPVxA', client_secret='LJ98CGoni4HTGF2loz4y7qWPb4Zk-Q', user_agent='linux:GHpiiV9U3s65QMsh3oPVxA:v1 (by /u/your_username)')

# specify subreddit to search in
subreddit_name = 'chromeos'
subreddit = reddit.subreddit(subreddit_name)

# specify phrases to search for
search_phrases = ['I wish my OS could', 'Why can\'t my device just', 'It would be cool if', 'They should add']

# create a new text file to store results
txt_filename = 'search_results.txt'
with open(txt_filename, 'w') as txt_file:

    # search for posts containing specified phrases
    for phrase in search_phrases:
        search_results = subreddit.search(phrase, limit=None)
        for result in search_results:
            txt_file.write(f"{result.title}\n")
            txt_file.write(f"Link: https://www.reddit.com{result.permalink}\n\n")

subreddit_name1 = 'osdev'
subreddit1 = reddit.subreddit(subreddit_name1)

ignore_phrases = ['I got', 'I made',]

with open(txt_filename, 'a') as txt_file:
    # search for posts in second subreddit
    search_results = subreddit1.search('', limit=None)
    for result in search_results:
        title = result.title.lower()
        if any(phrase in title for phrase in ignore_phrases):
            continue
        txt_file.write(f"{result.title}\n")
        txt_file.write(f"Link: https://www.reddit.com{result.permalink}\n\n")
