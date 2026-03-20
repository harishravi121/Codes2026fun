#write a code for a image in camera of laptop based queries to gemini api to make a humaoid hand solve a rubiks cube based on a rubiks cube solver from github 

import cv2
import kociemba
from google import genai
from google.genai import types

# Setup Gemini Client
client = genai.Client(api_key="YOUR_GEMINI_API_KEY")

def capture_face(face_name):
    """Captures an image from the laptop webcam."""
    cap = cv2.VideoCapture(0)
    print(f"Show the {face_name} face to the camera and press 's' to capture.")
    while True:
        ret, frame = cap.read()
        cv2.imshow('Capture Cube Face', frame)
        if cv2.waitKey(1) & 0xFF == ord('s'):
            cv2.imwrite(f"{face_name}.jpg", frame)
            break
    cap.release()
    cv2.destroyAllWindows()
    return f"{face_name}.jpg"

def get_cube_state_from_gemini(image_paths):
    """Sends 6 images to Gemini to get the Kociemba cubestring."""
    # We prompt Gemini to return the specific 54-character string format
    prompt = """
    Analyze these 6 images of a Rubik's Cube (Up, Down, Front, Back, Left, Right).
    Provide the cube state as a single 54-character string using these letters:
    U (White), R (Red), F (Green), D (Yellow), L (Orange), B (Blue).
    Format: UUUUUUUUURRRRRRRRRFFFFFFFFFDDDDDDDDDLLLLLLLLLBBBBBBBBB
    Only return the string.
    """
    
    parts = [prompt]
    for path in image_paths:
        with open(path, "rb") as f:
            parts.append(types.Part.from_bytes(data=f.read(), mime_type="image/jpeg"))

    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=parts
    )
    return response.text.strip()

# --- Execution Flow ---
faces = ['Up', 'Right', 'Front', 'Down', 'Left', 'Back']
images = [capture_face(f) for f in faces]

print("Analyzing cube with Gemini...")

cube_string = get_cube_state_from_gemini(images)


def execute_move(move_char):
    if move_char == "R":
        hand.move_to_right_face()
        hand.perform_90_degree_turn()
    elif move_char == "R2":
        hand.move_to_right_face()
        hand.perform_180_degree_turn()
    # ... and so on
    
# Iterate through the Kociemba solution
for move in solution.split():
    execute_move(move)

try:
    solution = kociemba.solve(cube_string)
    print(f"Solution Found: {solution}")
    # Example Output: "R2 U' B L F'..."
except Exception as e:
    print(f"Error: Could not solve string. Check image quality. {e}")
