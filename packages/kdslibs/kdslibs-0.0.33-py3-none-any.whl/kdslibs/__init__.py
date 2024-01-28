# @title Default title text
import urllib.request
import os

datadict={}
link = "data.py"


current_dir = os.path.dirname(os.path.abspath(__file__))
#current_dir = os.getcwd()


def helpenv():
  """
  conda create -n "myenv2" python=3.8.0
  conda activate myenv2
  conda install -c conda-forge tensorflow
  conda install -c anaconda ipykernel
  python -m ipykernel install --user --name=myenv2
  conda install opencv
  conda install -c conda-forge matplotlib
  conda install scikit-learn
  conda install scikit-image
  pip install opendatasets
  conda install pandas
  pip install kaggle
  pip install bs4
  pip install nltk
  pip install wget
  pip install seaborn
  #NER
  pip install spacy
  python -m spacy download en_core_web_sm
  #Word2Vec
  pip install gensim
  pip install wordcloud
  pip install tensorflow-hub
    pip install tensorflow-text
    """

  #General





  def helpImport():
    """
  import cv2
  import numpy as np
  import matplotlib.pyplot as plt
  import pandas
  import pandas as pd
  import numpy as numpy
  import seaborn as sns

  # HOG
  from skimage.feature import hog
  from skimage import exposure

  # Regular expression
  import re
  from bs4 import BeautifulSoup


  # Stop Words, Stemmer
  import nltk
  from nltk.corpus import stopwords
  from nltk.stem import PorterStemmer
  #nltk.download('stopwords')
  #nltk.download('punkt')

  #count Vectorizer and Tf-Idf
  from sklearn.feature_extraction.text import CountVectorizer
  from sklearn.feature_extraction.text import TfidfVectorizer
  from keras.preprocessing.text import Tokenizer
  from tensorflow.keras.preprocessing.sequence import pad_sequences

  ## Neural Networks
  from keras.models import Sequential
  from keras.layers import Embedding, LSTM, Dense
  from keras.utils import to_categorical

  #Model
  from sklearn.naive_bayes import MultinomialNB
  from sklearn.cluster import KMeans

  # Test-Train Split
  from sklearn.model_selection import train_test_split

  #Model Evaluation
  from sklearn.metrics import confusion_matrix
  from sklearn.metrics import accuracy_score
  from sklearn.metrics import classification_report

  #Utils
  from imutils import paths
  """




# Construct the path to the resource file
resource_file_path = os.path.join(current_dir, link)


def setLink(linki):
  global  link
  link=linki


def printLink():
  global  link
  print(link)


def printall():
  print(readData(link))



def printhead(dataSearch):
  printchead(link,dataSearch)


def printchead(link,dataSearch):
  strs=readData(link).split("###ENDOFSEGMENT###")
  for index in range(0,len(strs)):
      segmentData=strs[index].split("##HEADER##")
      if dataSearch in segmentData[0]:
        if len(segmentData)>1:
          #print(segmentData[0])
          #print("\n")
          print(segmentData[1])
        else:
          print(segmentData[0])
          print("No Data")

def readData(linki):
  #print(linki)
  with urllib.request.urlopen(linki) as url:
      s = url.read()
      # I'm guessing this would output the html source code ?
      return s.decode()

def printheader():
  print(printcheader(link))

def printcheader(link):
  strs=readData(link).split("###ENDOFSEGMENT###")
  for index in range(0,len(strs)):
      segmentData=strs[index].split("##HEADER##")
      print(segmentData[0])

def convert_to_alphanumeric(input_string):
    alphanumeric_string = ''.join(char for char in input_string if char.isalnum())
    return alphanumeric_string

def getData():
  global datadict
  file_contents=""
  file_path = resource_file_path  # Replace with the actual file path
  #print(file_path)
  try:
    with open(file_path, 'r') as file:
        file_contents = file.read()
        #print(file_contents)
  except FileNotFoundError:
    print(f"File '{file_path}' not found.")
  except IOError:
    print(f"Error reading file '{file_path}'.")

  strs=file_contents.split("###ENDOFSEGMENT###")
  for index in range(0,len(strs)):
      segmentData=strs[index].split("##HEADER##")
      if len(segmentData)==2:
        datadict[convert_to_alphanumeric(segmentData[0])] = segmentData[1]

getData()

def getKeys():
  return datadict.keys()

def println(key):
  print(datadict[key])


def displayImagesFromPath(imagePath=[],gstr=[]):
  """
  finalImages=[]
  for eachPath in imagePath:
    images=[]
    original,grayImage=readImage(eachPath)
    images.append(original)
    images.append(grayImage)
    finalImages.append(images)
  displayImages(finalImages,gstr)

  """
  finalImages=[]
  for eachPath in imagePath:
    images=[]
    original,grayImage=readImage(eachPath)
    images.append(original)
    images.append(grayImage)
    finalImages.append(images)
  displayImages(finalImages,gstr)


#User Defined Function to Display Images
def displayImages(images=[],gstr=[], fsize=(16, 16)):
  """
    newStr=[]
  if len(gstr) ==0:
    for eachImageIndex in range(len(gstr),len(images)):
      print(newStr)
      newStr.append("Image_"+ str(eachImageIndex) )
  else:
    newStr=gstr
  if (len(images)==0) or len(images) !=len(newStr):
    print("No images passed or argument length does not match")
    return
  else:
    # Create a 4x4 subplot grid
    print(len(images[0]),len(images))
    noOfRows=len(images[0])
    #print(images[2].shape)
    noOfColumns =len(images)
    fig, axes = plt.subplots(noOfRows, noOfColumns, figsize=fsize)

    counter=0
    # Fill the subplots with content (sample data in this case)
    for i in range(noOfColumns):
      for j in range(noOfRows):
        ax = axes[j, i]
        img=images[i][j]
        if len(img.shape)==3:
          img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
          ax.imshow(img)
        else:
          ax.imshow(img,"gray")
        if j==0:
          ax.set_title(newStr[i])

    # Adjust spacing between subplots
    #plt.tight_layout()

    # Show the plot
    plt.show()
  """
  newStr=[]
  if len(gstr) ==0:
    for eachImageIndex in range(len(gstr),len(images)):
      print(newStr)
      newStr.append("Image_"+ str(eachImageIndex) )
  else:
    newStr=gstr
  if (len(images)==0) or len(images) !=len(newStr):
    print("No images passed or argument length does not match")
    return
  else:
    # Create a 4x4 subplot grid
    print(len(images[0]),len(images))
    noOfRows=len(images[0])
    #print(images[2].shape)
    noOfColumns =len(images)
    fig, axes = plt.subplots(noOfRows, noOfColumns, figsize=fsize)

    counter=0
    #Fill the subplots with content (sample data in this case)
    for i in range(noOfColumns):
      for j in range(noOfRows):
        ax = axes[j, i]
        img=images[i][j]
        if len(img.shape)==3:
          img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
          ax.imshow(img)
        else:
          ax.imshow(img,"gray")
        if j==0:
          ax.set_title(newStr[i])

    # Adjust spacing between subplots
    #plt.tight_layout()

    # Show the plot
    plt.show()

#User Defined Function to Read Images
def readImage(ipImagePath):
  """
  Input :
    ipImagePath : The path of an image to read
  return
     cv2.imread(ipImagePath),cv2.imread(ipImagePath,cv2.IMREAD_GRAYSCALE)
     The orginal Image and Grayscale Image
  """
  return cv2.imread(ipImagePath),cv2.imread(ipImagePath,cv2.IMREAD_GRAYSCALE)


def readImagesFromPath(base_path):
  """
  def readImagesFromPath(base_path):
  from imutils import paths
  X_train=[]
  X_test=[]
  y_train=[]
  y_test=[]
  images=paths.list_images(base_path)
  for eachImage in images:
    trainOrtest=eachImage.split("/")[-3]
    WolfOrDog=eachImage.split("/")[-2]
    #print(trainOrtest, WolfOrDog, eachImage)
    img=cv2.imread(eachImage,cv2.IMREAD_GRAYSCALE)
    img=cv2.resize(img, (224, 224))
    if (trainOrtest=="Train"):
      X_train.append(img)
      if (WolfOrDog=="wolves"):
        y_train.append(0)
      else: #Dog
        y_train.append(1)
    else:
      X_test.append(img)
      if (WolfOrDog=="wolves"):
        y_test.append(0)
      else: #Dog
        y_test.append(1)
  return X_train,X_test,y_train,y_test
  """
  from imutils import paths
  X_train=[]
  X_test=[]
  y_train=[]
  y_test=[]
  images=paths.list_images(base_path)
  for eachImage in images:
    trainOrtest=eachImage.split("/")[-3]
    WolfOrDog=eachImage.split("/")[-2]
    #print(trainOrtest, WolfOrDog, eachImage)
    img=cv2.imread(eachImage,cv2.IMREAD_GRAYSCALE)
    img=cv2.resize(img, (224, 224))
    if (trainOrtest=="Train"):
      X_train.append(img)
      if (WolfOrDog=="wolves"):
        y_train.append(0)
      else: #Dog
        y_train.append(1)
    else:
      X_test.append(img)
      if (WolfOrDog=="wolves"):
        y_test.append(0)
      else: #Dog
        y_test.append(1)
  return X_train,X_test,y_train,y_test


#User Defined Function to Sobel Edge Detection
def edge_applySobel(ipImage):
  """
  def applySobel(ipImage):
  sobel_image_x = cv2.Sobel(ipImage, cv2.CV_64F, 1, 0, ksize=5)
  sobel_image_y = cv2.Sobel(ipImage, cv2.CV_64F, 0, 1, ksize=5)
  sobel_magnitude_image = cv2.magnitude(sobel_image_x, sobel_image_y)
  return sobel_magnitude_image

  #Method 2
  # Apply Sobel operator to get gradients in the x and y directions
  sobel_x = cv2.Sobel(grayimage, cv2.CV_64F, 1, 0, ksize=3)
  sobel_y = cv2.Sobel(grayimage, cv2.CV_64F, 0, 1, ksize=3)

  # Convert the gradients back to uint8 format
  sobel_x = cv2.convertScaleAbs(sobel_x)
  sobel_y = cv2.convertScaleAbs(sobel_y)

  # Combine the gradients using the magnitude formula
  gradient_magnitude = cv2.addWeighted(sobel_x, 0.5, sobel_y, 0.5, 1)


  """
  sobel_image_x = cv2.Sobel(ipImage, cv2.CV_64F, 1, 0, ksize=5)
  sobel_image_y = cv2.Sobel(ipImage, cv2.CV_64F, 0, 1, ksize=5)
  sobel_magnitude_image = cv2.magnitude(sobel_image_x, sobel_image_y)
  return sobel_magnitude_image


