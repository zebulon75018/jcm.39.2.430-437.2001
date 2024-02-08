import sys
import cv2
import numpy as np
import matplotlib.pyplot as plt

def image_difference_heatmap(image1_path, image2_path):
    # Read the images
    image1 = cv2.imread(image1_path, cv2.IMREAD_GRAYSCALE)
    image2 = cv2.imread(image2_path, cv2.IMREAD_GRAYSCALE)

    # Compute the absolute difference between the images
    difference = cv2.absdiff(image1, image2)

    # Create a heatmap of the difference
    plt.imshow(difference, cmap='hot', interpolation='nearest')
    plt.title('Difference Heatmap')
    plt.colorbar()
    plt.savefig('heatmap.png')  # Save the heatmap as PNG file
    #plt.show()

if __name__ == "__main__":
    # Check if the number of arguments is correct
    if len(sys.argv) != 3:
        print("Usage: python script.py <image1_path> <image2_path>")
        sys.exit(1)

    # Get the paths to the images from command line arguments
    image1_path = sys.argv[1]
    image2_path = sys.argv[2]

    # Compute and display the difference heatmap, and save it as PNG
    image_difference_heatmap(image1_path, image2_path)  