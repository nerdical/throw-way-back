'''
There are possible issues with authentication
So I cannot gurarantee that end users who
download this app will be able to use it.
However; please download it, try it out
and see what you can do with it.
'''

import fbconsole as F
import praw

P = praw.Reddit(user_agent = ("Post top image from the past week in /r/historyporn to Facebook for throw[way]back Thursday."
							  "Put together by /u/koberg"))

user_id = "throw-way-back"
user_pass = "Tr0wW@y8AcK"
P.login(user_id, user_pass)

sub = P.get_subreddit("historyporn")

imagePost = sub.get_top_from_week(limit = 1)

for post in imagePost:
	message = "Throw[way]back Thursday!\n\n" + post.title + "\n\n" + post.url + "\n\nSubmitted by /u/" + str(post.author) + "\n\nThis post was made with the Throw[way]back python script.\nMore information can be found at https://github.com/nerdical/throw-way-back"
	post.upvote()
	F.APP_ID = "746516458795325"
	F.AUTH_SCOPE = ['publish_stream']
	F.authenticate()
	F.post('/me/feed', {'message' : message})