#User Defined Function to resize Images
def resizeImage(ipImage, height=224,width=224):
  """
  def resizeImage(ipImage, height=new_height,width=new_width):
  return cv2.resize(ipImage, (height, width))
  """
  return cv2.resize(ipImage, (height, width))

#User Defined Function to Canny Edge Detection
def edge_applyCanny(ipImage,th_lower=100, th_upper=200):
  """
  def applyCanny(ipImage,th_lower=100, th_upper=200):
  return cv2.Canny(ipImage, th_lower, th_upper)
  """
  return cv2.Canny(ipImage, th_lower, th_upper)


def seg_regionsplitMerge():
  """
  import cv2
  import numpy as np

  # Load the input image
  image = cv2.imread('/content/Landscape-Color.jpg')  # Replace 'house.png' with your image path
  # Convert the image to grayscale
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  # Create an output image to display segmented regionsac
  segmented_image = np.zeros_like(image)
  # Define a threshold for region splitting
  split_threshold = 128
  # Define a threshold for region merging
  merge_threshold = 64


  # Function for region splitting
  def region_split(image, x1, y1, x2, y2):
      region = image[y1:y2, x1:x2]

      if (x2 - x1) > 1:
          mean_intensity = np.mean(region)

          if not np.isnan(mean_intensity) and mean_intensity > split_threshold:
              mid_x = (x1 + x2) // 2
              mid_y = (y1 + y2) // 2
              region_split(image, x1, y1, mid_x, mid_y)
              region_split(image, mid_x, y1, x2, mid_y)
              region_split(image, x1, mid_y, mid_x, y2)
              region_split(image, mid_x, mid_y, x2, y2)
          else:
              merge_regions(x1, y1, x2, y2)
      else:
          merge_regions(x1, y1, x2, y2)

  # Function for region merging
  def merge_regions(x1, y1, x2, y2):
      region = gray[y1:y2, x1:x2]
      region_size = (x2 - x1) * (y2 - y1)

      if region_size > 0:
          mean_intensity = np.mean(region)

          if not np.isnan(mean_intensity) and mean_intensity < merge_threshold:
              mid_x = (x1 + x2) // 2
              mid_y = (y1 + y2) // 2

              merge_regions(x1, y1, mid_x, mid_y)
              merge_regions(mid_x, y1, x2, mid_y)
              merge_regions(x1, mid_y, mid_x, y2)
              merge_regions(mid_x, mid_y, x2, y2)
          else:
              # Fill the region with mean intensity value in the segmented image
              segmented_image[y1:y2, x1:x2] = [mean_intensity, mean_intensity, mean_intensity]

  # Perform region splitting
  region_split(gray, 0, 0, gray.shape[1], gray.shape[0])

  # Save the segmented image as a temporary file
  cv2.imwrite('segmented_image.png', segmented_image)

  # Display the segmented image using IPython.display
  Image(filename='segmented_image.png')
  """
  print("Not Implemented")

def seg_threshold_otsu():
  """
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
  _, thresh = cv2.threshold(gray, 0, 25, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
  contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  foreground_mask = np.zeros_like(image)
  cv2.drawContours(foreground_mask, contours, -1, (255, 255, 255), thickness=-1)
  foreground = cv2.bitwise_and(image, foreground_mask)

  """
  print("Not Implemented")


def seg_countours_canny():
  """
  canny=cv2.Canny(gray,150,200)
  countours,hierarchy=cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
  cv2.drawContours(gray, contours, -1, (255, 255, 255), thickness=-1)
   # Draw contours on a blank image
    contour_image = np.zeros_like(image)
    cv2.drawContours(contour_image, contours, -1, (0, 255, 0), 2)
  """

## WATERSHED SEGMENTATION
def seg_watershedSegmentation(ipImage,th_lower=100, th_upper=200):
  """
    image=ipImage.copy()
  # Convert the image to gray scale
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Apply thresholding
  ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

  # Noise removal using morphological operations
  kernel = np.ones((3, 3), np.uint8)
  opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

  # Sure background area
  sure_bg = cv2.dilate(opening, kernel, iterations=3)

  # Finding sure foreground area
  dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
  ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

  # Finding unknown region
  sure_fg = np.uint8(sure_fg)
  unknown = cv2.subtract(sure_bg, sure_fg)

  # Marker labelling
  ret, markers = cv2.connectedComponents(sure_fg)
  markers = markers + 1
  markers[unknown == 255] = 0

  # Apply watershed algorithm
  #markers = cv2.watershed(image, markers)
  #image[markers == -1] = [255, 255, 255]  # Color the boundaries in red

  # Apply watershed algorithm
  markers = cv2.watershed(image, markers)

  # Get unique segment labels
  unique_labels = np.unique(markers)

  # Assign a random color to each segment
  colors = np.random.randint(0, 255, size=(len(unique_labels), 3))

  # Color each segment in the original image
  for label, color in zip(unique_labels, colors):
      image[markers == label] = color
  """
  image=ipImage.copy()
  # Convert the image to gray scale
  gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Apply thresholding
  ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

  # Noise removal using morphological operations
  kernel = np.ones((3, 3), np.uint8)
  opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

  # Sure background area
  sure_bg = cv2.dilate(opening, kernel, iterations=3)

  # Finding sure foreground area
  dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
  ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)

  # Finding unknown region
  sure_fg = np.uint8(sure_fg)
  unknown = cv2.subtract(sure_bg, sure_fg)

  # Marker labelling
  ret, markers = cv2.connectedComponents(sure_fg)
  markers = markers + 1
  markers[unknown == 255] = 0

  # Apply watershed algorithm
  #markers = cv2.watershed(image, markers)
  #image[markers == -1] = [255, 255, 255]  # Color the boundaries in red

  # Apply watershed algorithm
  markers = cv2.watershed(image, markers)

  # Get unique segment labels
  unique_labels = np.unique(markers)

  # Assign a random color to each segment
  colors = np.random.randint(0, 255, size=(len(unique_labels), 3))

  # Color each segment in the original image
  for label, color in zip(unique_labels, colors):
      image[markers == label] = color
  return image



## REGION GROWNING
def seg_regionGrowing2(grayImage, threshold=50, seed_x_ratio=0.5, seed_y_ratio=0.5):
    """
    ## REGION GROWNING
def seg_regionGrowing2(grayImage, threshold=50, seed_x_ratio=0.5, seed_y_ratio=0.5):
    # Get the dimensions of the input grayscale image
    height, width = grayImage.shape

    # Calculate seed coordinates based on the ratios
    seed_x = int(height * seed_x_ratio)
    seed_y = int(width * seed_y_ratio)

    # Initialize a binary mask for the segmented region
    output_mask = np.zeros_like(grayImage, dtype=np.uint8)

    # Create a stack to keep track of pixels to be processed
    stack = [(seed_x, seed_y)]

    # Region growing process
    while stack:
        # Pop a pixel from the stack
        x, y = stack.pop()

        # Check if the pixel is within image bounds and has not been processed
        if 0 <= x < height and 0 <= y < width and output_mask[x, y] != 255:
            # Check intensity similarity with the seed pixel
            if abs(int(grayImage[x, y]) - int(grayImage[seed_x, seed_y])) <= threshold:
                # Add the pixel to the segmented region
                output_mask[x, y] = 255

                # Add neighboring pixels to the stack for further processing
                stack.extend([(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)])

    # Return the binary mask representing the segmented region
    return output_mask
    """
    # Get the dimensions of the input grayscale image
    height, width = grayImage.shape

    # Calculate seed coordinates based on the ratios
    seed_x = int(height * seed_x_ratio)
    seed_y = int(width * seed_y_ratio)

    # Initialize a binary mask for the segmented region
    output_mask = np.zeros_like(grayImage, dtype=np.uint8)

    # Create a stack to keep track of pixels to be processed
    stack = [(seed_x, seed_y)]

    # Region growing process
    while stack:
        # Pop a pixel from the stack
        x, y = stack.pop()

        # Check if the pixel is within image bounds and has not been processed
        if 0 <= x < height and 0 <= y < width and output_mask[x, y] != 255:
            # Check intensity similarity with the seed pixel
            if abs(int(grayImage[x, y]) - int(grayImage[seed_x, seed_y])) <= threshold:
                # Add the pixel to the segmented region
                output_mask[x, y] = 255

                # Add neighboring pixels to the stack for further processing
                stack.extend([(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)])

    # Return the binary mask representing the segmented region
    return output_mask


## K MEAN SEGMENTATION
def seg_kmeansSegment(grayImage,num_clusters=3):
  """
  ## K MEAN SEGMENTATION
def kmeansSegment(grayImage,num_clusters=3):
  # Reshape the image into a 2D array of pixels
  pixels = grayImage.reshape((-1, 1))  # Convert to 2D array of (B, G, R) values.
  print(pixels.shape)
  # Reshape the pixel array back to the original image shape
  reshaped_image = pixels.reshape(grayImage.shape)

  # Apply K-Means clustering
  kmeans = KMeans(n_clusters=num_clusters)
  kmeans.fit(pixels)
  labels = kmeans.labels_
  # Create an array of the same shape as the reshaped image to store the segmented result
  segmented_image = np.zeros_like(pixels)

  # Assign each pixel to its corresponding cluster center color
  for cluster_id in range(num_clusters):
    # Use boolean indexing to select pixels belonging to the current cluster
            segmented_image[labels == cluster_id] = kmeans.cluster_centers_[cluster_id]

  # Reshape the segmented image to match the original image shape
  segmented_image = segmented_image.reshape(grayImage.shape)

  # Assign a intensity color to each cluster
  cluster_colors = [0,127,255]

  # Convert the segmented image back to the original image data type
  segmented_image = segmented_image.astype(np.uint8)
  return segmented_image
  """
  # Reshape the image into a 2D array of pixels
  pixels = grayImage.reshape((-1, 1))  # Convert to 2D array of (B, G, R) values.
  print(pixels.shape)
  # Reshape the pixel array back to the original image shape
  reshaped_image = pixels.reshape(grayImage.shape)

  # Apply K-Means clustering
  kmeans = KMeans(n_clusters=num_clusters)
  kmeans.fit(pixels)
  labels = kmeans.labels_
  # Create an array of the same shape as the reshaped image to store the segmented result
  segmented_image = np.zeros_like(pixels)

  # Assign each pixel to its corresponding cluster center color
  for cluster_id in range(num_clusters):
    # Use boolean indexing to select pixels belonging to the current cluster
    segmented_image[labels == cluster_id] = kmeans.cluster_centers_[cluster_id]

  # Reshape the segmented image to match the original image shape
  segmented_image = segmented_image.reshape(grayImage.shape)

  # Assign a intensity color to each cluster
  cluster_colors = [0,127,255]

  # Convert the segmented image back to the original image data type
  segmented_image = segmented_image.astype(np.uint8)
  return segmented_image






