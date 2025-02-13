Project Overview
This project automates the scraping and classification of NeurIPS research papers. It extracts paper details (title, abstract, links) from the NeurIPS website and classifies them into predefined categories like Deep Learning, NLP, and Reinforcement Learning using Google Gemini AI.

How to Run
1. Set Up the Environment
Install required dependencies:
bash
Copy
Edit
pip install requests beautifulsoup4 pandas google-generativeai python-dotenv
Obtain a Google Gemini API key and store it in a .env file:
ini
Copy
Edit
GEMINI_API_KEY=your_api_key_here
2. Run the Scraper in Jupyter Notebook
Open scraper.ipynb in Jupyter Notebook.
Run all cells to scrape NeurIPS papers and save data in neurips_papers.csv.
3. Run the Annotation Script
Run automation.py in the terminal:
bash
Copy
Edit
python automation.py
This script will classify the papers using Google Gemini AI and update neurips_papers.csv with categorized labels.
Project Files
scraper.ipynb → Scrapes research papers and saves data in CSV.
automation.py → Uses AI to classify papers and updates the CSV.
.env → Stores the Google Gemini API key.
neurips_papers.csv → The dataset containing paper details and AI-generated categories.
This project enables efficient research paper categorization, saving time and effort in literature reviews
