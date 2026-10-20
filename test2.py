import json
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

# -------------------------------------------------------------
# 1. Initialize the Client with API Key from .env
# -------------------------------------------------------------
load_dotenv()

api_key = os.environ.get("GEMINI_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY not found in .env file. Please check your .env configuration.")

client = genai.Client(api_key=api_key)


# -------------------------------------------------------------
# 2. Define the Local Tool Function (Step 5)
# Note: Type hints and docstrings are required so the LLM
# understands what the function does and what parameters it takes.
# -------------------------------------------------------------
def get_student_result(student_id: str) -> str:
    """Retrieves academic results, GPA, and standing for a given student ID.

    Args:
        student_id: The unique identifier for the student (e.g., 'STU-101', 'STU-102').
    """
    print(f"\n[LOCAL FUNCTION EXECUTED] Querying record for: {student_id}")

    mock_records = {
        "STU-101": {
            "name": "Amina Al-Balushi",
            "major": "Computer Science",
            "gpa": 3.85,
            "status": "Honor Roll",
            "credits_completed": 90,
        },
        "STU-102": {
            "name": "Marcus Vance",
            "major": "Mechanical Engineering",
            "gpa": 3.10,
            "status": "In Good Standing",
            "credits_completed": 64,
        },
    }

    normalized_id = student_id.strip().upper()
    data = mock_records.get(normalized_id)

    if data:
        return json.dumps({"found": True, "record": data})
    return json.dumps({"found": False, "error": f"No student found with ID {student_id}"})


# -------------------------------------------------------------
# 3. Connect to LLM and Run the Tool Calling Loop
# -------------------------------------------------------------
def run():
    # We use client.chats because it automatically executes tools locally
    # and submits the output back to the model without manual boilerplate.
    chat = client.chats.create(
        model="gemini-3.8-flash",
        config=types.GenerateContentConfig(
            tools=[get_student_result],  # Pass the function directly
            temperature=0.0,
        ),
    )

    query = "What is the GPA and standing of student STU-101?"
    print(f"User Query: {query}")

    # Send message to model
    response = chat.send_message(query)

    print("\n--- Final Model Output ---")
    print(response.text)


if __name__ == "__main__":
    run()