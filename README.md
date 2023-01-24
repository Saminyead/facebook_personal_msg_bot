# facebook_personal_msg_bot

You want to send the same message to many friends on Facebook. So you logged in, went to 'new message', typed a bunch of names, and hit send. 
The messages are sent, but now you have a message group that no one wanted, and where no one would really write much of anything. Great! Another dead group that 
was created for just a single text! 

Alternatively, you can individually click on each people's message box, and Ctrl+C Ctrl+V the same message over and over. This is fine if you have to send to, say
around 10 people. But what if it is multiples of 10, many multiples in fact. This is where this bot comes in.

Before you can use the bot as intended, there are some preparatory steps:

1. Install all packages in the "requirements.txt" file. Run the following commands in order in command prompt -- cd /d path-where-repo-is and 
pip install -r requirements.txt.

2. In the repo folder, create a file named ".env", then open it up with a text editor like notepad. In the .env file write your facebook login email and password in two
separate lines like so: 
email=youremail@example.com
password=yourpassword
(replace youremail@example.com and yourpassword with your Facebook login email and password respectively)

Now that the preparatory steps are done, let's set up the bot:
1. in the msg_content.txt file, write a message 
2. in the list_of_names.txt file, write a list of names of friend you want to send the message to -- each name in a new line
3. run the script send_fb_msg.py;

and now all your friends have received the same message, and there are no awkward groups!

At this point, you may have a lot of questions:

1. Is this a spam bot?

DO NOT USE IT FOR SPAM! Not only will your account be banned, but it's your Facebook friends who will be annoyed with you. This bot is simply made to send
the same message to multiple friends without having to mindlessly copy paste in each friend's message box.

2. Will my account get flagged as spam?

There are quite a few 'timeouts' within the program, so that it does not perform mutliple actions too fast. For example, there is a 15 seconds wait after the 
command for fetching the page at 'www.facebook.com', 1 second of timeout after each button click, and so on. Thus, the actions should look more 'human-like'. However,
running the program for a long time - especially day after day, or running it with no timeouts will increase the chances of being flagged as spam.

3. Doesn't Meta have an API for this?

Yes, they do in fact. It's called the Send API, documentations for which can be found <a href="https://developers.facebook.com/docs/messenger-platform/reference/send-api/">here</a>.
But it only works if you want to send a message through a Facebook Page you own. As a result, this API is mostly useful for business purposes e.g. sending the same messages to your customers. But there is no API which allows you to send messages from your personal account to your friends. Hence, the bot.

So yes, the bot is not extremely useful for business purposes -- use the Send API for that. But if like me, you want to send the same message to lots of friends without 
having to open a group that will be mostly dead -- you can use this.
