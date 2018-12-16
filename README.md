# CyberSecurityTool/Stegsolve
Stegsolve allows you to look at different image modifications and sometimes see some encrypted messages in it
____
### On start
![alt text](https://pp.userapi.com/c850636/v850636259/69aa2/H6lAicV6Ja0.jpg)<br />
  On start app will ask you to choose the image(.jpg only) to work with using the default for your OS explorer
### Operations with image
  After you have chosen the image to work with you will see this window(in my case i have chosen the picture of this old man):
  ![alt text](https://pp.userapi.com/c850636/v850636259/69ac8/Hj_LR5NIsEE.jpg)<br />
____
## Lets take a look at the main window, there are 3 main parts:
  ### 1. Image preview:
   ![alt text](https://pp.userapi.com/c850636/v850636259/69acf/8oGCc9gWDSU.jpg)<br />
    Here you will see your image preview, it will change depending on second part choice
  ____
  ### 2. Choice block:
   ![alt text](https://pp.userapi.com/c850636/v850636259/69ae9/wqNn2t0q-rc.jpg)<br />
    This block contains all the image modifications, lets take a look at them:
   #### 2.1 Default image: 
   ![alt text](https://pp.userapi.com/c850636/v850636259/69b32/S3SA48aWRbU.jpg)<br />
    This is the default image you have uploaded to the app
   #### 2.2 Color inversion aka XOR aka Negative:
   ![alt text](https://pp.userapi.com/c850636/v850636259/69b39/2tYLh-D7Mck.jpg)<br />
    This modification turns each pixel of image (r,g,b) into (255-r, 255-g, 255-g)
   #### 2.3 Red plane/Green plane/Blue plane:
   ![alt text](https://pp.userapi.com/c850636/v850636259/69b5b/G5uyYRh-9tA.jpg)<br />
    Red plane turns each pixel from (r, g, b) to (r, 0, 0)<br />
    Green plane turns each pixel from (r, g, b) to (0, g, 0)<br />
    Blue plane turns each pixel from (r, g, b) to (0, 0, b)<br />
   #### 2.4 Full red/Full green/Full blue:
   ![alt text](https://pp.userapi.com/c850636/v850636259/69b67/47-b0pCg69k.jpg)<br />
    Full red turns each pixel from (r, g, b) to (255, g, b)<br />
    Full green turns each pixel from (r, g, b) to (r, 255, b)<br />
    Full blue turns each pixel from (r, g, b) to (r, g, 255)<br />
  ____
  ### 3. Select file button:
   ![alt text](https://pp.userapi.com/c850636/v850636259/69b9e/X_b5khxyItA.jpg)<br />
    If you want to change image to work with but you dont want to rerun the app you can press this button and choose another app