def test_train_split(X,y,  test_size = 0.20):
  """
  def test_train_split(X,y,  test_size = 0.20):
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
  return X_train, X_test, y_train, y_test

  # train dataframe
  train_df, dummy_df = train_test_split(df,  train_size= 0.7, shuffle= True, random_state= 123)

  # valid and test dataframe
  valid_df, test_df = train_test_split(dummy_df,  train_size= 0.5, shuffle= True, random_state= 123)


  """
  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state = 0)
  return X_train, X_test, y_train, y_test








## FEATURE EXTRACTION

def extract_color_histograms_feature_extraction(image_path):
  """
  def extract_color_histograms_feature_extraction(image_path):
      # Read the input image
      image = cv2.imread(image_path)

      # Convert the image to HSV color space
      hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

      # Compute color histograms for each channel
      hist_hue = cv2.calcHist([hsv_image], [0], None, [256], [0, 256])
      hist_saturation = cv2.calcHist([hsv_image], [1], None, [256], [0, 256])
      hist_value = cv2.calcHist([hsv_image], [2], None, [256], [0, 256])

      # Concatenate the histograms
      hist_features = np.concatenate((hist_hue, hist_saturation, hist_value), axis=None)

      # Display the original image and the color histogram
      cv2.imshow('Original Image', image)
      plt.figure()
      plt.title("Color Histogram")
      plt.xlabel("Bins")
      plt.ylabel("# of Pixels")
      plt.plot(hist_features)
      plt.xlim([0, 768])
      plt.show()
  """
  print("Not Implemented")

def extract_contourbased(origImage,grayimage):
  """
  def contourbased(origImage,grayimage):
  # Apply a threshold to create a binary image
  _, binary_image = cv2.threshold(grayimage, 200, 255, cv2.THRESH_BINARY)
  # Find contours in the binary image
  contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  # Iterate through the contours
  for contour in contours:
      # Calculate contour-based features
      area = cv2.contourArea(contour)
      perimeter = cv2.arcLength(contour, True)
  # Check if area is zero to avoid division by zero
  if area == 0:
          compactness = 0
  else:
          compactness = (perimeter ** 2) / (4 * np.pi * area)
  # Draw the contours on the original image (optional)
  contour_image = cv2.drawContours(origImage.copy(), contours, -1, (0, 255, 0), 2)
  contour_image2 = cv2.drawContours(np.zeros_like(origImage), contours, -1, (255, 255, 255), 3)
  return contour_image,contour_image2

  """
  # Apply a threshold to create a binary image
  _, binary_image = cv2.threshold(grayimage, 200, 255, cv2.THRESH_BINARY)
  # Find contours in the binary image
  contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  # Iterate through the contours
  for contour in contours:
      # Calculate contour-based features
      area = cv2.contourArea(contour)
      perimeter = cv2.arcLength(contour, True)
  # Check if area is zero to avoid division by zero
  if area == 0:
          compactness = 0
  else:
          compactness = (perimeter ** 2) / (4 * np.pi * area)
  # Draw the contours on the original image (optional)
  contour_image = cv2.drawContours(origImage.copy(), contours, -1, (0, 255, 0), 2)
  contour_image2 = cv2.drawContours(np.zeros_like(origImage), contours, -1, (255, 255, 255), 3)
  return contour_image,contour_image2



#rom skimage import data, color
def extract_HOG(grayimage):
  """
  from skimage.feature import hog
  from skimage import exposure
  import matplotlib.pyplot as plt
  def HOG(grayimage):
      # Calculate HOG features
      fd, hog_image = hog(grayimage, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualize=True)
      # HOG rescaled images
      hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))
      return hog_image_rescaled

  #fd, hog_image = hog(resized_img, orientations=9, pixels_per_cell=(8, 8),
                	cells_per_block=(2, 2), visualize=True, multichannel=True)
  """
  # Calculate HOG features
  fd, hog_image = hog(grayimage, orientations=8, pixels_per_cell=(16, 16), cells_per_block=(1, 1), visualize=True)
  # HOG rescaled images
  hog_image_rescaled = exposure.rescale_intensity(hog_image, in_range=(0, 10))
  return hog_image_rescaled


def extract_harrisConrner():
  """
  img = cv.imread(filename)
  gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
  gray = np.float32(gray)
  # cv. CornerHarris (gray image, 3by3 neighbourhood,3by3sobel kernel, ‘k’parameter as explained in example problem)
  dst = cv.cornerHarris(gray,3,3,0.04)

  dst = cv.cornerHarris(gray,3,3,0.04)
  #result is dilated for marking the corners, not important
  # Dilation is applied to enhance the appearance of detected corners, None is used). By default, this will use a 3x3 rectangular kernel for dilation.
  dst = cv.dilate(dst,None)
  # Threshold for an optimal value, it may vary depending on the image.
  img[dst>0.01*dst.max()]=[0,0,255]
  # 0.01 * dst.max() calculates 1% of the maximum corner response value. This is used as a threshold for determining which corners to consider as significant. Corners with a response value greater than this threshold are considered as corners of interest.


  """
  print("Not Implemented")

def extract_sift():
  """
  sift=cv2.SIFT_create()
  image1=cv2.imread(img1, cv2.IMREAD_GRAYSCALE)
  image2=cv2.imread(img2, cv2.IMREAD_GRAYSCALE)
  keypoint1 = sift.detect(image1,None)
  keypoint2 = sift.detect(image2,None)
  img1_with_keypoints=cv2.drawKeypoints(image1,keypoint1,None)
  img2_with_keypoints=cv2.drawKeypoints(image2,keypoint2,None)
  keypoint1,descriptor1 = sift.detectAndCompute(image1,None)
  keypoint2,descriptor2 = sift.detectAndCompute(image2,None)
  bf=cv2.BFMatcher()
  matches=bf.knnMatch(descriptor1, descriptor2, k=2)

  good_matches=[]
  for m,n in matches:
    if m.distance<0.5*n.distance:
      good_matches.append(m)

  matching_result=cv2.drawMatches(image1, keypoint1, image2, keypoint2, good_matches,outImg=None,flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

  plt.imshow(matching_result), plt.title("Image1 with Keypoints"), plt.axis('off')
  """


# IMAGE ENHANCEMENT

# User Defined Function for Contract Stretching
def enhance_contrast_stretching(ipImage):
    """
    def contrast_stretching(ipImage):

    r_min_intensity=0
    r_max_intensity=255
    g_min_intensity=0
    g_max_intensity=255
    b_min_intensity=0
    b_max_intensity=255

    b, g, r = cv2.split(ipImage)

    #b-channel
    b_stretched_image = ((b - np.max(b)) / (np.max(b) - np.min(b))) * (b_max_intensity - b_min_intensity) + b_min_intensity

    #g-channel
    g_stretched_image = ((g - np.max(g)) / (np.max(g) - np.min(g))) * (g_max_intensity - g_min_intensity) + g_min_intensity

    #r-channel
    r_stretched_image = ((r - np.max(r)) / (np.max(r) - np.min(r))) * (r_max_intensity - r_min_intensity) + r_min_intensity

    stretched_image = cv2.merge((b_stretched_image, g_stretched_image, r_stretched_image))
    stretched_image = np.uint8(stretched_image)
    return stretched_image
    """

    r_min_intensity=0
    r_max_intensity=255
    g_min_intensity=0
    g_max_intensity=255
    b_min_intensity=0
    b_max_intensity=255

    b, g, r = cv2.split(ipImage)

    #b-channel
    b_stretched_image = ((b - np.max(b)) / (np.max(b) - np.min(b))) * (b_max_intensity - b_min_intensity) + b_min_intensity

    #g-channel
    g_stretched_image = ((g - np.max(g)) / (np.max(g) - np.min(g))) * (g_max_intensity - g_min_intensity) + g_min_intensity

    #r-channel
    r_stretched_image = ((r - np.max(r)) / (np.max(r) - np.min(r))) * (r_max_intensity - r_min_intensity) + r_min_intensity

    stretched_image = cv2.merge((b_stretched_image, g_stretched_image, r_stretched_image))
    stretched_image = np.uint8(stretched_image)
    return stretched_image


# User Defined Function for Histogram Equalization
def enhance_histogram_equalization(ipImage):
    """
    def histogram_equalization(ipImage):
    b, g, r = cv2.split(ipImage)
    b_equalized = cv2.equalizeHist(b)
    g_equalized = cv2.equalizeHist(g)
    r_equalized = cv2.equalizeHist(r)
    enhanced_image = cv2.merge((b_equalized, g_equalized, r_equalized))
    return enhanced_image
    """
    b, g, r = cv2.split(ipImage)
    b_equalized = cv2.equalizeHist(b)
    g_equalized = cv2.equalizeHist(g)
    r_equalized = cv2.equalizeHist(r)
    enhanced_image = cv2.merge((b_equalized, g_equalized, r_equalized))
    return enhanced_image

# User Defined Function for Histogram Equalization
def enhance_clahe(ipImage):
    """
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    clahe_img = clahe.apply((img*255).astype(np.uint8))
    plt.figure(figsize=(10,7))
    plt.imshow(clahe_img, cmap="gray");
    """
    print("Not Implemented")

# User Defined Function for Intensity Level Slicing
def enhance_intensityLevelSlicing(ipImage):
  """
    lower_bound = 180
  upper_bound = 255
  grayImage=cv2.cvtColor(ipImage, cv2.COLOR_BGR2GRAY)
  mask = np.zeros_like(ipImage)
  mask[(grayImage >= lower_bound) & (grayImage <= upper_bound)] = 255

  sliced_image = cv2.bitwise_and(ipImage, mask)
  return sliced_image
  """
  lower_bound = 180
  upper_bound = 255
  grayImage=cv2.cvtColor(ipImage, cv2.COLOR_BGR2GRAY)
  mask = np.zeros_like(ipImage)
  mask[(grayImage >= lower_bound) & (grayImage <= upper_bound)] = 255

  sliced_image = cv2.bitwise_and(ipImage, mask)
  return sliced_image

# User Defined Function for Gamma Correcton
def enhance_gamma_correction(image, gamma=1.5):
    """
    def gamma_correction(image, gamma=1.5):
    look_up_table = np.array([((i / 255.0) ** gamma) * 255 for i in np.arange(0, 256)]).astype('uint8')
    return cv2.LUT(image, look_up_table)
    """
    look_up_table = np.array([((i / 255.0) ** gamma) * 255 for i in np.arange(0, 256)]).astype('uint8')
    return cv2.LUT(image, look_up_table)


