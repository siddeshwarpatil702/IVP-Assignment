import cv2

path = r"C:\Users\siddeshwar\OneDrive\Desktop\Image n Video Processing\Screenshot 2025-09-16 193602.png"

img = cv2.imread(path)

if img is None:
    print("Unable to read image")
else:
    print("Image loaded successfully!")

    height, width, channels = img.shape
    print("Original Height:", height)
    print("Original Width:", width)

    rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    new_height, new_width, channels = rotated.shape
    print("Rotated Height:", new_height)
    print("Rotated Width:", new_width)

    cv2.imshow("Original Image", img)
    cv2.imshow("Rotated Image", rotated)

    cv2.imwrite("rotated_image.jpg", rotated)

    cv2.waitKey(0)
    cv2.destroyAllWindows()