import cv2
import numpy as np

# calculates the centers of the given contours
def calculate_centers(contours):
    centers = []
    for contour in contours:
        moments = cv2.moments(contour)
        if moments["m00"] != 0:
            x_center = int(moments["m10"] / moments["m00"])
            y_center = int(moments["m01"] / moments["m00"])
            centers.append((x_center, y_center))
    return np.array(centers)

# fits a line to given points and draws it on the image
def draw_fitted_line(points, img):
    if len(points) > 0:
        [vx, vy, x0, y0] = cv2.fitLine(points, cv2.DIST_L2, 0, 0.01, 0.01)
        height, width = img.shape[:2]
        y1 = int((-x0 * vy / vx) + y0)
        y2 = int(((width - x0) * vy / vx) + y0)
        cv2.line(img, (width - 1, y2), (0, y1), (0, 0, 255), 2)

# Loads and preprocesses the image
img = cv2.imread("red.png")
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Defines HSV color range for detection
lower_hsv = np.array([0, 200, 140])
upper_hsv = np.array([160, 255, 230])

# Creates a mask and find contours
mask = cv2.inRange(hsv_img, lower_hsv, upper_hsv)
# the '_' is used as a placeholder to ignore the second value that gets returned by cv2.findContours
contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

# Calculates contour centers
contour_centers = calculate_centers(contours)

# Separates centers into left and right based on x-coordinate
img_width = img.shape[1]
left_side = contour_centers[contour_centers[:, 0] < img_width / 2]
right_side = contour_centers[contour_centers[:, 0] >= img_width / 2]

# Draws fitted lines on the image
draw_fitted_line(left_side, img)
draw_fitted_line(right_side, img)

# Saves the processed image
cv2.imwrite("answer.png", img)
