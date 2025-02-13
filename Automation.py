import os
import pandas as pd
import google.generativeai as genai  
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# Annotation Labels
LABELS = ["Deep Learning", "NLP", "Computer Vision", "Reinforcement Learning", "Optimization"]

# Load CSV File
csv_path = "./neurips_papers.csv"
df = pd.read_csv(csv_path)

def classify_paper(title, abstract):
    """Send paper title & abstract to Gemini API and classify into predefined categories."""
    prompt = f"""
    Classify the following research paper into one of these categories: {', '.join(LABELS)}.
    
    Title: {title}
    Abstract: {abstract}
    
    Provide only the category name from the given options.
    """
    try:
        model = genai.GenerativeModel("gemini-pro")  
        response = model.generate_content(prompt)
        classification = response.text.strip()
        return classification if classification in LABELS else "Unknown"
    except Exception as e:
        print(f"Error classifying paper: {e}")
        return "Error"

# Annotate Papers and Update CSV
df["annotation"] = df.apply(lambda row: classify_paper(row["Title"], row["Abstract"]), axis=1)

df.to_csv(csv_path, index=False)
print("Updated CSV with annotations successfully!")