def nlp_pos():
  """
  import nltk
from nltk import word_tokenize
nltk.download('averaged_perceptron_tagger')
sentence = word_tokenize("applicant is removed from applicant list of the job ")
nltk.pos_tag(sentence)
  """
  print("Not Implemented")


def nlp_clean_text(input_string):
    """
    def clean_text(input_string):
      # Step 1: Remove HTML tags using BeautifulSoup
      soup = BeautifulSoup(input_string, "html.parser")
      cleaned_text = soup.get_text()

      # Step 2: Remove special characters using regex
      cleaned_text = re.sub(r"[^a-zA-Z\s]", "", cleaned_text)

      # Optionally, remove extra whitespaces
      cleaned_text = " ".join(cleaned_text.split())
      #cleaned_text = cleaned_text.replace(" .","")

      cleaned_text=cleaned_text.lower()


      return cleaned_text
    """
    # Step 1: Remove HTML tags using BeautifulSoup
    soup = BeautifulSoup(input_string, "html.parser")
    cleaned_text = soup.get_text()

    # Step 2: Remove special characters using regex
    cleaned_text = re.sub(r"[^a-zA-Z\s]", "", cleaned_text)

    # Optionally, remove extra whitespaces
    cleaned_text = " ".join(cleaned_text.split())
    #cleaned_text = cleaned_text.replace(" .","")

    cleaned_text=cleaned_text.lower()


    return cleaned_text

def nlp_remove_stopwords(input_text):
    """
    from nltk.corpus import stopwords
    from nltk.stem import PorterStemmer
    #nltk.download('stopwords')
    def nlp_remove_stopwords(input_text):
    # Tokenize the input text into words
    words = nltk.word_tokenize(input_text)

    # Get the list of English stop words
    stop_words = set(stopwords.words("english"))

    # Remove stop words from the list of words
    filtered_words = [word for word in words if word not in stop_words]

    # Join the filtered words back into a string
    cleaned_text = " ".join(filtered_words)

    return cleaned_text
    """
    # Tokenize the input text into words
    words = nltk.word_tokenize(input_text)

    # Get the list of English stop words
    stop_words = set(stopwords.words("english"))

    # Remove stop words from the list of words
    filtered_words = [word for word in words if word not in stop_words]

    # Join the filtered words back into a string
    cleaned_text = " ".join(filtered_words)

    return cleaned_text

def nlp_stem_onehotTokenize():
	"""
	### Dataset Preprocessing
	# messages is DF here
	# title is one of the column
	import nltk
	import re
	from nltk.corpus import stopwords
	from nltk.stem.porter import PorterStemmer
  from keras.preprocessing.text import one_hot
	nltk.download('stopwords')
	ps = PorterStemmer()
	voc_size=5000
	corpus = []
	for i in range(0, len(messages)):
		print(i)
		review = re.sub('[^a-zA-Z]', ' ', messages['title'][i])
		review = review.lower()
		review = review.split()

		review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
		review = ' '.join(review)
		corpus.append(review)
	onehot_repr=[one_hot(words,voc_size) for words in corpus]
	onehot_repr
	"""
	print("Not Implemented")


def nlp_apply_lemmu(input_text):
  """
  from nltk.stem.wordnet import WordNetLemmatizer
  lemma=WordNetLemmatizer()
  nltk.download('wordnet')
  lemma.lemmatize("word")

  import spacy
  nlp = spacy.load('en_core_web_sm')
  doc = nlp(u'this product integrates designing and painting the colors')
  for token in doc:
    print (token.text, token.lemma_)
  """
  print("Not Implemented")




def nlp_apply_stemming(input_text):
    """
    def nlp_apply_stemming(input_text):
    # Initialize the Porter stemmer
    stemmer = PorterStemmer()

    # Tokenize the input text into words
    words = nltk.word_tokenize(input_text)

    # Apply stemming to each word
    stemmed_words = [stemmer.stem(word) for word in words]

    # Join the stemmed words back into a string
    stemmed_text = " ".join(stemmed_words)

    return stemmed_text
    """
    # Initialize the Porter stemmer
    stemmer = PorterStemmer()

    # Tokenize the input text into words
    words = nltk.word_tokenize(input_text)

    # Apply stemming to each word
    stemmed_words = [stemmer.stem(word) for word in words]

    # Join the stemmed words back into a string
    stemmed_text = " ".join(stemmed_words)

    return stemmed_text

def nlp_NamedEntityRegconinzation():
  """
  pip install spacy -q
import spacy

# in conda prompt
#!python -m spacy download en_core_web_lg
#!python -m spacy download en_core_web_sm

nlp= spacy.load("en_core_web_sm") ## English core Web Document
nlp.pipe_names

doc=nlp("The Chinese Foreign Ministry spokesperson..")

for ent in doc.ents:
  print(ent.text, "|", ent.label_ ,"|",spacy.explain(ent.label_))

from spacy import displacy
displacy.render(doc,style="ent",jupyter=True)
"""
  print("Not Implemented")

def nlp_word2Vec():
  """
tokenized_sentences = [['Hello','This','is','python','training','by','faculty'],
             ['Hello','This','is','Java','training','by','faculty'],
             ['Hello','This','is','Data Science','training','by','Unfold','Data','Science'],
             ['Hello','This','is','programming','training','']]
from gensim.models import Word2Vec
mymodel = Word2Vec(tokenized_sentences, min_count=1)
print(mymodel)
words = list(mymodel.wv.index_to_key)
print(words)
print(mymodel.wv['Hello'])
mymodel.wv.most_similar("Science")
  """
  print("Not Implemented")


def nlp_word2VecKeras():
  """
  from numpy import array
from keras.preprocessing.text import one_hot
from keras.preprocessing.sequence import pad_sequences
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Embedding
# define documents
Sent = ['Hello, how are you',
        'how are you',
        'how are you doing',
        'I am doing great',
        'I am doing good',
        'I am good']
sent_labels = array([1,1,1,0,0,0])
# integer encoding of the documents
my_vocab_size = 30
encoded_sent = [one_hot(i, my_vocab_size) for i in Sent]
print(encoded_sent)
# padding documents to a max length =5
length = 5
padded_sent = pad_sequences(encoded_sent, maxlen=length, padding='pre')
print(padded_sent)
# defining the model
mymodel = Sequential()
mymodel.add(Embedding(my_vocab_size, 8, input_length=length))
mymodel.add(Flatten())
mymodel.add(Dense(1, activation='sigmoid'))
# compiling the model
mymodel.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
# fiting  the model
mymodel.fit(padded_sent, sent_labels, epochs=30)
# evaluate the model
modelloss, modelaccuracy = mymodel.evaluate(padded_sent, sent_labels, verbose=0)
print('Accuracy: %f' % (modelaccuracy*100))


mysent_to_predict = ['how are you man',
        'I am doing great']
# integer encode the documents
vocab_size = 30
encoded = [one_hot(d, vocab_size) for d in mysent_to_predict]
print(encoded)

# pad documents to a max length of 5 words
max_length = 5
mypadded = pad_sequences(encoded, maxlen=max_length, padding='pre')
print(mypadded)
mymodel.predict(mypadded)
  """
  print("Not Implemented")

def nlp_webScrapper():
  """
  #Making a Request
import requests

# Making a GET request
r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')

statusCode=r.status_code
url=r.url
content=r.content

pip install beautifulsoup4
from bs4 import BeautifulSoup
soup = BeautifulSoup(r.content, 'html.parser')

print(soup.prettify()) #Readable content.
print(soup.title)# Getting the title tag
print(soup.title.name) # Getting the name of the tag
print(soup.title.parent.name)# Getting the name of parent tag
s = soup.find('div', class_='entry-content')
content = s.find_all('p')
  """
  print("Not Implemented")


def nlp_glove():
  """
  import gensim.downloader as api
  glove_model = api.load('glove-wiki-gigaword-300')
  glove_model["beautiful"]
  glove_model.most_similar("girl")
  glove_model.most_similar(positive=['boy', 'queen'], negative=['girl'], topn=10)
  """
  print("Not Implemented")

def normalizeImages(X_train,y_train):
  """
  def normalizeImages(X_train,y_train):
  X_train = X_train.astype('float32')
  X_train/=255
  y_train=y_train.astype('float32')
  y_train/=255
  return X_train,y_train
  """
  X_train = X_train.astype('float32')
  X_train/=255
  y_train=y_train.astype('float32')
  y_train/=255
  return X_train,y_train


def visualize_wordcloud(df, textCol, classCol):
  """
  def visualize_wordcloud(df, textCol, classCol):
  from collections import Counter
  from wordcloud import WordCloud, ImageColorGenerator
  pos_data = df.loc[df[classCol] == 1]
  pos_head_lines = pos_data[textCol]
  words = [eachword for eachheadline in pos_head_lines for eachword in eachheadline.split()]
  word_could_dict=Counter(words)

  wordcloud = WordCloud(width = 1000, height = 500).generate_from_frequencies(word_could_dict)
  plt.figure(figsize=(15,8))
  plt.imshow(wordcloud)
  plt.axis("off")
  #############################
  from wordcloud import WordCloud
  import matplotlib.pyplot as plt
  cloud = WordCloud()
  cloud=cloud.generate("kesperson did not refer to any agreement, and said Pres")
  plt.imshow(cloud)
  #########################
  !pip install goose3
  from goose3 import Goose
  g=Goose()
  url="https://en.wikipedia.org/wiki/Data_science"
  article = g.extract(url)
  article.cleaned_text

  import nltk
  nltk.download('punkt')
  tokens = nltk.tokenize.word_tokenize(article.cleaned_text)
  frequency = nltk.FreqDist(tokens)
  most_common = frequency.most_common(20)

  """
  from collections import Counter
  from wordcloud import WordCloud, ImageColorGenerator
  pos_data = df.loc[df[classCol] == 1]
  pos_head_lines = pos_data[textCol]
  words = [eachword for eachheadline in pos_head_lines for eachword in eachheadline.split()]
  word_could_dict=Counter(words)

  wordcloud = WordCloud(width = 1000, height = 500).generate_from_frequencies(word_could_dict)
  plt.figure(figsize=(15,8))
  plt.imshow(wordcloud)
  plt.axis("off")



def visualize_model(model):
  """
    from tensorflow.keras.utils import plot_model
  plot_model(model, to_file='model.png', show_shapes=True)
  """
  from tensorflow.keras.utils import plot_model
  plot_model(model, to_file='model.png', show_shapes=True)


