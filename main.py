import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class AIArcheologist:
    """
    A class to reconstruct text fragments using AI and find contextual sources.
    """
    def __init__(self, gemini_key, google_key, search_engine_id):
        """
        Initializes the AIArcheologist with necessary API keys and IDs.

        Args:
            gemini_key (str): The API key for the Gemini API.
            google_key (str): The API key for the Google Custom Search API.
            search_engine_id (str): The Custom Search Engine ID.
        """
        if not all([gemini_key, google_key, search_engine_id]):
            raise ValueError("API keys and Search Engine ID must be provided.")
            
        self.gemini_key = gemini_key
        self.google_key = google_key
        self.search_engine_id = search_engine_id
        
        genai.configure(api_key=self.gemini_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash-preview-09-2025')

    def reconstruct_fragment(self, fragment):
        """
        Uses the Gemini API to reconstruct the given text fragment.

        Args:
            fragment (str): The text fragment to reconstruct.

        Returns:
            str: The reconstructed text, including explanations of slang.
        
        Raises:
            Exception: If the API call fails.
        """
        print("🤖 Calling the 'AI Archaeologist' to reconstruct the fragment...")
        try:
            prompt = f"""You are an 'AI Archeologist' specializing in early 2000s internet culture.
Your task is to take the following fragmented text from an old forum and reconstruct
it into a complete, coherent sentence. You must also explain the meaning of any slang used.

Here is the fragment: '{fragment}'"""
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            raise Exception(f"Error during AI reconstruction: {e}") from e

    def search_for_context(self, query):
        """
        Searches the web for context using the Google Custom Search API.

        Args:
            query (str): The search query.

        Returns:
            list: A list of relevant URLs.

        Raises:
            HttpError: If the Google Search API call fails.
        """
        print("🌐 Searching the archives for contextual sources...")
        try:
            service = build("customsearch", "v1", developerKey=self.google_key)
            result = service.cse().list(
                q=query,
                cx=self.search_engine_id,
                num=3
            ).execute()
            
            return [item.get('link', '') for item in result.get('items', [])]
        except HttpError as e:
            raise HttpError(f"Error during web search: {e.resp.status} {e.resp.reason}", e.resp) from e


    @staticmethod
    def generate_report(original, reconstructed, urls):
        """
        Formats and returns the final Reconstruction Report.

        Args:
            original (str): The original text fragment.
            reconstructed (str): The AI-reconstructed text.
            urls (list): A list of contextual URLs.

        Returns:
            str: A formatted report string.
        """
        report = "\n" + "="*60 + "\n"
        report += "          📜 AI ARCHAEOLOGIST RECONSTRUCTION REPORT 📜\n"
        report += "="*60 + "\n\n"
        
        report += "--- [Original Fragment] ---\n"
        report += f"> {original}\n\n"
        
        report += "--- [AI-Reconstructed Text & Analysis] ---\n"
        report += f"{reconstructed.strip()}\n\n"
        
        report += "--- [Contextual Sources] ---\n"
        if urls:
            for i, url in enumerate(urls, 1):
                report += f"[{i}] {url}\n"
        else:
            report += "No relevant sources were found in the archives.\n"
            
        report += "\n" + "="*60 + "\n"
        
        return report

def main():
    """
    Main function to run the application.
    """
    load_dotenv()
    
    try:
        archeologist = AIArcheologist(
            gemini_key=os.getenv("GEMINI_API_KEY"),
            google_key=os.getenv("GOOGLE_API_KEY"),
            search_engine_id=os.getenv("SEARCH_ENGINE_ID")
        )
    except ValueError as e:
        print(f"🔴 Configuration Error: {e}")
        print("   Please ensure GEMINI_API_KEY, GOOGLE_API_KEY, and SEARCH_ENGINE_ID are in your .env file.")
        return

    if len(sys.argv) < 2:
        print("🔴 Usage Error: Please provide a text fragment as a command-line argument.")
        print("   Example: python main.py \"omg lol brb g2g\"")
        return
        
    original_fragment = " ".join(sys.argv[1:])

    try:
        reconstructed_text = archeologist.reconstruct_fragment(original_fragment)
        context_urls = archeologist.search_for_context(original_fragment)
        final_report = AIArcheologist.generate_report(original_fragment, reconstructed_text, context_urls)
        print(final_report)

    except (Exception, HttpError) as e:
        print(f"\n❌ An error occurred during the reconstruction process: {e}")

if __name__ == "__main__":
    main()
