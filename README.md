# Distracted_Driver_Detection
Primary Goal: To achieve a model which takes image as an input and tell about driver that it is driving properly or distracted with some other activities.

Solution: For creating a model we need a dataset of images of drivers in which they are doing different activities while driving vehicle. After getting the dataset we use the concept of transfer learning which helps us to predict the movements of driver.  


![ezgif com-gif-maker (3)](https://user-images.githubusercontent.com/87935713/216521496-6470c69f-1940-4c84-8200-d55f7376be1e.gif)

This is a small representation of WebApp, Please ignore UI 😅😅.

Dataset : Our dataset comes from kaggle.com in which there was a competition of state farm distracted driver detection in which they provided us around 1 lakh images of driver doing different activities while driving.

Link of Dataset for downloading: https://www.kaggle.com/competitions/state-farm-distracted-driver-detection/data


Our dataset is already splitted into train and test.

![train_test_count](https://user-images.githubusercontent.com/87935713/216608467-a2068ecc-3df2-46ed-b12d-1b7b49f5cbc4.png)


From above graph we observe that our testing data is very large data as compared to training data.

In this dataset the images are divided into 10 categories according to the movements of drivers they are:

c0: normal driving

c1: texting - right

c2: talking on the phone - right

c3: texting - left

c4: talking on the phone - left

c5: operating the radio

c6: drinking

c7: reaching behind

c8: hair and makeup

c9: talking to passenger

When we see our training data folder we have subfolders where each folder contains the images according to there categories.

![train_category_count](https://user-images.githubusercontent.com/87935713/216607888-40768bfe-d8c2-464a-9bbe-7b99dcf3b21a.png)

Process of training our Model:

Before we start to train our model we need to take precautions for one thing which is overfitting. When we visualize the counts of train and test set we found that our test data is 4 times more than train data, it directly tell us that there are more chances that our model will be overfitted on our train data, so we need to take care of this.

Step 1: Whenever we wanted to train our model the first and foremost thing is to prepare input data for our model. So our first step is to prepare input data for our model.

Step 2: While tackling with the images data there is always an recommendation to do Data Augmentation. Data augmentation is done when we have less data to train our model and we need to reduce overfitting of model. Here we have both the cases so here we are performing Image Augmentation with the help ImageDataGenerator class in keras module.

Step 3: Now comes our favourite step, to define the structure of our model and adding layers in our model. While dealing with images we can use an approach of transfer learning. Transfer learning appraoch is so much helpful when we have less number of training data.

Here I am telling brief introduction of transfer learning :

Transfer learning is a technique in deep learning that allows a model to be fine
tuned for a specific task, using knowledge learned from a pre-trained model that
has been trained on a similar or related task. The goal of transfer learning is to
leverage the knowledge learned from the pre-trained model to reduce the amount of
data and computational resources needed to train a new model for the target task.

Here is a blog on transfer learning you may checkout for deep knowledge:
https://machinelearningmastery.com/transfer-learning-for-deep-learning/

Step 4: In this problem we are using pretrained model VGG16 which trained on the ImageNet dataset, which contains over 1 million labeled images from 1000 different classes.

Step 5: Including VGG16 model layers we are also adding our CNN layers and Dense layers for training our model.

Step 6: Finally we start our training of our model by providing training images data to our model.

Step 7: At last, now our model is trained we save the state of our model into model.h5 file for further use.

Note: Here I have used Google Colab for accomplishing this project. So all the paths of files in the code are according to google colab paths. So before running the code please ensure all the paths.

Steps to run the WebApp:

Step 1: First Download whole code and files into your PC.

Step 2: Run requirements.txt file for installing necessary libraries for this WebApp

Step 3: Change the Path in code according to your directory structure.

Step 4: Run the file app.py in your terminal which provide you a link of localhost. Copy that url and paste it in your browser and click enter and see the magic.


