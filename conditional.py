from PIL import ImageGrab
from image import ImageProcessingv2
from thefuzz import fuzz
from config import *
import pytesseract


class Condition:
    
    # Initialize Image Processor
    image_processor = ImageProcessingv2(IMG_DIR)


    def is_battle_result_available() -> bool:
        try:
            # Capture a region of the screen using Pillow
            x, y, width, height = 373, 370, 310, 65  # Define the region coordinates and dimensions
            screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
            
            # Convert the captured region to a format that Tesseract can process
            screenshot.save(f"{IMG_DIR}/is_battle_result.png")
                        
            # Perform OCR on the captured region using Tesseract
            extracted_text = pytesseract.image_to_string(f"{IMG_DIR}/is_battle_result.png", lang='ENG')       
            match_percent = int(fuzz.partial_ratio(extracted_text.strip().lower(), 'battle results'))
                    
            # Check if the extracted text is similar to the desired text
            if match_percent >= MATCH_PERCENT:
                return True
            else:
                return False
        except:
            return False
  

    def is_attack_available() -> bool:
        try:
            # Capture a region of the screen using Pillow
            x, y, width, height = 1058, 1083, 185, 65  # Define the region coordinates and dimensions
            screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
            
            # Convert the captured region to a format that Tesseract can process
            screenshot.save(f"{IMG_DIR}/is_attack_available.png")
            
            # Perform Threshold 
            threshold_value = 150
            image = screenshot.convert("L").point(lambda p: p > threshold_value and 255)             
            
            # Perform OCR on the captured region using Tesseract
            extracted_text = pytesseract.image_to_string(image, lang='ENG')    
            match_percent = int(fuzz.partial_ratio(extracted_text.strip().lower(), 'fight'))
                    
            # Check if the extracted text is similar to the desired text
            if match_percent >= MATCH_PERCENT:
                return True
            else:
                return False
        except:
            return False      
  
     
    def is_fight_available() -> bool:
        try:
            # Capture a region of the screen using Pillow
            x, y, width, height = 235, 1190, 120, 35  # Define the region coordinates and dimensions
            screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
            
            # Convert the captured region to a format that Tesseract can process
            screenshot.save(f"{IMG_DIR}/is_fighting.png")
                        
            # Perform OCR on the captured region using Tesseract
            extracted_text = pytesseract.image_to_string(f"{IMG_DIR}/is_fighting.png", lang='ENG')
            
            #print(extracted_text.strip())
            #print(len(extracted_text.strip()))
            
            # Check if the extracted text is similar to the desired text
            if extracted_text.strip() == 'CoH':
                return False
            #elif len(extracted_text.strip()) == 0:
            #    return False
            else:
                return True
        except:
            return False
    
    
    def is_monster_attraction_active() -> bool:
        try:
            # Define the region coordinates and dimensions
            x, y, width, height = 32, 1070, 410, 35  
            screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
            
            # Convert the captured region to a format that Tesseract can process
            screenshot.save(f"{IMG_DIR}/is_monster_attraction_card.png")
                        
            # Perform OCR on the captured region using Tesseract
            extracted_text = pytesseract.image_to_string(screenshot, lang='eng', config='--psm 6')
        # print(extracted_text.strip().lower())

            # Check if the extracted text is similar to the desired text
            if extracted_text.strip().lower() == 'monster attraction card':
                return True
            else:
                return False
        except:
            return False

  
    def is_health_low(game_state, player:int) -> bool:
           
        if player == 1:
            try:
                score1, score2 = Condition.image_processor.extract_number(x=431, y=443, width=215, height=46, order=1)
                
                if score1 != -2 and score2 != -2:
                    percent = round((score1/score2) * 100,2)
                    print(f'{score1}/{score2} = {percent}%')  

                if score1 >= 0 and score2 >= 0:
                    game_state.alt_percent.append(percent)
                    if len(game_state.alt_percent) > 0:
                        if int(game_state.alt_percent[-1]) >= HEALTH_LESS_THAN or game_state.alt_percent[-1] == 0.0:
                            #print('False I')
                            game_state.is_health_low = False
                            game_state.item = None
                        else:
                            #print('True I')
                            game_state.is_health_low = True
                            game_state.item = 'max_hp_potion'
                    else:
                        #print('False II')
                        game_state.is_health_low = False
                        game_state.item = None
                else:
                    if len(game_state.alt_percent) > 0:
                        if int(game_state.alt_percent[-1]) >= HEALTH_LESS_THAN or game_state.alt_percent[-1] == 0.0:
                            #print('False III')
                            game_state.is_health_low = False
                            game_state.item = None
                        else:
                            #print('True II')
                            game_state.is_health_low = True
                            game_state.item = 'max_hp_potion'
                    else:
                        #print('False IV')
                        game_state.is_health_low = False
                        game_state.item = None   
            except Exception:
                if len(game_state.alt_percent) > 0:
                    if int(game_state.alt_percent[-1]) >= HEALTH_LESS_THAN or game_state.alt_percent[-1] == 0.0:
                        print('False V')
                        game_state.is_health_low = False
                        game_state.item = None
                    else:
                        print('True III')
                        game_state.is_health_low = True
                        game_state.item = 'max_hp_potion'
                else:
                    print('False VI')
                    game_state.is_health_low = False
                    game_state.item = None
                   
        elif player == 2:
            try:
                # Get Scores from Image
                score1, score2 = Condition.image_processor.extract_number(x=1431, y=443, width=215, height=46, order=2)  
                
                # If not Scores are available dont Print Anything           
                if score1 != -2 and score2 != -2:
                    percent = round((score1/score2) * 100,2)
                    print(f'{score1}/{score2} = {percent}%')              
                    
                # Check to see 
                if score1 >= 0 and score2 >= 0:
                    game_state.alt_percent.append(percent)
                    if len(game_state.alt_percent) > 0:
                        if int(game_state.alt_percent[-1]) <= CAPTURE_HEALTH_LESS_THAN and game_state.alt_percent[-1] != 0.0:
                            print(int(game_state.alt_percent[-1]) <= CAPTURE_HEALTH_LESS_THAN )
                            print(game_state.alt_percent[-1])
                            print('True I')
                            return True, None
                        else:                          
                            print('False I')
                            return False, None
                    else:
                        print('False II')
                        return False, None
                else:
                    if len(game_state.alt_percent) > 0:
                        if int(game_state.alt_percent[-1]) <= CAPTURE_HEALTH_LESS_THAN and game_state.alt_percent[-1] != 0.0:
                            print('True II')
                            return True, None
                        else:
                            print('False III')
                            return False, None
                    else:
                        print('False IV')
                        return False, None                     
            except Exception:
                if len(game_state.alt_percent) > 0:
                    if int(game_state.alt_percent[-1]) <= CAPTURE_HEALTH_LESS_THAN and game_state.alt_percent[-1] != 0.0:
                        print('False V')
                        return False, None
                    else:
                        print('True III')
                        return True, 'max_hp_potion'
                else:
                    print('False VI')
                    return False, None
     
     
    def is_on_capture_list(game_state) -> bool:
        try:
            # Get Text from Image
            text = Condition.image_processor.extract_text(x=1080, y=356, width=310, height=45, order=1)
            
            # Loop to see if Monster is on catch list
            for monster in CAPTURE_LIST:
                match_percent = fuzz.partial_ratio(monster, text.strip().upper())
                if match_percent > CAPTURE_PERCENT:
                    print(f'{text} in catch list!!')
                    game_state.is_on_catch_list = True
                    return
            print(f'{text} NOT in catch list!!')
        
        except:
            game_state.is_on_catch_list = False


    def is_arena_conquered(arena:str) -> bool:
        try:
            # Define the region coordinates and dimensions
            if arena == 'BRONZE':
                x, y, width, height = 940, 485, 150, 25 
            elif arena == 'SILVER':
                x, y, width, height = 940, 610, 150, 25  
            elif arena == 'GOLD':
                x, y, width, height = 940, 738, 150, 25 
            elif arena == 'PLATINUM':
                x, y, width, height = 940, 860, 150, 25  
            elif arena == 'DIAMOND':
                x, y, width, height = 940, 990, 150, 25
            else:
                print('Error: No Arena provided')
                
            screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
            
            # Convert the captured region to a format that Tesseract can process
            screenshot.save(f"{IMG_DIR}/is_participation_allow.png")
                        
            # Perform OCR on the captured region using Tesseract
            extracted_text = pytesseract.image_to_string(screenshot, lang='eng', config='--psm 6')
            #print(extracted_text.strip().lower())

            # Check if the extracted text is similar to the desired text
            if extracted_text.strip().lower() == 'can participate':
                return True
            else:
                return False
        except:
            return False
        

    def is_teamate_champion(arena:str):
        try:
            # Define the region coordinates and dimensions
            if arena == 'BRONZE':
                x, y, width, height = 435, 535, 230, 25  
            elif arena == 'SILVER':
                x, y, width, height = 435, 660, 230, 25  
            elif arena == 'GOLD':
                x, y, width, height = 435, 785, 230, 25  
            elif arena == 'PLATINUM':
                x, y, width, height = 435, 910, 230, 25  
            elif arena == 'DIAMOND':
                x, y, width, height = 435, 1035, 230, 25
            else:
                print('Error: No Arena provided') 
                
            screenshot = ImageGrab.grab(bbox=(x, y, x + width, y + height))
            
            # Convert the captured region to a format that Tesseract can process
            screenshot.save(f"{IMG_DIR}/is_teamate_champion.png")
                        
            # Perform OCR on the captured region using Tesseract
            extracted_text = pytesseract.image_to_string(screenshot, lang='eng', config='--psm 6')
            print(extracted_text.strip().lower())

            # Check if the extracted text is similar to the desired text
            if extracted_text.strip().lower() == 'gameover':
                return True
            else:
                return False
        except:
            return False
