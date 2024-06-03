from PIL import ImageGrab, ImageOps, Image
from misc import Misc
import matplotlib.pyplot as plt
from config import *
import pytesseract
import numpy as np
import cv2 as cv
import easyocr


class ImageProcessing:
    def __init__(self, img_dir: str):
        """Initialize with the directory to save images."""
        self.img_dir = img_dir

    def capture_screenshot(self, x: int, y: int, width: int, height: int, order: int):
        """Capture and save a screenshot of the specified region."""
        screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
        #screenshot_path = f"{self.img_dir}/health_bar{order}.png"
        #screenshot.save(screenshot_path)
        return screenshot

    def process_image(self, image, order: int):
        """Convert image to grayscale and apply thresholding."""
        screenshot_gray = ImageOps.grayscale(image)
        screenshot_gray.save(f"{self.img_dir}/screenshot_grayscale{order}.png")
        threshold_value = 200  # Adjust as needed
        screenshot_thresholded = screenshot_gray.point(
            lambda p: 255 if p < threshold_value else 0)
        screenshot_thresholded.save(f"{self.img_dir}/screenshot_thresholded{order}.png")
        return screenshot_thresholded

    def extract_text(self, coordinate: int, order: int) -> str:
        """Capture a screen region and extract text using OCR."""
        x, y, width, height = coordinate, 443, 88, 46
        screenshot = self.capture_screenshot(x, y, width, height, order)
        processed_image = self.process_image(screenshot, order)
        extracted_text = pytesseract.image_to_string(
            processed_image, lang='eng', config='--psm 7')
        return extracted_text.strip()

    def extract_number(self, coordinate: int, order: int) -> int:
        """Capture a screen region and extract a numeric value using OCR."""
        x, y, width, height = coordinate, 443, 88, 46
        screenshot = self.capture_screenshot(x, y, width, height, order)
        processed_image = self.process_image(screenshot, order)
        extracted_text = pytesseract.image_to_string(
            processed_image, lang='eng', config='--psm 10-c tessedit_char_whitelist=0123456789')
        extracted_number = ''.join(filter(str.isdigit, extracted_text))
        try:
            return int(extracted_number)
        except ValueError:
            return -1  # Return a default value if OCR fails


class ImageProcessingv2:
    
    def __init__(self, img_dir: str):
        """Initialize with the directory to save images."""
        self.img_dir = img_dir
        self.reader = easyocr.Reader(['en'])  # You can specify more languages

    def convert_to_grayscale(self, screenshot, order):
        screenshot_gray = ImageOps.grayscale(screenshot)
        screenshot_gray.save(f"{self.img_dir}test_screenshot_grayscale{order}.png")
        
    def capture_screenshot(self, x: int, y: int, width: int, height: int, order: int):
        """Capture and save a screenshot of the specified region."""
        screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
        self.convert_to_grayscale(screenshot, order)
        return f"{self.img_dir}test_screenshot_grayscale{order}.png"

    def remove_icc_profile(self, image_path: str) -> str:
        # Open the image using PIL
        with Image.open(image_path) as img:
            # Remove ICC profile by saving without the ICC profile
            if "icc_profile" in img.info:
                img.info.pop("icc_profile")
            # Save the image to a new file
            img.save(image_path)
            return image_path

    def show_image(self, image):
        """Utility function to display an image using matplotlib."""
        plt.figure()
        plt.imshow(image, cmap='gray')
        plt.axis('off')  # Hide axes
        plt.show()

    def invert_image_colors(self, image):
        return cv.bitwise_not(image)

    def noise_removal(self, image):
        kernel = np.ones((1, 1), np.uint8)
        image = cv.dilate(image, kernel, iterations=1)
        kernel = np.ones((1, 1), np.uint8)
        image = cv.erode(image, kernel, iterations=1)
        image = cv.morphologyEx(image, cv.MORPH_CLOSE, kernel)
        #image = cv.medianBlur(image, 2)
        return (image)

    def read_image(self, processed_image_path):
        return cv.imread(processed_image_path, cv.IMREAD_UNCHANGED)

    def get_text_from_blob(self, extracted_blob:str):
        return " ".join([text for (_, text, _) in extracted_blob])

    def threshold(self, inverted_image):
         _, thresh_image = cv.threshold(inverted_image, 169, 255, cv.THRESH_BINARY)
         return thresh_image
         
    def get_number_from_image(self, image_path, order: int):
        """Convert image to grayscale and apply thresholding."""
        # Remove ICC profile from image
        processed_image_path = self.remove_icc_profile(image_path)

        # Read image
        img = self.read_image(processed_image_path)
        if img is None:
            print(f"Failed to load image from {image_path}")
            return -3

        # Invert Image Colors
        inverted_image = self.invert_image_colors(img)     

        # Apply a threshold to convert the image to black and white
        thresh_image = self.threshold(inverted_image)

        # Reduce Image Noise
        no_noise = self.noise_removal(thresh_image)

        # Show the intermediate images for debugging       
        #self.show_image(no_noise)

        # Use EasyOCR to extract text from the image
        extracted_blob = self.reader.readtext(no_noise)

        # Extract and print the text
        extracted_blob = self.get_text_from_blob(extracted_blob)

        # Clean Blob and extract as much as possible? lol
        score1, score2 = Misc.clean_blob(extracted_blob)

        try:
            return int(score1), int(score2)
        except ValueError:
            return -1, -1  # Return a default value if OCR fails
     
    def get_text_from_image(self, image_path, order: int):
        """Convert image to grayscale and apply thresholding."""
        # Remove ICC profile from image
        processed_image_path = self.remove_icc_profile(image_path)

        # Read image
        img = self.read_image(processed_image_path)
        if img is None:
            print(f"Failed to load image from {image_path}")
            return -3

        # Invert Image Colors
        inverted_image = self.invert_image_colors(img)     

        # Apply a threshold to convert the image to black and white
        thresh_image = self.threshold(inverted_image)

        # Reduce Image Noise
        no_noise = self.noise_removal(thresh_image)

        # Show the intermediate images for debugging       
        #self.show_image(no_noise)

        # Use EasyOCR to extract text from the image
        extracted_blob = self.reader.readtext(no_noise)

        # Extract and print the text
        extracted_blob = self.get_text_from_blob(extracted_blob)

        try:
            return extracted_blob
        except ValueError:
            return -1, -1  # Return a default value if OCR fails
           
    def extract_number(self, x: int, y: int, width: int, height: int, order: int) -> int:
        """Capture a screen region and extract a numeric value using OCR."""       
        image_path = self.capture_screenshot(x, y, width, height, order)
        return self.get_number_from_image(image_path, order)  
                         
    def extract_text(self, x: int, y: int, width: int, height: int, order: int) -> str:
        """Capture a screen region and extract text using OCR."""
        image_path = self.capture_screenshot(x, y, width, height, order)        
        return self.get_text_from_image(image_path, order)
        """
        #processed_image = self.process_image(screenshot, order)
        #extracted_text = pytesseract.image_to_string(
        #    processed_image, lang='eng', config='--psm 7')
        #return extracted_text.strip()
        """




# Example usage:
#if __name__ == "__main__":
#    image_processor = ImageProcessing(IMG_DIR)

    # Extract text example
    #text_result = image_processor.extract_text(coordinate=431, order=1)
    #print(f"Extracted Text: {text_result}")

    # Extract number example
#    number_result = image_processor.extract_number(coordinate=431, order=1)
#    print(f"Extracted Number: {number_result}")
