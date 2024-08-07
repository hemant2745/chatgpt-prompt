import spacy
import json
nlp = spacy.load("en_core_web_sm")
json_schema = {
    "name": "",
    "email": "",
    "phone": "",
    "skills": [],
    "experience": [
        {
            "company": "",
            "title": "",
            "dates": "",
            "description": ""
        }
    ],
    "education": [
        {
            "degree": "",
            "university": "",
            "year": ""
        }
    ]
}
with open("resume_parsed.json", "w") as f:
    json.dump(json_schema, f, indent=4)
