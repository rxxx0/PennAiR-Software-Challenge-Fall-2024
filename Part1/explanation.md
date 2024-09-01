![PennAir 2024 App Static](https://github.com/user-attachments/assets/1c63627a-806a-4313-b081-f18eb276e794)

My first thought when I saw this image was to directly apply Canny edge detection to see what would happen. It _did_ correctly outline the shapes, but it also outlined every
"dark spot" in the grass.

To get around this, I needed some way to remove (or "close") the small edges detected in the grass. To do this, I dilated the Canny output. 
This dilation effectively removes the small edges by making them bigger and bigger until they collapse and become white space, after which 
we can negate the image to isolate the shapes.

After this, all that remains to do is to use the built-in findContours method, compute the location of the shapes' centers, and then display it as text.
