import cv2

img = cv2.imread("input.jpg")

if img is None:
    print("Error")
else:
    h, w, _ = img.shape

    margin = 40
    y_pos = h // 2
    pt1 = (margin, y_pos)
    pt2 = (w - margin, y_pos)

    color = (0, 255, 0)
    thick = 3
    
    cv2.Line(img, pt1, pt2, color, thick, tipLength=0.05)
    cv2.Line(img, pt2, pt1, color, thick, tipLength=0.05)

    text = f"Width: {w}px"
    font = cv2.FONT_HERSHEY_SIMPLEX
    scale = 1.0
    text_thick = 2
    
    (text_w, text_h), _ = cv2.getTextSize(text, font, scale, text_thick)
    text_x = (w - text_w) // 2
    text_y = y_pos - 20

    cv2.putText(img, text, (text_x + 2, text_y + 2), font, scale, (0, 0, 0), text_thick + 1, cv2.LINE_AA)
    cv2.putText(img, text, (text_x, text_y), font, scale, (255, 255, 255), text_thick, cv2.LINE_AA)

    cv2.imwrite("annotated_width.jpg", img)
    print(f"Saved: annotated_width.jpg (Width detected: {w}px)")

    cv2.imshow("Annotated Width", img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()