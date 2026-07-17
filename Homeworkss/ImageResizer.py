import cv2
import os

def resize_image(img_path):
    img = cv2.imread(img_path)
    if img is None:
        print("Error: Could not load image!")
        return

    sizes = { "small": (400, 400), "medium": (800, 600), "large": (1280, 720)  }

    for label, (w, h) in sizes.items():
        out = cv2.resize(img, (w, h))
        
        filename = f"resized_{label}.jpg"
        cv2.imwrite(filename, out)
        print(f"Saved: {filename}")
        
        cv2.imshow(label, out)
        cv2.waitKey(0)
        
    print("Done")
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    file = "image.jpg"
