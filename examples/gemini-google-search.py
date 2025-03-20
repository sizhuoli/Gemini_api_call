#!/usr/bin/env python
# coding: utf-8

# # Google Gemini with Google Search
# 
# Gemini 2.0 Flash comes with native Google Search integration, allowing the model to access up-to-date information from the web. This is particularly useful for queries that require current information or external knowledge. By enabling Google Search, Gemini can provide more accurate and timely responses.
# 
# Key features:
# - Simple to enable with one configuration change
# - Automatically searches when needed for up-to-date information
# - Supports 30+ languages
# - Free tier: 1,500 queries per day
# - Paid tier: $35 per 1,000 queries
# 
# You can learn more about Google Search integration with Gemini here:
# [https://ai.google.dev/gemini-api/docs/grounding?lang=python](https://ai.google.dev/gemini-api/docs/grounding?lang=python)


# In[19]:


import os
from google import genai
from dotenv import load_dotenv

load_dotenv('../.env')
# create client
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY","xxx"))


# # Generate a list of cookie recipes
# response = client.models.generate_content(
#     model='gemini-2.0-flash',
#     contents='Who won the Euro 2024?',
#     config={"tools": [{"google_search": {}}]},
# )
#
# # print the response
# print(f"Response: {response.text}")
# # print the search details
# print(f"Search Query: {response.candidates[0].grounding_metadata.web_search_queries}")
# # urls used for grounding
# print(f"Search Pages: {', '.join([site.web.title for site in response.candidates[0].grounding_metadata.grounding_chunks])}")
#

# more complex example with multiple queries

# In[20]:


# Generate a list of cookie recipes
response = client.models.generate_content(
    model='gemini-2.0-flash',
    contents='xai company',
    config={"tools": [{"google_search": {}}]},
)

# print the response
print(f"Response: {response.text}")
# print the search details
print(f"Search Query: {response.candidates[0].grounding_metadata.web_search_queries}")
# urls used for grounding
print(f"Search Pages: {', '.join([site.web.title for site in response.candidates[0].grounding_metadata.grounding_chunks])}")


# In[ ]:




