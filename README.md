# BollyDialogueSearch
Text based search of bollywood dialogues

Note: Data is scraped from a website. Script for scraping is in script folder.

Requirements:
  1. Elastic Search - For text search and data storage
  2. Flask - python restful frameword
  3. angular - frontend server
  
Steps to Run:
  1. Once you have the data. Load the data in elastic search
  2. Start the backend server. Command: python runbackend.py
  3. Start the frontend server. Go to frontend_service folder and run "python -m SimpleHTTPServer 8000"
  
  Access the UI at http://localhost:8000
   
  