def visualize_history(history):
  """
  def visualize_history(history):
  # Plot results
  acc = history.history['accuracy']
  val_acc = history.history['val_accuracy']
  loss = history.history['loss']
  val_loss = history.history['val_loss']

  epochs = range(1, len(acc)+1)

  plt.plot(epochs, acc, 'g', label='Training accuracy')
  plt.plot(epochs, val_acc, 'r', label='Validation accuracy')
  plt.title('Training and validation accuracy')
  plt.legend()

  plt.figure()

  plt.plot(epochs, loss, 'g', label='Training loss')
  plt.plot(epochs, val_loss, 'r', label='Validation loss')
  plt.title('Training and validation loss')
  plt.legend()
  plt.show()
  """
  # Plot results
  acc = history.history['accuracy']
  val_acc = history.history['val_accuracy']
  loss = history.history['loss']
  val_loss = history.history['val_loss']

  epochs = range(1, len(acc)+1)

  plt.plot(epochs, acc, 'g', label='Training accuracy')
  plt.plot(epochs, val_acc, 'r', label='Validation accuracy')
  plt.title('Training and validation accuracy')
  plt.legend()

  plt.figure()

  plt.plot(epochs, loss, 'g', label='Training loss')
  plt.plot(epochs, val_loss, 'r', label='Validation loss')
  plt.title('Training and validation loss')
  plt.legend()
  plt.show()

def visualize_classificationEvaluation(y_test,y_pred,target_names = ['No', 'Yes']):
  """
  def model_classificationEvaluation(y_test,y_pred):
  confusion_m=confusion_matrix(y_test,y_pred)
  accuracy=accuracy_score(y_test,y_pred)
  print(classification_report(y_test,y_pred))
  return confusion_m,accuracy
  """
  confusion_m=confusion_matrix(y_test,y_pred)
  accuracy=accuracy_score(y_test,y_pred)
  # Plot Confusion Matrix
  sns.heatmap(confusion_m, annot=True, cbar=False, fmt='d', cmap='Blues')
  plt.ylabel('True Label')
  plt.xlabel('Predicted Label')
  plt.title('Confusion Matrix')
  plt.show()
  print(classification_report(y_test,y_pred), target_names=target_names)
  return confusion_m,accuracy

def visualize_Images(X_train,y_train,randomImage=16):
  """
  def visualize_Images(X_train,y_train,randomImage=16):
  random_indices= np.random.randint(0,940,randomImage)
  plt.figure(figsize=(15, 3 * 4))
  num_rows=4
  num_images_per_row=int(randomImage/num_rows)

  # Display the selected images
  for i, index in enumerate(random_indices):
      plt.subplot(num_rows, num_images_per_row, i + 1)
      plt.imshow(X_train[index],"gray")
      #print(X_train[index][0])
      plt.title(f"{y_train[index]}")
      plt.axis('off')
  plt.show()
  """
  random_indices= np.random.randint(0,940,randomImage)
  plt.figure(figsize=(15, 3 * 4))
  num_rows=4
  num_images_per_row=int(randomImage/num_rows)

  # Display the selected images
  for i, index in enumerate(random_indices):
      plt.subplot(num_rows, num_images_per_row, i + 1)
      plt.imshow(X_train[index],"gray")
      #print(X_train[index][0])
      plt.title(f"{y_train[index]}")
      plt.axis('off')
  plt.show()


def visualize_imageGen(train_gen):
  """
  g_dict = train_gen.class_indices      # defines dictionary {'class': index}
classes = list(g_dict.keys())       # defines list of dictionary's kays (classes), classes names : string
images, labels = next(train_gen)      # get a batch size samples from the generator

plt.figure(figsize= (20, 20))

for i in range(16):

    plt.subplot(4, 4, i + 1)
    image = images[i] / 255       # scales data to range (0 - 255)
    plt.imshow(image)
    index = np.argmax(labels[i])  # get image index
    class_name = classes[index]   # get class of image
    plt.title(class_name, color= 'blue', fontsize= 15)
    plt.axis('off')

plt.show()
  """
  g_dict = train_gen.class_indices      # defines dictionary {'class': index}
  classes = list(g_dict.keys())       # defines list of dictionary's kays (classes), classes names : string
  images, labels = next(train_gen)      # get a batch size samples from the generator

  plt.figure(figsize= (20, 20))

  for i in range(16):

      plt.subplot(4, 4, i + 1)
      image = images[i] / 255       # scales data to range (0 - 255)
      plt.imshow(image)
      index = np.argmax(labels[i])  # get image index
      class_name = classes[index]   # get class of image
      plt.title(class_name, color= 'blue', fontsize= 15)
      plt.axis('off')

  plt.show()


def vector_BOW(X_text,y,max_features=5000):
  """
  def vector_BOW(X_text,y)
  cv = CountVectorizer(max_features=max_features)
  #  X = cv.fit_transform(df["Review"].values).toarray()
  X = cv.fit_transform(X_text).toarray()
  #  y=df["col"].values
  bow = cv.get_feature_names_out()
  return X,y,bow
  """
  cv = CountVectorizer(max_features=max_features)
  #  X = cv.fit_transform(df["Review"].values).toarray()
  X = cv.fit_transform(X_text).toarray()
  #  y=df["col"].values
  bow = cv.get_feature_names_out()
  return cv,X,y,bow

def vector_Tokenize_textToSequence(X,max_words = 1000):
  """
  def vector_Token_padToSequence(X,max_words = 1000):
  # Tokenization
  tokenizer = Tokenizer(num_words=max_words)
  tokenizer.fit_on_texts(X)
  X_sequences = tokenizer.texts_to_sequences(X)
  return tokenizer,X_sequences
  """
  # Tokenization
  tokenizer = Tokenizer(num_words=max_words)
  tokenizer.fit_on_texts(X)
  X_sequences = tokenizer.texts_to_sequences(X)
  return tokenizer,X_sequences

def vector_tfidf(X_text,y,max_features=5000):
  """
  def vector_tfidf(X_text,y,max_features=5000):
  tv = TfidfVectorizer(max_features=5000)
  #X = tv.fit_transform(df_sentiment["Review_processed"].values).toarray()
  #y=df_sentiment["Sentiment"].values

  X = tv.fit_transform(X_text).toarray()
  tfidf = tv.get_feature_names_out()
  return X,y,tfidf
  """
  tv = TfidfVectorizer(max_features=5000)
  #X = tv.fit_transform(df_sentiment["Review_processed"].values).toarray()
  #y=df_sentiment["Sentiment"].values

  X = tv.fit_transform(X_text).toarray()
  tfidf = tv.get_feature_names_out()
  return tv,X,y,tfidf


def model_MultinomialNB(X_train, y_train,X_test):
  """
  def model_MultinomialNB(X_train, y_train,X_test):
  model = MultinomialNB().fit(X_train, y_train)
  y_pred=model.predict(X_test)
  return model, y_pred
  """
  model = MultinomialNB().fit(X_train, y_train)
  y_pred=model.predict(X_test)
  return model, y_pred


def example_readFromCSV():
  """
  df1=pd.read_csv("out.csv")

  for i,row in df1.iterrows():
      x=row["x"]
      y=row["y"]
      #    y=int(i/2048)
      #    x=int(i%2048)
      red=row["Red"]
      green=row["Green"]
      blue=row["Blue"]
      img_array[y,x,0]=red
      img_array[y,x,1]=green
      img_array[y,x,2]=blue
  img_array=img_array.astype("uint8")

  eachrow=[]
  with open('my_file.csv', 'r') as file:
    eachrow=file.read().split("\n")


    """


def example_myReview(myreview, cv,model,label_mapping = {0: 'negative', 1: 'positive'}):
  """
  def example_myReview(myreview, cv,model,label_mapping = {0: 'negative', 1: 'positive'}):
  print("Input : ",myreview)

  myreview_preprocess=nlp_clean_text(myreview)
  print("cleaning : ",myreview_preprocess)

  myreview_preprocess=nlp_remove_stopwords(myreview_preprocess)
  print("Remove StopWords : ",myreview_preprocess)

  myreview_preprocess=nlp_apply_stemming(myreview_preprocess)
  print("Apply Stemming : ",myreview_preprocess)

  myX=cv.transform([myreview_preprocess]).toarray()
  print("Model Features : ",myX)

  mypredict=model.predict(myX)


  # Create a function to convert label-encoded list to normal form
  def decode_labels(encoded_list, label_mapping):
      decoded_list = [label_mapping[label] for label in encoded_list]
      return decoded_list

  # Call the function to decode the list
  decoded_mypredict = decode_labels(mypredict, label_mapping)
  print("Prediction:  : ",decoded_mypredict)
  """


  print("Input : ",myreview)

  myreview_preprocess=nlp_clean_text(myreview)
  print("cleaning : ",myreview_preprocess)

  myreview_preprocess=nlp_remove_stopwords(myreview_preprocess)
  print("Remove StopWords : ",myreview_preprocess)

  myreview_preprocess=nlp_apply_stemming(myreview_preprocess)
  print("Apply Stemming : ",myreview_preprocess)

  myX=cv.transform([myreview_preprocess]).toarray()
  print("Model Features : ",myX)

  mypredict=model.predict(myX)


  # Create a function to convert label-encoded list to normal form
  def decode_labels(encoded_list, label_mapping):
      decoded_list = [label_mapping[label] for label in encoded_list]
      return decoded_list

  # Call the function to decode the list
  decoded_mypredict = decode_labels(mypredict, label_mapping)
  print("Prediction:  : ",decoded_mypredict)









def example_predictReview(myreview, tokenizer, model,max_words=50):
  """
  def example_predict(myreview, tokenizer, model,max_words=50):
  print("Input : ",myreview)

  myreview_preprocess=nlp_clean_text(myreview)
  print("cleaning : ",myreview_preprocess)


  myX=tokenizer.texts_to_sequences([myreview_preprocess])
  myX_padded = pad_sequences(myX, maxlen=max_words)

  mypredict=model.predict(myX_padded)
  label_mapping = {0: 'Not a Sarcasm', 1: 'Sarcasm'}
  print(mypredict)

  threshold = 0.5  # Change this to your desired threshold
  mypredict = [1 if x > threshold else 0 for x in mypredict]

  # Create a function to convert label-encoded list to normal form
  def decode_labels(encoded_list, label_mapping):
      decoded_list = [label_mapping[label] for label in encoded_list]
      return decoded_list

  # Call the function to decode the list
  decoded_mypredict = decode_labels(mypredict, label_mapping)
  print("Prediction:  : ",decoded_mypredict)
  """
  print("Input : ",myreview)

  myreview_preprocess=nlp_clean_text(myreview)
  print("cleaning : ",myreview_preprocess)


  myX=tokenizer.texts_to_sequences([myreview_preprocess])
  myX_padded = pad_sequences(myX, maxlen=max_words)

  mypredict=model.predict(myX_padded)
  label_mapping = {0: 'No', 1: 'Yes'}
  print(mypredict)

  threshold = 0.5  # Change this to your desired threshold
  mypredict = [1 if x > threshold else 0 for x in mypredict]

  # Create a function to convert label-encoded list to normal form
  def decode_labels(encoded_list, label_mapping):
      decoded_list = [label_mapping[label] for label in encoded_list]
      return decoded_list

  # Call the function to decode the list
  decoded_mypredict = decode_labels(mypredict, label_mapping)
  print("Prediction:  : ",decoded_mypredict)


