# PennAiR-Software-Challenge-Fall-2024

### How to run code

1. Install a python environment (see [here](https://realpython.com/installing-python/) for more info)
2. Install the cv2 and numpy packages (see [here](https://packaging.python.org/en/latest/tutorials/installing-packages/))
3. Either in terminal or in an IDE, open the python file you downloaded from this repo.
   
If you are trying part 1, run the following
```py
cv2.imshow('img', trace('img_path'))
cv2.waitKey(0)
cv2.destroyAllWindows()
```
where img_path is the path of the shapes on grass image.

If you are trying part 2 or 3, run the following
```py
makeVideo('input_path', 'output_path')
```
where input_path is the path of the video of the moving shapes and output_path is the path where you want the output video to be saved. 



