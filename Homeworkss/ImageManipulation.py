import cv2
import matplotlib.pyplot as plt

img = cv2.imread("input.jpg")

if img is None:
    print("Error: Could not load 'input.jpg'. Make sure the image is in this folder!")
else:
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    h, w, _ = img_rgb.shape

    rotated = cv2.rotate(img_rgb, cv2.ROTATE_90_CLOCKWISE)

    side = int(min(h, w) * 0.6)
    cy, cx = h // 2, w // 2
    
    y1, y2 = cy - (side // 2), cy + (side // 2)
    x1, x2 = cx - (side // 2), cx + (side // 2)
    
    cropped = img_rgb[y1:y2, x1:x2]

    bright = cv2.convertScaleAbs(img_rgb, alpha=1.0, beta=50)

    plt.figure(figsize=(10, 8))

    plt.subplot(2, 2, 1)
    plt.title("Original")
    plt.imshow(img_rgb)
    plt.axis("off")

    plt.subplot(2, 2, 2)
    plt.title("Rotated (90 Deg)")
    plt.imshow(rotated)
    plt.axis("off")

    plt.subplot(2, 2, 3)
    plt.title("Better Center Crop (Square)")
    plt.imshow(cropped)
    plt.axis("off")

    plt.subplot(2, 2, 4)
    plt.title("Brighter (Beta +50)")
    plt.imshow(bright)
    plt.axis("off")

    plt.tight_layout()
    plt.show()