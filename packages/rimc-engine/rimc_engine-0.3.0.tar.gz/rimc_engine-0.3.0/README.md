# RIMC (Retro Image Converter) Engine for Python

This module will allow you to convert any photo of your choice to the filtered image in a retro / vintage style!

<table>
  <tr>
    <th>Original</th>
    <th>Edited</th>
  </tr>
  <tr>
    <td><img src="gallery/ex1.JPG" width="500"></td>
    <td><img src="gallery/ex1_edit.JPG" width="500"></td>
  </tr>
  <tr>
    <td><img src="gallery/ex2.jpg" width="500"></td>
    <td><img src="gallery/ex2_edit.jpg" width="500"></td>
  </tr>
</table>

You are allowed to visit [gallery](/gallery) for more examples.

## Usage

### convert_image.py

This is the script file, in which there is a finction to take an image name and produce a vintage photo out of it

### main.py

This is an example of simple usage of the script



## ideas

recipes
predefined collection / film

Processing / Developing

## Notes

Cropping
```python
img2 = Image.open(path+name)
k = 0.5
# img2.resize((int(img2.size[0]*k), int(img2.size[1]*k)))
mk = min(img2.size)
img2 = ImageOps.fit(img2, (mk, mk), centering=(0.5, 0.7))

img2.show() 

# img_contain = ImageOps.crop(img_contain, 200)
```