def example_predictImage():
  """
  from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.efficientnet import preprocess_input

def predict_and_display(image_path, model, class_labels):

    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = preprocess_input(img_array)

    prediction = model.predict(img_array)
    predicted_class_index = np.argmax(prediction)

    predicted_class_label = class_labels[predicted_class_index]

    plt.imshow(img)
    plt.axis('off')
    plt.title(f"Predicted Diesease: {predicted_class_label}")
    plt.show()

# Load your trained model
model.load_weights('/content/my_model_weights.h5')

# Define your class labels (e.g., ['car', 'truck', ...])
class_labels = list(train_gen.class_indices.keys())

# Replace 'path_to_test_image' with the path to the image you want to test
image_path_to_test = data_dir + '/Anthracnose/20211008_124253 (Custom).jpg'
predict_and_display(image_path_to_test, model, class_labels)
  """
  print("Not Implemented")


def example_model_rnn():
  """
  from keras.datasets import imdb
(X_train,Y_train), (X_test, Y_test) = imdb.load_data(path = "imdb.npz",num_words = 250)
word_index = imdb.get_word_index()

from tensorflow.keras.utils import pad_sequences
maxword = 250
X_train = pad_sequences(X_train, maxlen = maxword)
X_test = pad_sequences(X_test, maxlen = maxword)

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import SimpleRNN, Dense,Activation, Embedding

rnn = Sequential()
rnn.add(Embedding(len(word_index), 32, input_length = len(X_train[0])))
rnn.add(SimpleRNN(16, input_shape = (len(word_index), maxword), return_sequences = False, activation = "relu"))
rnn.add(Dense(1))
rnn.add(Activation("sigmoid"))
rnn.summary()

rnn.compile(optimizer='adam',     loss="binary_crossentropy",     metrics=["accuracy"])
rnn.fit(x=X_train, y=Y_train, batch_size=32, epochs=4,validation_data=(X_test, Y_test))
  """

def example_model_lstm(X_train, X_test,y_train,y_test,inputLen=50,max_words=1000):
  """
  def example_model_lstm(X_train, X_test,y_train,y_test,inputLen=50,max_words=1000)
  # Build LSTM Model
  embedding_dim = 50
  lstm_units = 100
  X_train_padded = pad_sequences(X_train, maxlen=inputLen)
  X_test_padded = pad_sequences(X_test, maxlen=inputLen)

  model = Sequential()
  model.add(Embedding(input_dim=max_words, output_dim=embedding_dim, input_length=inputLen))
  model.add(LSTM(units=lstm_units, dropout=0.2, recurrent_dropout=0.25)))
  model.add(Dense(1, activation='sigmoid'))

  # Compile the model
  model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
  # Train the model
  history= model.fit(X_train_padded, y_train, epochs=10, batch_size=32, validation_split=0.1)

  # Evaluate the model
  loss, accuracy = model.evaluate(X_test_padded, y_test)
  return model, history, loss, accuracy
  """
  # Build LSTM Model
  embedding_dim = 50
  lstm_units = 100
  X_train_padded = pad_sequences(X_train, maxlen=inputLen)
  X_test_padded = pad_sequences(X_test, maxlen=inputLen)

  model = Sequential()
  model.add(Embedding(input_dim=max_words, output_dim=embedding_dim, input_length=inputLen))
  model.add(LSTM(units=lstm_units, dropout=0.2, recurrent_dropout=0.25))
  model.add(Dense(1, activation='sigmoid'))

  # Compile the model
  model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
  # Train the model
  history= model.fit(X_train_padded, y_train, epochs=10, batch_size=32, validation_split=0.1)

  # Evaluate the model
  loss, accuracy = model.evaluate(X_test_padded, y_test)
  return model, history, loss, accuracy


def example_model_bidirectionalLSTM():
  """
  ## Creating model
  embedding_vector_features=40
  model=Sequential()
  model.add(Embedding(voc_size,embedding_vector_features,input_length=sent_length))
  model.add(Bidirectional(LSTM(100)))
  model.add(Dense(1,activation='sigmoid'))
  model.compile(loss='binary_crossentropy',optimizer='adam',metrics=['accuracy'])
  print(model.summary())
  """
  print("Not Implemented")

def example_model_prediction_lstm():
  '''
  with open("/content/drive/Shareddrives/mtech-datashare/dataset/NLP/india.txt", 'r', encoding='utf-8') as myfile:
    mytext = myfile.read()



mytext="........"
mytokenizer = Tokenizer()
mytokenizer.fit_on_texts([mytext])
total_words = len(mytokenizer.word_index) + 1

my_input_sequences = []
for line in mytext.split('\n'):
    print(line)
    token_list = mytokenizer.texts_to_sequences([line])[0]
    print(token_list)
    #print(token_list)
    for i in range(1, len(token_list)):
        my_n_gram_sequence = token_list[:i+1]
        print(my_n_gram_sequence)
        my_input_sequences.append(my_n_gram_sequence)

max_sequence_len = max([len(seq) for seq in my_input_sequences])
input_sequences = np.array(pad_sequences(my_input_sequences, maxlen=max_sequence_len, padding='pre'))

X = input_sequences[:, :-1]
y = input_sequences[:, -1]

y = np.array(tf.keras.utils.to_categorical(y, num_classes=total_words))

model = Sequential()
model.add(Embedding(total_words, 100, input_length=max_sequence_len-1))
model.add(LSTM(150))
model.add(Dense(total_words, activation='softmax'))
print(model.summary())

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])
model.fit(X, y, epochs=100, verbose=1)

input_text = "who is the "
predict_next_words= 7

for _ in range(predict_next_words):
    token_list = mytokenizer.texts_to_sequences([input_text])[0]
    print(token_list)
    token_list = pad_sequences([token_list], maxlen=max_sequence_len-1, padding='pre')
    predicted = np.argmax(model.predict(token_list), axis=-1)
    output_word = ""
    for word, index in mytokenizer.word_index.items():
        if index == predicted:
            output_word = word
            break
    input_text += " " + output_word

print(input_text)
  '''
  print("Not Implemented")

def example_optimizer():
  """
  #Stochastic Gradient Descent (SGD):
  tf.keras.optimizers.SGD(learning_rate=0.01, momentum=0.9)

  #RMSprop:
  tf.keras.optimizers.RMSprop(learning_rate=0.001, rho=0.9)

  #Adam:
  tf.keras.optimizers.Adam(learning_rate=0.001, beta_1=0.9, beta_2=0.999)
  optimizer = tf.keras.optimizers.Adam(learning_rate=0.001)
  model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])

  #Adagrad:
  tf.keras.optimizers.Adagrad(learning_rate=0.01)

  #Adadelta:
  tf.keras.optimizers.Adadelta(learning_rate=1.0, rho=0.95)

  #Nadam:
  tf.keras.optimizers.Nadam(learning_rate=0.002, beta_1=0.9, beta_2=0.999)

  #FTRL:
  tf.keras.optimizers.FTRL(learning_rate=0.01, learning_rate_power=-0.5)

  #Adamax:
  tf.keras.optimizers.Adamax(learning_rate=0.002, beta_1=0.9, beta_2=0.999)

  #Proximal Adagrad:
  tf.keras.optimizers.ProximalAdagrad(learning_rate=0.01)

  #Proximal Gradient Descent:
  tf.keras.optimizers.ProximalGradientDescent(learning_rate=0.01)
  """
  print("Not Implemented")

def example_model_fit():
  """
  from tensorflow.keras.callbacks import EarlyStopping,ModelCheckpoint
history = model.fit(X_train, y_train, epochs=20,batch_size=32)
history = model.fit(X_train, y_train, epochs=5, batch_size=32, validation_split=0.2)
history = model.fit(X_train, y_train, epochs=10, batch_size=32, validation_data=(X_val, y_val))
early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
model_checkpoint = ModelCheckpoint(filepath='best_model.h5', save_best_only=True, monitor='val_loss')
history = model.fit(X_train, y_train, epochs=100, batch_size=32, validation_data=(X_val, y_val), callbacks=[early_stopping, model_checkpoint])
history = model.fit(x=train_gen, epochs = 10,verbose = 1,validation_data = valid_gen, validation_steps = None,shuffle = False, batch_size = 32, callbacks = [early_stopping])
  """
  print("Not Implemented")


def example_model_pretrained():
  """

  from tensorflow.keras import regularizers
  from keras.callbacks import EarlyStopping, LearningRateScheduler
  from tensorflow.keras.preprocessing import image
  from tensorflow.keras.applications.efficientnet import preprocess_input
  from tensorflow.keras.applications import EfficientNetB0, EfficientNetB1, EfficientNetB2, EfficientNetB3, EfficientNetB4, EfficientNetB5, EfficientNetB6, EfficientNetB7
  from tensorflow.keras.optimizers import Adam, Adamax
  from tensorflow.keras.metrics import categorical_crossentropy
  from tensorflow.keras.preprocessing.image import ImageDataGenerator
  from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Activation, Dropout, BatchNormalization

  # Create Model Structure
  img_size = (224, 224)
  channels = 3
  img_shape = (img_size[0], img_size[1], channels)
  class_count = len(list(train_gen.class_indices.keys())) # to define number of classes in dense layer

  # create pre-trained model (you can built on pretrained model such as :  efficientnet, VGG , Resnet )
  # we will use efficientnetb7 from EfficientNet family.

  base_model = tf.keras.applications.efficientnet.EfficientNetB7(include_top= False, weights= "imagenet", input_shape= img_shape, pooling= 'max')
  base_model.trainable = False

  model = Sequential([
      base_model,
      BatchNormalization(axis= -1, momentum= 0.99, epsilon= 0.001),
      Dense(128,kernel_regularizer= regularizers.l2(l= 0.016), activity_regularizer= regularizers.l1(0.006),
                  bias_regularizer= regularizers.l1(0.006), activation = 'relu'),
      Dropout(rate= 0.45, seed= 123),
      Dense(class_count, activation= 'softmax')
  ])

  model.compile(Adamax(learning_rate = 0.001), loss = 'categorical_crossentropy', metrics= ['accuracy'])
  model.summary()
  """
  print("Not Implemented")

