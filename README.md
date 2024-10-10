# Moodify 🎵🎧

Moodify is a Flask web app that generates a personalized playlist for users based on their Spotify listening history and their current mood. Users can log into Spotify, describe the vibe they are feeling, and Moodify will use AI (GPT model) to interpret the mood and generate a playlist by leveraging Spotify's API.

## Getting Started

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/moodify.git
   cd moodify
2. Set up a virtual environment and install dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
3. Run the app:
   ```bash
   python -m flask --app main.py run --port 8080 --debug
4. Open your browser and navigate to:
   
   **[http://127.0.0.1:8080](http://127.0.0.1:8080)**