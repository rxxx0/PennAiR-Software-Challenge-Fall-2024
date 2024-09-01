I had to make 3 modifications to the part 2 algorithm to achieve background agnosticism:

#### Strengthen the Denoising
I made the bilateral filtering step stronger to compensate for the increased "noise" due to the shapes not being of uniform color.

#### Adaptive Thresholding
We can't directly apply Canny like we did in part 1 and 2 since the shapes are not of uniform color, so we use adaptive thresholding
to threshold different parts of the frame accordingly.

#### Closing instead of Dilating
In part 2, we used dilation to effectively rid the frame of the small extraneous edges that were detected in the grass. That approach
did not work here, so I tried closing (cv2.MORPH_CLOSE) instead of dilation (cv2.MORPH_DILATE), which did work.
