import tkinter as tk
from tkinter import PhotoImage
from PIL import Image, ImageTk
class TileMapping:
    '''
    build a mapping between tile number and tile character & tile image
    for displaying tiles in GUI and console
    '''
    tile_mapping = {
        1: "🀇", 
        2: "🀈", 
        3: "🀉", 
        4: "🀊", 
        5: "🀋", 
        6: "🀌", 
        7: "🀍", 
        8: "🀎", 
        9: "🀏", 

        21: "🀙", 
        22: "🀚", 
        23: "🀛", 
        24: "🀜", 
        25: "🀝", 
        26: "🀞", 
        27: "🀟", 
        28: "🀠", 
        29: "🀡", 

        41: "🀐", 
        42: "🀑", 
        43: "🀒", 
        44: "🀓", 
        45: "🀔", 
        46: "🀕", 
        47: "🀖", 
        48: "🀗", 
        49: "🀘", 

        63: "🀀", 
        66: "🀁", 
        69: "🀂", 
        72: "🀃", 
        75: "🀄", 
        78: "🀅", 
        81: "🀆", 
        }
    

    tile_mapping_image = {
        1: 'Res/tiles/m1.png',
        2: 'Res/tiles/m2.png',
        3: 'Res/tiles/m3.png',
        4: 'Res/tiles/m4.png',
        5: 'Res/tiles/m5.png',
        6: 'Res/tiles/m6.png',
        7: 'Res/tiles/m7.png',
        8: 'Res/tiles/m8.png',
        9: 'Res/tiles/m9.png',

        21: 'Res/tiles/p1.png',
        22: 'Res/tiles/p2.png',
        23: 'Res/tiles/p3.png',
        24: 'Res/tiles/p4.png',
        25: 'Res/tiles/p5.png',
        26: 'Res/tiles/p6.png',
        27: 'Res/tiles/p7.png',
        28: 'Res/tiles/p8.png',
        29: 'Res/tiles/p9.png',

        41: 'Res/tiles/s1.png',
        42: 'Res/tiles/s2.png',
        43: 'Res/tiles/s3.png',
        44: 'Res/tiles/s4.png',
        45: 'Res/tiles/s5.png',
        46: 'Res/tiles/s6.png',
        47: 'Res/tiles/s7.png',
        48: 'Res/tiles/s8.png',
        49: 'Res/tiles/s9.png',

        63: 'Res/tiles/w1.png',
        66: 'Res/tiles/w2.png',
        69: 'Res/tiles/w3.png',
        72: 'Res/tiles/w4.png',
        75: 'Res/tiles/d1.png',
        78: 'Res/tiles/d2.png',
        81: 'Res/tiles/d3.png',
        }
    reverse_mapping = {v: k for k, v in tile_mapping.items()}

    loaded_images = {}

    @staticmethod
    def load_images():
        for key, path in TileMapping.tile_mapping_image.items():
            TileMapping.loaded_images[key] = PhotoImage(file=path).subsample(2, 2)

def main():
    root = tk.Tk()
    root.geometry("1200x800")
    canvas = tk.Canvas(root, width=1200, height=800)
    canvas.pack()

    TileMapping.load_images()

    label = tk.Label(root, image=TileMapping.loaded_images[1])
    label.image = TileMapping.loaded_images[1]
    canvas.create_window(500, 500, window=label)

    root.mainloop()

if __name__ == "__main__":
    main()