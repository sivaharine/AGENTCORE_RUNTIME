🤖 E-commerce Customer Support Agent

A simple AI-powered customer support backend built with FastAPI, MongoDB, and Gemini AI.
The system receives user queries, checks product information from the database, and generates helpful support responses using an LLM.

🚀 Features

AI-powered customer support responses

Product search from MongoDB inventory

Greeting and farewell detection

LLM-based response generation using Gemini

REST API endpoint for chat interaction

⚙️ Tech Stack

FastAPI

MongoDB

Google Gemini API

Python

📂 Project Files

main.py – FastAPI server and chat API endpoint

agent_core.py – Core logic for handling user queries and responses

database.py – MongoDB connection and product collection access

tool.py – Product lookup utility from the database

llm_client.py – Gemini API integration for generating responses

▶️ Run the Project
pip install -r requirements.txt
uvicorn main:app --reload

API endpoint:

POST /chat

Send a request with:

{
  "message": "Do you have iPhone 14?"
}

The system will check the product inventory and generate a helpful support response.
