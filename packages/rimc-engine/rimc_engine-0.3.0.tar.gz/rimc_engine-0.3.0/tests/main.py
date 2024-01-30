from rimc_engine import open_apply_save
import os

def main():
    path = "orig/"    
    # name = "DSC_0005.JPG" # "IMG_20230228_134853.jpg"
    # apply_film(name)
    print(os.listdir(path))
    for f in os.listdir(path):
        open_apply_save(f)

if __name__ == "__main__":
    main()