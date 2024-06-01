
![Machine Learning](https://img.shields.io/badge/Machine_Learning-SVM-blue?style=for-the-badge)
![ASL](https://img.shields.io/badge/Sign_Language-Translation-red?style=for-the-badge)
<br/>
<br/>
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)


<h2>SignSense <img src = "./pics/SignSense.png" height = 25px width = 50px /></h2> 

<h3> Sign Language Detection & Translation Web App </h3>
<strong>Developed By - </strong>
<ul>  
  <li> <a href = "https://www.linkedin.com/in/atharva-kadam-07b101228/" target = "_blank">Atharva Kadam</a></li>
  <li> <a href = "https://www.linkedin.com/in/aditya-ace/" target = "_blank" >Aditya A</a></li>
  <li> <a href = "https://www.linkedin.com/in/makarand-warade-9a1b32230/" target = "_blank" >Makarand Warade</a></li>
  
  
  
</ul>

<br>



## Toolset 🛠️
<i> Languages, Equipments, Environment </i>

![Python](https://img.shields.io/badge/Python-fed436?style=for-the-badge&logo=python)
![Mediapipe](https://img.shields.io/badge/Mediapipe-%23FF474C?style=for-the-badge&logo=https%3A%2F%2Fencrypted-tbn0.gstatic.com%2Fimages%3Fq%3Dtbn%3AANd9GcTi9TmikYW0uj3kX-OyYSNm_uwxiWOUTNoEzA%26s&link=https%3A%2F%2Fai.google.dev%2Fedge%2Fmediapipe%2Fsolutions%2Fguide)
![Sklearn](https://img.shields.io/badge/Scikit_Learn-%23f99938?style=for-the-badge&logo=Scikit%20learn&logoColor=black)
![Numpy](https://img.shields.io/badge/Numpy-%234d76ce?style=for-the-badge&logo=Numpy)
![OpenCV](https://img.shields.io/badge/OpenCV-grey?style=for-the-badge&logo=opencv)
<br/>
![Pickle](https://img.shields.io/badge/pickle-green?style=for-the-badge&logo=pickle)
![Flask](https://img.shields.io/badge/Flask-65DAF7?style=for-the-badge&logo=flask&logoColor=black)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)


## OverView 🔎

<br>
SignSense is a sign language detection system aimed at bridging communication gaps for the hearing impaired.


<br><i>
<a href = "https://en.wikipedia.org/wiki/Sign_language" target="_blank">Sign Language</a> is a vital means of communication for millions of individuals worldwide, particularly those who are deaf or hard of hearing. This software, aptly named SignSense, leverages Computer Vision and Machine Learning techniques to Detect and Translate Sign Language Gestures into Text in real time.
<br>
</i>

## Development 🔧


 The project development has been divided into two parts, Model Development & Front-End Integration. 

### Model Development 
<img src = "./pics/image.png" height = 500px width = 800px>
This stage involves creation of the Machine Learning Model, and exporting it inorder use in integration. 
<li>Dataset Creation</li>
<li>Data Processing</li>
<li>Model Training</li>
<li>Model Testing</li>
<li>Model Export</li>
<br/>

### Front End Integration 

<img src = "./pics/image1.png" height = 400px width = 600px>
This stage involves creation of the Integrated ML Model with Front End using Flask Framework. 
<br/>

## Implementation 🖑🏾
1. Simply Download 
2. Open PowerShell in your downloaded directory and run the following command.
    <pre><code>pip download -r requirements.txt </code></pre>

3. Once the Process is Complete, run the following Commands.
    <pre><code> cd Deploy </code></pre>
    <pre><code> python app.py </code></pre>
    
    Click on the link, and the browser window would pop up. 

## Update
To create your own model follow the following steps. 
1.  <pre><code>cd Model</code></pre>
2.  <pre><code>python collect_imgs.py</code></pre>
  Enter the No. of letters you want to train and the number of images you want to collect for each letter. 
  To start capturing press G. 
  
3. <pre><code>python create_dataset.py</code></pre>
4. <pre><code>python train_classifier.py</code></pre>
5. <pre><code>python test_classifier.py</code></pre>

Then copy the model.p into the Models directory of Deployment Folder and Simply follow the Implementation. 

  
  <center><footer><strong><i>Any Suggestion, Contribution and Forking is Highly Appreciated!!</i></strong></footer></center>

