# wato-coding-challenge

## Answer
![answer](https://github.com/adalal04/wato-coding-challenge/blob/7af5f213ee96ad3d98ae56a148fb4ac235abfe3d/answer.png)

### Methodology
I was able to solve this by filtering the image by color and by objects that contained a higher saturation. This helped me to isolate out 
the cones. Then, I was able to use contours to put the coordinates of the cone centers into a list. Then, I split this list into two 
separate lists, one containing cones on the left and one containing cones on the right. Lastly, I used the fitLine method to draw a line 
going through the cones.

### What I tried and why I think it didn't work
I thought that blurring the image may be able to filter the image enough so that the cones can get isolated. However, after multiple 
attempts and trying to figure out the issue, apparently the cones were not being read properly. I saw online that using an HSV image in this 
scenario would be a better approach. Through trial and error I was able to find the best HSV range in order for proper cone detection.
After that I spent some time trying to find the best HSV range so that only the cones would be detected. I displayed the mask image and kept 
playing around with the variables until I found a good match because there was other items in the image getting detected.
I was able to split the big list of cones into two lists, one containing cones on the left and the other containing cones on the right. 
After testing the code, I finally got a valid answer.

### Libraries
The libraries I used are OpenCV and NumPy.
