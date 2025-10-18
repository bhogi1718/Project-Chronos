🕰️ Project Chronos: AI Archaeologist  

👩‍💻 Team Members  

| Name | Roll Number |  
|------|--------------|  
| Charan | SE23UCSE240 |  
| Adrija | SE23UARI004 |  
| Amrutha | SE23UCSE110 |  
| Ishrath | SE23UECM023 |  

---

🧠 Project Overview  
Project Chronos is an AI-powered system that reconstructs incomplete or broken text, similar to how archaeologists restore ancient manuscripts.  
It uses Google Gemini Generative AI to intelligently fill in missing parts, producing coherent and contextually accurate text.  
This project combines Natural Language Processing (NLP) with Digital Archaeology, showing how AI can help preserve and revive lost or fragmented writings.  

---

⚙️ Getting Started  

Follow these steps to set up the project on your computer:  

1️⃣ Clone the Repository  
```bash
git clone https://github.com/bhogi1718/project-chronos.git
cd project-chronos
```  

2️⃣ Create a Virtual Environment (Optional but Recommended)  
```bash
python -m venv venv
```  
Activate it:  

- Windows:  
```bash
venv\Scripts\activate
```  
- macOS/Linux:  
```bash
source venv/bin/activate
```  

3️⃣ Install Required Packages  
Make sure you have Python 3.8+ installed, then run:  
```bash
pip install -r requirements.txt
```  

Dependencies include: 
- google-generativeai==0.8.5  
- python-dotenv==1.1.1  
- nltk, textblob, and others  

---

4️⃣ Set Up Your API Key  
To enable AI reconstruction, you need a Google Gemini API key:  

1. Create a .env file in the project root  
2. Add the following line:  
```env
GEMINI_API_KEY="AIzaSyAygmmEvcpndjDAB5UyTlpw89Itd1ZFNag"
GOOGLE_API_KEY="AIzaSyBZcIhDvcJikGW54L8oXuU85ODI_d8zQXw"
SEARCH_ENGINE_ID="547575e2eee85460f"
```  
3. Save the file.  
(Make sure .env is included in .gitignore so it’s not uploaded to GitHub.)  

---

🚀 How to Use  

Command Line  
You can reconstruct text directly via CLI:  
```bash
python main.py "your fragmented text here"
```  

Example:  
```bash
python main.py "gg ez noob team lmao"
```  

Output:  
```
============================================================
          📜 AI ARCHAEOLOGIST RECONSTRUCTION REPORT 📜
============================================================

--- [Original Fragment] ---
> gg ez noob team lmao

--- [AI-Reconstructed Text & Analysis] ---
## AI Archeologist Report: Early 2000s Gaming Forum Fragment

**Fragment Source:** Archived post from an unmoderated, competitive online gaming forum (circa 2003-2007).

**Original Fragment:** 'gg ez noob team lmao'

---

### 1. Reconstruction and Coherent Sentence

**Reconstructed Sentence:** "Good game; that was easy. The opposing team was unskilled, which is quite funny."

*(Alternatively, depending on direct transcription preference and context of who is speaking: "Good game, easy, noob team. Laughing my ass off.")*

**Most Common Intent-Based Interpretation (as a post-match taunt):** "Good game, it was easily won. Your team was filled with unskilled players, which is hilarious."

---

### 2. Slang Analysis and Explanation

The fragmented text contains four distinct pieces of early 21st-century internet/gaming slang:

| Term | Full Meaning/Origin | Contextual Use |
| :--- | :--- | :--- |
| **gg** | **Good Game** (Acronym) | A standard, polite acknowledgment of the end of a competitive match. **However,** when immediately followed by "ez," the politeness is often revoked, and "gg" becomes a prelude to mockery. |
| **ez** | **Easy** (Abbreviation) | Used to dismiss the effort required to win the match. It is a boastful claim that the opponents posed no challenge. |
| **noob** | **Newbie** (Slang/Derogatory Term) | Derives from "new" or "newcomer." In the early 2000s, it evolved into a highly derogatory term in gaming, meaning "an unskilled, inept, or foolish player." It implies the player lacks basic knowledge or competence. |
| **lmao** | **Laughing My Ass Off** (Acronym) | Standard internet acronym indicating amusement or hearty laughter. In this context, it emphasizes the humor the victor finds in the opponents' poor performance. |

### 3. Conclusion

The reconstructed sentence is a highly common post-match taunt used by the winning team against the losing team. It encapsulates the often-aggressive and competitive trash-talking environment prevalent in online gaming communities during the early 2000s. The sequence `gg ez` is a classic micro-aggression, often intended to provoke a reaction.

--- [Contextual Sources] ---
[1] https://www.reddit.com/r/LeagueOfMemes/comments/qkzvgx/ggez_noobs/
[2] https://steamcommunity.com/app/386360/discussions/0/3802776599344919328/
[3] https://www.reddit.com/r/VALORANT/comments/q1myri/people_who_type_gg_ez_at_the_end_of_the_round_are/

============================================================
```  

💡 Important Notes  
- Activate the virtual environment before running the project.  
- Do not upload .env to GitHub.  
- To save updated dependencies:  
```bash
pip freeze > requirements.txt
```  

---

🧰 Tech Stack  
- Language: Python  
- AI: Google Gemini API  
- Libraries: google-generativeai, nltk, textblob, dotenv, pandas 

---

👏 Acknowledgments  
- Google Gemini API for AI text generation  
- OpenAI documentation  
- Instructors for guidance and feedback  

---

📜 License  
This project is intended for academic and educational purposes only.  
