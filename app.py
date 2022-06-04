#!/usr/bin/env python
# coding: utf-8

# In[1]:


from textblob import TextBlob


# In[2]:


# python uses either flask or django, flask is slightly easier to use
# frontend side, either react (by facebook) or angular (by google)
from flask import Flask


# In[3]:


from flask import render_template, request


# In[4]:


# words __x__ are words that cannot be used as variables
app = Flask(__name__)


# In[5]:


# App Routing means mapping the URLs to a specific function that will handle the logic for that URL.
@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == "POST": #after enter button is pressed, POST condition will be met
        text = request.form.get("text")
        print(text)
        r = TextBlob(text).sentiment
        return(render_template("index.html", result=r))
    else: #before enter button is pressed
        return(render_template("index.html", result="is waiting..."))


# In[ ]:


# to protect the cloud from running illegal software
if __name__=="__main__":
    app.run()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




