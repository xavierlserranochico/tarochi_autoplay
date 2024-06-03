from datetime import datetime, timedelta
from config import *
import re


class Misc:
    
    def check_date(RUN_TIME):
        now = datetime.now()
        time_difference = now - RUN_TIME

        #print(time_difference)  

        # Check if the difference is more than 30 minutes
        if time_difference > timedelta(minutes=25):
            # Run your code here
            #print("Time difference is more than 30 minutes")
            return True
        else:
            #print("Time difference is not more than 30 minutes")
            return False
    
    def split_by_custom_delimiters(text: str):
        # Split by '/', " '", "_ '", ". '", or " "
        parts = re.split(r'/| \'|_ \'|\. \'| ', text)
        # Remove any empty parts resulting from the split
        parts = [part for part in parts if part]
        return parts
   
    def clean_blob(extracted_blob: str):
        # Correct common OCR errors
        corrected_blob = ''.join(CORRECTIONS.get(char, char) for char in extracted_blob)
        if corrected_blob != '':
            print(corrected_blob)
        
        # Split the corrected text by '/'
        parts = Misc.split_by_custom_delimiters(corrected_blob)
        if parts != []:
            print(parts)
        
        if len(parts) != 2:
            #print(f"Invalid format after split: {corrected_blob}")
            return -2, -2
        
        score1, score2 = parts

        #print(f"Original blob: {extracted_blob}")
        print(f"Corrected blob: {corrected_blob}")
        print(f"Score 1: {score1}")
        print(f"Score 2: {score2}")
        print()
        
        # Validate and correct scores
        if not score1.isdigit() or not score2.isdigit():
            print("Non-digit characters detected. Attempting to correct...")
            
            score1 = ''.join(CORRECTIONS.get(char, char) for char in score1)
            score2 = ''.join(CORRECTIONS.get(char, char) for char in score2)
            
            # Final validation
            if not score1.isdigit() or not score2.isdigit():
                print(f"Unable to correct to valid numbers: score1={score1}, score2={score2}")
                return -1, -1
        
        return score1, score2