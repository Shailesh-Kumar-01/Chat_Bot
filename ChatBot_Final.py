#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import files
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import time
time.clock = time.time


# In[2]:


app = Flask(__name__)
#chatbot = ChatBot('ChatBot')
chatbot = ChatBot("ChatterBot", storage_adapter="chatterbot.storage.SQLStorageAdapter")


# In[3]:


trainer = ChatterBotCorpusTrainer(chatbot)
#trainer.train("chatterbot.corpus.english")
trainer.train('./my_corpus.json')


# In[4]:


# Now we can export the data to a file
#trainer.export_for_training('./my_export.json')


# In[5]:


@app.route("/")
def home():
    return render_template("index.html")


# In[6]:


@app.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))


# In[ ]:


if __name__ == "__main__":
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