def example_model_machineTranslation():
  """
  #read readFromFileOrZipFile
  import tensorflow as tf
from tensorflow.keras import layers
import string
import re

strip_chars = string.punctuation + "¿"
strip_chars = strip_chars.replace("[", "")
strip_chars = strip_chars.replace("]", "")



def custom_standardization(input_string):
    lowercase = tf.strings.lower(input_string)
    return tf.strings.regex_replace(
        lowercase, f"[{re.escape(strip_chars)}]", "")

vocab_size = 15000
sequence_length = 20

source_vectorization = layers.TextVectorization(
    max_tokens=vocab_size,
    output_mode="int",
    output_sequence_length=sequence_length,
)
target_vectorization = layers.TextVectorization(
    max_tokens=vocab_size,
    output_mode="int",
    output_sequence_length=sequence_length + 1,
    standardize=custom_standardization,
)
train_english_texts = [pair[0] for pair in train_pairs]
train_spanish_texts = [pair[1] for pair in train_pairs]
source_vectorization.adapt(train_english_texts)
target_vectorization.adapt(train_spanish_texts)


batch_size = 64

def format_dataset(eng, spa):
    eng = source_vectorization(eng)
    spa = target_vectorization(spa)
    return ({
        "english": eng,
        "spanish": spa[:, :-1],
    }, spa[:, 1:])

def make_dataset(pairs):
    eng_texts, spa_texts = zip(*pairs)
    eng_texts = list(eng_texts)
    spa_texts = list(spa_texts)
    dataset = tf.data.Dataset.from_tensor_slices((eng_texts, spa_texts))
    dataset = dataset.batch(batch_size)
    dataset = dataset.map(format_dataset, num_parallel_calls=4)
    return dataset.shuffle(2048).prefetch(16).cache()

train_ds = make_dataset(train_pairs)
val_ds = make_dataset(val_pairs)


from tensorflow import keras
from tensorflow.keras import layers

embed_dim = 256
latent_dim = 1024

source = keras.Input(shape=(None,), dtype="int64", name="english")
x = layers.Embedding(vocab_size, embed_dim, mask_zero=True)(source)
encoded_source = layers.Bidirectional(
    layers.GRU(latent_dim), merge_mode="sum")(x)


past_target = keras.Input(shape=(None,), dtype="int64", name="spanish")
x = layers.Embedding(vocab_size, embed_dim, mask_zero=True)(past_target)
decoder_gru = layers.GRU(latent_dim, return_sequences=True)
x = decoder_gru(x, initial_state=encoded_source)
x = layers.Dropout(0.5)(x)
target_next_step = layers.Dense(vocab_size, activation="softmax")(x)
seq2seq_rnn = keras.Model([source, past_target], target_next_step)


seq2seq_rnn.compile(
    optimizer="rmsprop",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"])
seq2seq_rnn.fit(train_ds, epochs=1, validation_data=val_ds)


import numpy as np
spa_vocab = target_vectorization.get_vocabulary()
spa_index_lookup = dict(zip(range(len(spa_vocab)), spa_vocab))
max_decoded_sentence_length = 20

def decode_sequence(input_sentence):
    tokenized_input_sentence = source_vectorization([input_sentence])
    decoded_sentence = "[start]"
    for i in range(max_decoded_sentence_length):
        tokenized_target_sentence = target_vectorization([decoded_sentence])
        next_token_predictions = seq2seq_rnn.predict(
            [tokenized_input_sentence, tokenized_target_sentence])
        sampled_token_index = np.argmax(next_token_predictions[0, i, :])
        sampled_token = spa_index_lookup[sampled_token_index]
        decoded_sentence += " " + sampled_token
        print(decoded_sentence)
        if sampled_token == "[end]":
            break
    return decoded_sentence

test_eng_texts = [pair[0] for pair in test_pairs]
for _ in range(20):
    input_sentence = random.choice(test_eng_texts)
    print("-")
    print(input_sentence)
    print(decode_sequence(input_sentence))
  """
  print("Not Implemented")

def example_imagegenArray():
  """
  from tensorflow.keras.preprocessing.image import ImageDataGenerator



   #X_train, y_train = shuffle(X_train, y_train, random_state=42)
# Create an instance of ImageDataGenerator for training with augmentation
train_datagen2 = ImageDataGenerator(
    zoom_range=0.2,
    #horizontal_flip=True,
    validation_split=0.05
    )

# Flow from numpy arrays and generate augmented images for training
train_generator2 = train_datagen2.flow(
    X_train_augmented, y_train_augmented,
    batch_size=batch_size,
    shuffle=True , # set to True for training data

)

# Create a validation generator
#validation_generator = train_datagen2.flow(
#    X_val, y_val,
#    batch_size=batch_size,
#    shuffle=True
#)

# Flow from numpy arrays and generate images for testing
test_generator2 = test_datagen.flow(
    X_test, y_test,
    batch_size=batch_size,
    shuffle=False  # set to False for testing data
)

  """
  print("Not Implemented")

def example_imagegenDF():
  """
  from tensorflow.keras.preprocessing.image import ImageDataGenerator
  def scalar(img):
    return img

  #From DF, with Path in df.

  tr_gen = ImageDataGenerator(preprocessing_function= scalar,
                           rotation_range=40,
                           width_shift_range=0.2,
                           height_shift_range=0.2,
                           brightness_range=[0.4,0.6],
                           zoom_range=0.3,
                           horizontal_flip=True,
                           vertical_flip=True)
  train_gen = tr_gen.flow_from_dataframe(train_df,
                                       x_col = 'filepaths',
                                       y_col= 'labels',
                                       target_size = img_size,
                                       class_mode= 'categorical',
                                       color_mode= 'rgb',
                                       shuffle= True,
                                       batch_size=batch_size)
   #From DF, with image in xTrain, XTest.


   #X_train, y_train = shuffle(X_train, y_train, random_state=42)
# Create an instance of ImageDataGenerator for training with augmentation
train_datagen2 = ImageDataGenerator(
    zoom_range=0.2,
    #horizontal_flip=True,
    validation_split=0.05
    )

# Flow from numpy arrays and generate augmented images for training
train_generator2 = train_datagen2.flow(
    X_train_augmented, y_train_augmented,
    batch_size=batch_size,
    shuffle=True , # set to True for training data

)

# Create a validation generator
#validation_generator = train_datagen2.flow(
#    X_val, y_val,
#    batch_size=batch_size,
#    shuffle=True
#)

# Flow from numpy arrays and generate images for testing
test_generator2 = test_datagen.flow(
    X_test, y_test,
    batch_size=batch_size,
    shuffle=False  # set to False for testing data
)

  """
  print("Not Implemented")

def example_model_compile():
  """
  Activation: linear
model.add(Dense(1, activation='linear'))
model.compile(optimizer='adam', loss='mean_squared_error',metrics=['mean_absolute_error'])

Activation: sigmoid
model.add(Dense(1, activation='sigmoid'))
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy']

Activation: softmax
model.add(Dense(10, activation='softmax'))  # multi-class classification
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

model.add(Dense(10, activation='softmax'))  # Output layer with softmax activation for multi-class classification
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy',metrics=['accuracy'])
# Use sparse categorical crossentropy for multi-class classification with integer labels
  """

def example_model_nn():
  """
  # CONV -> RELU -> MAXPOOL
model = Sequential()

    # DENSE -> RELU
model.add(Input(shape=(224, 224,3)))
model.add(Flatten())
model.add(Dense(1024, activation="relu"))
model.add(BatchNormalization())

# DENSE -> RELU
model.add(Dense(256, activation="relu"))
model.add(BatchNormalization())
model.add(Dropout(0.25))

# DENSE -> RELU
model.add(Dense(128, activation="relu"))
model.add(BatchNormalization())

# DENSE -> RELU
model.add(Dense(64, activation="relu"))
model.add(BatchNormalization())
model.add(Dropout(0.25))

model.add(Dense(1, activation="sigmoid"))
model.summary()
  """

def example_model_bert_hamspam():
  """
  from sklearn.model_selection import train_test_split
import pandas as pd
import tensorflow_hub as hub
import tensorflow_text as text
df = pd.read_csv('https://raw.githubusercontent.com/akdiwahar/dataset/main/Sem3/NLP/spam1.csv', encoding='latin-1')
df1=df[df["Category"]=="ham"].sample(747)
df2=df[df["Category"]=="spam"]
df_final=pd.concat([df1,df2])
df_final["isSpam"]=df_final["Category"].apply(lambda x : 1 if x=="spam" else 0)
X_train, X_test, y_train, y_test = train_test_split(df_final['Message'],df_final['isSpam'], stratify=df_final['isSpam'])

bert_preprocess = hub.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_preprocess/3")
bert_encoder = hub.KerasLayer("https://tfhub.dev/tensorflow/bert_en_uncased_L-12_H-768_A-12/4")

def get_sentence_embeding(sentences):
    preprocessed_text = bert_preprocess(sentences)
    return bert_encoder(preprocessed_text)['pooled_output']

e = get_sentence_embeding([
    "banana",
    "grapes",
    "mango",
    "jeff bezos",
    "elon musk",
    "bill gates"
]
)
from sklearn.metrics.pairwise import cosine_similarity
cosine_similarity([e[0]],[e[1]])

import tensorflow as tf

### Model
# Bert layers
text_input = tf.keras.layers.Input(shape=(), dtype=tf.string, name='text')
preprocessed_text = bert_preprocess(text_input)
outputs = bert_encoder(preprocessed_text)

# Neural network layers
l = tf.keras.layers.Dropout(0.1, name="dropout")(outputs['pooled_output'])
l = tf.keras.layers.Dense(1, activation='sigmoid', name="output")(l)

# Use inputs and outputs to construct a final model
model = tf.keras.Model(inputs=[text_input], outputs = [l])
model.summary()

METRICS = [
      tf.keras.metrics.BinaryAccuracy(name='accuracy'),
      tf.keras.metrics.Precision(name='precision'),
      tf.keras.metrics.Recall(name='recall')
]

model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=METRICS)

model.fit(X_train, y_train, epochs=10)
model.evaluate(X_test, y_test)

y_predicted = model.predict(X_test)
y_predicted = y_predicted.flatten()
import numpy as np

y_predicted = np.where(y_predicted > 0.5, 1, 0)


  """
  print("Not Implemented")

