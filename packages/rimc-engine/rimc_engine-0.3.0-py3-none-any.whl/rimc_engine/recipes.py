"""const recipes = [
    new Recipe('classic vintage', 'CLSC', 'as it is now in rimc engine', null),
    new Recipe('gold', 'GOLD', 'kodak gold', 'https://film.recipes/2022/07/01/classic-gold-like-expired-film-kodak-gold/'),
    new Recipe('portrait', 'PORT', 'portra', 'https://film.recipes/2022/05/15/kodak-portra-grainy-for-a-portra-400-look/'),
    new Recipe('super', 'SUPR', 'superia', 'https://film.recipes/2022/05/24/mother-superia-the-anytime-fujicolor-film/'),
    new Recipe('silver bw', 'bwSV', 'silvertone', 'https://film.recipes/2022/09/15/silvertone-99-for-deep-metallic-mono/'),
    new Recipe('retro bw', 'bwRE', 'retro bw', 'https://film.recipes/2022/08/22/claunch-72-monotone-hipstamagic/'),
]"""

"""Dynamic Range: DR-Auto
Highlight: -2 (Low)
Shadow: -2 (Low)

Color: +1 (Medium-High)
Sharpness: -2 (Low)

Noise Reduction: -2 (Low)
White Balance: Daylight, +3 Red & -4 Blue
ISO: Auto, up to ISO 3200

Grain Effect: Strong, Small

Color Chrome Effect: Strong
Color Chrome Effect Blue: Weak
White Balance: 5200K, +1 Red & -6 Blue"""

class Units:
    # unit / final_values
    
    brightness = 1/5
    contrast = 0.2
    blur = 0.9
    sharpness = 0.15 

    color = 0.25

    grain = 0.02 

class Presets:
    """Collection of configurations for filters
    """
    leaks = {
        "classic":{"r_max":1000, "intensity":200, 
                    "density":50, "offset":(100,50),
                    "transparency":250, "uselines": False},
        "rollers1":{"r_max":700, "intensity":50, 
                    "density":20, "uselines": True},
        "rollers2":{"r_max":150, "intensity":500, 
                    "density":10, "uselines": True},
        "linear1":{"r_max":150, "intensity":50, 
                    "density":60, "uselines": True},
        "linear2":{"r_max":100, "intensity":250, 
                    "density":40, "uselines": True}                 
    }
    vignettes = {
        "rect_strong":{"sizep":0.02, "transparency":0, 
                      "brightness":220, "density":60, "frame":'rect'},
        "rect_pale":{"sizep":0.01, "transparency":0, 
                     "brightness":220, "density":60, "frame":'rect'},
        "round":{"sizep":0.05, "transparency":120,
                 "brightness":250, "density":5, "frame":"round"}          
    }
    tints = {
        "brown":(0.1, -0.01, -0.1),
        "red":(0.1, -0.05, -0.1),
        "blue":(-0.1, -0.05, 0.035)
    }

class Recipe:
    """Defines configuration set for filters

    color: enhances color
    brightness: change brightness
    contrast: change contrast
    sharpness: ??,
    grain: , leaks,
    tint, vignette
    """
    def __init__(self, name: str,
                 brightness=0, contrast=0, blur=0,
                 sharpness=0, color=0, grain=0,
                 tint=Presets.tints["brown"],
                 leaks=Presets.leaks["classic"],
                 vignette=Presets.vignettes["rect_pale"]
                 ):
        
        self.name = name

        self.check(brightness, (-3, 4))
        self.brightness = brightness*Units.brightness

        self.check(contrast, (-3, 6))
        self.contrast = contrast*Units.contrast

        self.check(blur, (0, 5))
        self.blur = blur*Units.blur

        self.check(sharpness, (-5, 7))
        self.sharpness = sharpness*Units.sharpness
        
        self.check(color, (-4, 10))
        self.color = color*Units.color

        self.check(grain, (0, 10))
        self.grain = grain*Units.grain

        self.tint = tint
        self.leaks = leaks
        self.vignette = vignette

    def check(self, value, x=(-5, 5)):
        if not (x[0] <= value <= x[1]):
            raise ValueError(f"This value ({value}) should be in range:", x)

recipes_collection = {
    'CLSC':Recipe(name='CLSC', 
                  brightness=1, contrast=3, blur=1,
                  sharpness=1, color=1, grain=1)
}
    

