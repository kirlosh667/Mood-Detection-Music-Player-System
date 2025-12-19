import cv2
from colorama import Fore, Style, init

init(autoreset=True)

def capture_image():
    """Capture image from webcam and save it as 'face.jpg'"""
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print(Fore.RED + "❌ Could not access webcam.")
        return None

    print(Fore.CYAN + Style.BRIGHT + "📸 Press 'Enter' to capture the image...")

    while True:
        ret, frame = cap.read()
        if not ret:
            print(Fore.RED + "⚠️ Failed to capture image.")
            break

        cv2.imshow("Camera - Press Enter to Capture", frame)
        key = cv2.waitKey(1) & 0xFF

        if key == 13:  # Enter key
            save_path = "face.jpg"
            cv2.imwrite(save_path, frame)
            print(Fore.GREEN + f"✅ Image saved as {save_path}")
            break

    cap.release()
    cv2.destroyAllWindows()
    return "face.jpg"
