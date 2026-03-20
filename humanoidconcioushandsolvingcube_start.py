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



Building a system where a humanoid hand solves a Rubik's cube using Gemini for vision and a GitHub-based solver is an ambitious robotics project. 

To achieve this, you need to bridge three domains: **Computer Vision** (Gemini API), **Logic** (Kociemba Solver), and **Hardware Control** (Humanoid Hand).

### 1. Prerequisites
You will need to install the following libraries:
* `opencv-python` (for webcam access)
* `google-generativeai` (Gemini API)
* `kociemba` (The industry-standard Rubik's solver)

```bash
pip install opencv-python google-generativeai kociemba
```

---

### 2. The Integrated Python Script
This script captures the cube's state via your laptop camera, sends it to Gemini to translate colors into a string format, and then uses the Kociemba algorithm to generate the moves.

```python
import cv2
import google.generativeai as genai
import kociemba
import PIL.Image

# 1. Setup Gemini API
genai.configure(api_key="YOUR_GEMINI_API_KEY")
model = genai.GenerativeModel('gemini-1.5-flash')

def capture_cube_faces():
    """Captures 6 images (one for each face) from the laptop webcam."""
    cam = cv2.VideoCapture(0)
    faces = []
    print("Position each face of the cube. Press 'c' to capture, 'q' to finish.")
    
    while len(faces) < 6:
        ret, frame = cam.read()
        cv2.imshow("Cube Capture", frame)
        
        key = cv2.waitKey(1)
        if key == ord('c'):
            # Save frame as PIL image for Gemini
            color_converted = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            pil_img = PIL.Image.fromarray(color_converted)
            faces.append(pil_img)
            print(f"Captured face {len(faces)}/6")
        elif key == ord('q'):
            break
            
    cam.release()
    cv2.destroyAllWindows()
    return faces

def get_cube_string(images):
    """Sends images to Gemini to get the 54-character cube state string."""
    prompt = """
    Analyze these 6 images of a Rubik's cube. 
    Provide the state as a single 54-character string using:
    U (Up/White), R (Right/Red), F (Front/Green), D (Down/Yellow), L (Left/Orange), B (Back/Blue).
    The order must be: U1-U9, R1-R9, F1-F9, D1-D9, L1-L9, B1-B9.
    Only return the string.
    """
    response = model.generate_content([prompt, *images])
    return response.text.strip()

def solve_cube():
    # Step A: Capture vision
    face_images = capture_cube_faces()
    
    # Step B: Vision to Logic (via Gemini)
    # Note: For production, you'd want to handle Gemini's potential formatting errors
    cube_state = get_cube_string(face_images)
    print(f"Detected State: {cube_state}")
    
    try:
        # Step C: Generate Solution
        solution = kociemba.solve(cube_state)
        print(f"Solution Moves: {solution}")
        
        # Step D: Hand Control (Conceptual)
        # map_moves_to_hand(solution)
        
    except Exception as e:
        print(f"Error solving: {e}. Ensure the cube string was accurate.")

if __name__ == "__main__":
    solve_cube()
```

---

### 3. Controlling the Humanoid Hand
A "humanoid hand" (like the Shadow Hand or a DIY servo-based hand) doesn't understand "R" or "U'". You must map these moves to specific motor sequences.

**Mapping Logic:**
* **Move R (Right Face):** The hand must hold the cube with the thumb and palm, then use the pinky or index finger to flick the right layer 90°.
* **Rotation:** If the hand only has one "active" side, you may need a move called a **Cube Rotation** (flipping the whole cube) before executing the face turn.

**Conceptual code for the hand interface:**
```python
def execute_move(move):
    if move == "R":
        servo_finger_index.move(90) # Flick the layer
        servo_wrist.rotate(0)       # Reset
    elif move == "U":
        # Humanoid hands often rotate the whole cube to move the 'Up' face to 'Front'
        robot_arm.flip_cube()
        execute_move("F") 
```

### 4. Implementation Tips
* **Lighting:** Gemini is great at color, but glare on plastic stickers can confuse it. Try to use matte stickers or diffuse lighting.
* **GitHub Resource:** If you are using a specific hand like the **Shadow Hand**, look for the `urdf` models on GitHub to simulate the movements in ROS (Robot Operating System) before trying it on hardware.
* **The "String" Format:** Kociemba expects exactly 54 characters. If Gemini returns 53 or 55, the script will crash. You may need to prompt Gemini to "Double-check your count."

**Would you like me to help you write the specific mapping logic for a particular robot hand controller (like Arduino or ROS)?**