def example_model_topicModelling():
  """
  import re
  import spacy
  from nltk.corpus import stopwords
  from nltk.stem.wordnet import WordNetLemmatizer
  import string
  from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
  import numpy as np
  from sklearn.decomposition import LatentDirichletAllocation
  nlp = spacy.load('en_core_web_sm')
  corpus = [D1, D2, D3, D4, D5]

  #PreProcessong
  import nltk
  nltk.download('stopwords')
  nltk.download('wordnet')
  stop = set(stopwords.words('english'))
  exclude = set(string.punctuation)
  lemma = WordNetLemmatizer()

  def clean(doc):
      stop_free = " ".join([i for i in doc.lower().split() if i not in stop])
      punc_free = ''.join(ch for ch in stop_free if ch not in exclude)
      normalized = " ".join(lemma.lemmatize(word) for word in punc_free.split())
      return normalized

  clean_corpus = [clean(doc).split() for doc in corpus]

  #Convert Text into Numerical Representation
  tf_idf_vectorizer = TfidfVectorizer(tokenizer=lambda doc: doc, lowercase=False)
  cv_vectorizer = CountVectorizer(tokenizer=lambda doc: doc, lowercase=False)
  tf_idf_arr = tf_idf_vectorizer.fit_transform(clean_corpus)
  cv_arr = cv_vectorizer.fit_transform(clean_corpus)

  #Vocabulary
  vocab_tf_idf = tf_idf_vectorizer.get_feature_names_out()
  vocab_cv = cv_vectorizer.get_feature_names_out()

  #LDA
  lda_model = LatentDirichletAllocation(n_components = 6, max_iter = 20, random_state = 20)
  X_topics = lda_model.fit_transform(tf_idf_arr)
  topic_words = lda_model.components_


  # Retrive Topic
  n_top_words = 6

  for i, topic_dist in enumerate(topic_words):
      sorted_topic_dist = np.argsort(topic_dist)
      topic_words = np.array(vocab_tf_idf)[sorted_topic_dist]
      print(topic_words)
      topic_words = topic_words[:-n_top_words:-1]
      print ("Topic", str(i+1), topic_words)

  #  Annotating the topics
  doc_topic = lda_model.transform(tf_idf_arr)
  for n in range(doc_topic.shape[0]):
      topic_doc = doc_topic[n].argmax()
      print ("Document", n+1, " -- Topic:" ,topic_doc)
  """
  print("Not Implemented")


def example_face():
  """
  !wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_eye.xml
  !wget https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml
  import cv2
  import matplotlib.pyplot as plt

  face_detector=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
  eye_dectector = cv2.CascadeClassifier('haarcascade_eye.xml')
  img = cv2.imread('/content/drive/Shareddrives/mtech-datashare/dataset/ComputerVision/Group.jpg')
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  results = face_detector.detectMultiScale(gray, 1.3, 5)
  for (x,y,w,h) in results:
      cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)

  plt.imshow(img)
  """
  print("Not Implemented")


def example_cv2_usage():
  """
image = cv2.imread("Landscape-Color.jpg")
bgr_img = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
grey_img=cv2.cvtColor(bgr_img, cv2.COLOR_BGR2GRAY)
bgr_img2 = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
resized_img=cv2.resize(bgr_img,(600,600))
resized_image = cv2.resize(image, (target_width, target_height), interpolation=cv2.INTER_LINEAR)

INTER_NEAREST – a nearest-neighbor interpolation
INTER_LINEAR – a bilinear interpolation (used by default)
INTER_AREA – resampling using pixel area relation. It may be a preferred method for image decimation, as it gives moire’-free results. But when the image is zoomed, it is similar to the INTER_NEAREST method.
INTER_CUBIC – a bicubic interpolation over 4×4 pixel neighborhood
INTER_LANCZOS4 – a Lanczos interpolation over 8×8 pixel neighborhood


#Histogram Equalization
b,g,r= cv2.split(resized_img)
beq = cv2.equalizeHist(b)

hist_eq_image=cv2.merge((beq,geq,req))

#intensity Level Slicing
mask = np.zeros_like(r)
mask[(r >= lower_bound) & (r <= upper_bound)] = 255
masks=np.dstack([mask,mask,mask])  # masks=cv2.merge((mask,mask,mask))
enhanced_image = cv2.bitwise_and(bgr_img,masks)

# Bit Plane Slicing
bit_plane = 4
extracted_plane = (image >> bit_plane) & 1
bit_plane_image = extracted_plane * 25

#Gray to color
colormap_image = cv2.applyColorMap(gray, cv2.COLORMAP_JET)

#contrast strench/Linear transformation
intensity_img=(((resized_img - current_min) / (current_max - current_min)) * (max_intensity - min_intensity) )+ min_intensity
intensity_img=np.uint8(intensity_img)

# Power Law Transformation
gamma = 0.5
enhanced_image = np.power(image / 255.0, gamma) * 255.0
enhanced_image = np.uint8(enhanced_image)

# Log Transformation
c = 255 / np.log(1 + np.max(image))
enhanced_image = c * np.log(1 + image)
enhanced_image = np.uint8(enhanced_image)

#add/subtract two image
 cv2.add(resized_image1, resized_image2)
 cv2.subtract(resized_img,newimage)
 np.vstack([resized_img,newimage])

  """
  print("Not Implemented")

def example_cv2_usage2():
  """
  # Gaussian blur
    ksize = (5, 5)  # Kernel size, adjust as needed
    sigma = 0  # Standard deviation, 0 means the kernel is calculated based on ksize
    blurred_img = cv2.GaussianBlur(img, ksize, sigma)
# Brighten Image 
    brightness_factor = 50
    brightened_img = cv2.add(img, np.ones_like(img) * brightness_factor)
    brightened_img = np.clip(brightened_img, 0, 255)
# Sharpen 
    sharpening_kernel = np.array([[-1, -1, -1],
                                  [-1, 9, -1],
                                  [-1, -1, -1]])
    sharpened_img = cv2.filter2D(img, -1, sharpening_kernel)

#Contrast adjustment(Linear)
   gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    min_pixel_value = 0
    max_pixel_value = 255
    min_intensity = np.min(gray_img)
    max_intensity = np.max(gray_img)
    contrast_stretched_img = np.uint8(        (gray_img - min_intensity) / (max_intensity - min_intensity) * (max_pixel_value - min_pixel_value) + min_pixel_value    )
# GAmma Correction    
    gamma = 1.5
    corrected_img = np.power(img_float, gamma)
    corrected_img = np.clip(corrected_img, 0, 1)
    corrected_img = (corrected_img * 255).astype(np.uint8)

  """
  print("Not Implemented")

def example_cv2_affine():
  """
  #Translation
  tx = 500  # Translation in the x-direction
  ty = 100  # Translation in the y-direction
  translation_matrix = np.float32([[1, 0, tx], [0, 1, ty]])
  translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))


  # Rotate
  angle = 180
  center = (width / 2, height / 2)
  rotation_matrix = cv2.getRotationMatrix2D(center, angle, 1.0)# A scale value of 1.0
  rotated_image = cv2.warpAffine(resized_image, rotation_matrix, (width, height))

  # Shear
  shearFactor=0.3
  translation_matrix = np.float32([[1, shearFactor, 0], [0, 1, 0]])
  translated_image = cv2.warpAffine(image, translation_matrix, (image.shape[1], image.shape[0]))


  #remove noise
  img_smooth = cv2.GaussianBlur(img_grey, (13,13), 0)


  # Contrast control
  alpha = 1.5 # Contrast control
  beta = 10 # Brightness control

  # call convertScaleAbs function
  adjusted = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)
  """
  print("Not Implemented")

def readFromFileOrZipFile():
  """
  import wget
  import zipfile

  zip_file_name = 'spa-eng.zip'
  extract_to_directory = 'trans'
  with zipfile.ZipFile(zip_file_name, 'r') as zip_ref:
      zip_ref.extractall(extract_to_directory)
  print(f"Successfully extracted files to {extract_to_directory}")

  text_file = "trans/spa-eng/spa.txt"
  with open(text_file , 'r', encoding='utf-8') as f:
      lines = f.read().split("\n")[:-1]
  text_pairs = []
  for line in lines:
      english, spanish = line.split("\t")
      spanish = "[start] " + spanish + " [end]"
      text_pairs.append((english, spanish))
  """
  print("Not Implemented")




def downloadFromKaggle(apiurl):
  """
  def downloadFromKaggle(apiurl):
  import opendatasets as od
  od.download("apiurl")
  """
  import opendatasets as od
  od.download("apiurl")


def helpFunc():
	 return [
	'displayImages',
	 'displayImagesFromPath',
	 'downloadFromKaggle',
	 'edge_applyCanny',
	 'edge_applySobel',
	 'enhance_clahe',
	 'enhance_contrast_stretching',
	 'enhance_gamma_correction',
	 'enhance_histogram_equalization',
	 'enhance_intensityLevelSlicing',
	 'example_cv2_affine',
	 'example_cv2_usage',
	 'example_edge',
	 'example_enhance',
	 'example_extract',
	 'example_face',
	 'example_imagegenArray',
	 'example_imagegenDF',
	 'example_model_bert_hamspam',
	 'example_model_bidirectionalLSTM',
	 'example_model_compile',
	 'example_model_fit',
	 'example_model_lstm',
	 'example_model_machineTranslation',
	 'example_model_nn',
	 'example_model_prediction_lstm',
	 'example_model_pretrained',
	 'example_model_rnn',
	 'example_model_topicModelling',
	 'example_myReview',
	 'example_optimizer',
	 'example_predictImage',
	 'example_predictReview',
	 'example_seg',
	 'extract_HOG',
	 'extract_contourbased',
	 'extract_harrisConrner',
	 'extract_sift',
	 'helpImport',
	 'helpenv',
	 'model_MultinomialNB',
	 'nlp_NamedEntityRegconinzation',
	 'nlp_apply_lemmu',
	 'nlp_apply_stemming',
	 'nlp_clean_text',
	 'nlp_glove',
	 'nlp_pos',
	 'nlp_remove_stopwords',
	 'nlp_stem_onehotTokenize',
	 'nlp_webScrapper',
	 'nlp_word2Vec',
	 'nlp_word2VecKeras',
	 'normalizeImages',
	 'readFromFileOrZipFile',
	 'readImage',
	 'readImagesFromPath',
	 'resizeImage',
	 'resource_file_path',
	 'seg_countours',
	 'seg_kmeansSegment',
	 'seg_regionGrowing2',
	 'seg_regionsplitMerge',
	 'seg_threshold_otsu',
	 'seg_watershedSegmentation',
	 'test_train_split',
	 'vector_BOW',
	 'vector_Tokenize_textToSequence',
	 'vector_tfidf',
	 'visualize_Images',
	 'visualize_classificationEvaluation',
	 'visualize_history',
	 'visualize_imageGen',
	 'visualize_model',
	 'visualize_wordcloud']


