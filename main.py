from colorama import Fore, Style, init
from capture_image import capture_image
from detectmood import detect_emotion
from play_music import play_music
import time

init(autoreset=True)

def main():
    print(Fore.CYAN + "╔═══════════════════════════════════════════════╗")
    print(Fore.CYAN + "║ 🎧  Welcome to the Mood-Based Music Player!  ║")
    print(Fore.CYAN + "╚═══════════════════════════════════════════════╝")

    print(Fore.YELLOW + "Initializing camera...")
    time.sleep(1)

    image_path = capture_image()
    
    if image_path:
        mood = detect_emotion(image_path)

        # Mood color themes
        color_map = {
            "happy": Fore.YELLOW,
            "sad": Fore.BLUE,
            "angry": Fore.RED,
            "neutral": Fore.WHITE,
            "surprise": Fore.CYAN,
            "fear": Fore.MAGENTA,
            "disgust": Fore.GREEN
        }

        mood_color = color_map.get(mood.lower(), Fore.WHITE)
        print(mood_color + Style.BRIGHT + f"💫 Final Mood: {mood.upper()}")

        play_music(mood)
    else:
        print(Fore.RED + "❌ No image captured. Exiting...")

if __name__ == "__main__":
    main()

