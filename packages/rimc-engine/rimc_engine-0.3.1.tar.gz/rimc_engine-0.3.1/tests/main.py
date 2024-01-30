from rimc_engine import open_apply_save
import os
from datetime import datetime



def main():
    path = "orig/"    
    
    print(os.listdir(path))
    for f in os.listdir(path):
        # Get the current timestamp
        current_timestamp = round(datetime.timestamp(datetime.now())/60)
        print(current_timestamp)
        open_apply_save(f, suffix=str(current_timestamp))

if __name__ == "__main__":
    main()



"""
EFFECTS LOG
28442403 - original 'CLSC':Recipe(name='CLSC', 
                  brightness=1, contrast=3, blur=1,
                  sharpness=1, color=1, grain=1)



"""