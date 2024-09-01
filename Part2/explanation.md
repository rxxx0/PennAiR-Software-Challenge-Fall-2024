It took my computer (Apple M2) 25 seconds to process the video.

I had to alter the algorithm from part 1 slightly to get it to work on video. Here are the changes I made:

#### Grayscale

The part 1 algorithm was not working as intended when I applied it to the video but after some experimentation
I found that grayscaling the frame before applying the algorithm helped.

#### Denoising

To help reduce the jarring changes in pixel intensity that happen in the grass and on shape-grass borders, I applied 
a bilateral filter to the grayscaled frame.

The rest of the video algorithm is essentially the same as the part 1 algorithm.
