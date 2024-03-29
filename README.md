# jcm.39.2.430-437.2001
https://journals.asm.org/doi/10.1128/jcm.39.2.430-437.2001

# Python code for similary detection. 

[![Watch the video](https://img.youtube.com/vi/WKOYBTMHhmc/default.jpg)](https://youtu.be/WKOYBTMHhmc)




# Template Matching in OpenCV


https://docs.opencv.org/3.4/d4/dc6/tutorial_py_template_matching.html


![Template matching](/match.jpg "Template Matching")


Install 

    virtualenv or pip -m venv envsim 
    envsim\bin\activate or envsim\scrip\activate
    pip install -r requierement.txt 
    python test2.py 

line 14 : change the value 
    threshold = 0.999

![Template Matching .999!](/res99.png "Template Matching .999")

    threshold = 0.97

    
![Template Matching .97!](/res97.png "Template Matching .97")

    threshold = 0.95

![Template Matching .95!](/res95.png "Template Matching .95")

    threshold = 0.90

![Template Matching .90!](/res95.png "Template Matching .90")


# Compute levenstein between Initial Area and BIK Area

With 0.97 we save matching zone : 

    Initial Zone
    
![Zone initiale!](/crop595_460.png  "Zone initiale")

    Witness Area 

![Zone temoin!](/crop1127_81.png  "Zone temoin")

    BIK Area 
    
![Zone BIK!](/crop843_523.png  "Zone BIK")

 
    python  levenstein.py
    array([220, 220, 220, ..., 233, 233, 232], dtype=uint8)
    Levenshtein Distance between initial Area & BIK Area  is 3436


    chatgptdiff.py 
    
![Heatmap!](/heatmap2.png  "heatmap")


![diff after linearisation of 2 images!](/histodiff.png  "diff after linearisation of two images")


    

# fastfeature

https://docs.opencv.org/4.x/df/d0c/tutorial_py_fast.html


    python fastfeature.py 


    
![Fast Feature reult!](/fastfeature.png "Fast Feature")
