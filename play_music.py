import os
import random
import pygame

def play_music(mood):
    """
    Plays a random song from the mood folder.
    Allows skipping to the next song by pressing 'n' key.
    """
    mood = mood.lower()
    folder = os.path.join("music", mood)

    if not os.path.exists(folder):
        print(f"❌ No folder found for mood: {mood}")
        return

    songs = [os.path.join(folder, f) for f in os.listdir(folder) if f.endswith(('.mp3', '.wav'))]

    if not songs:
        print("❌ No songs found in folder.")
        return

    pygame.mixer.init()
    print(f"🎶 Found {len(songs)} songs for mood: {mood}")

    current_index = random.randint(0, len(songs) - 1)
    playing = True

    while True:
        song = songs[current_index]
        print(f"🎵 Now playing: {os.path.basename(song)}")

        pygame.mixer.music.load(song)
        pygame.mixer.music.play()

        # Wait for the song to end or for user to press 'n'
        while pygame.mixer.music.get_busy():
            print("▶ Press 'n' for next song or 'q' to quit.", end="\r")

            # Check keyboard input
            import msvcrt  # Windows-only for key detection
            if msvcrt.kbhit():
                key = msvcrt.getch().decode("utf-8").lower()
                if key == 'n':
                    print("\n⏭ Skipping to next song...")
                    pygame.mixer.music.stop()
                    current_index = (current_index + 1) % len(songs)
                    break
                elif key == 'q':
                    print("\n👋 Exiting player.")
                    pygame.mixer.music.stop()
                    return

    pygame.mixer.quit()
