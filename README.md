# project-MUGI
This project serves as a long term process that will assist in me learning various machine learning topics as well as bring to fruition a passion project. I envision MUGI as an end product to be a computer vision based appliation made to assist athletes specifically martial artist in tracking form, biases, competetion analysis and feedback.  Below you can find my logs and updates so far. NOTE: Last log is not up to date 


# Phase One

1. Choose a pose estimation model to use and how to implement in an IOS app
     - We want the top down approach which is human detection first then joint detection 
     - https://developer.apple.com/videos/play/tech-talks/10154/
     - https://developers.google.com/mediapipe/framework/getting_started/ios
     - Mediapipe vs yolo 
         -will occlusion occur?
          -barbells, other humans ( rarley happens) -> does not matter
     - fast movements vs slow movements
            -fast movements to be taken more into conderation in phase 2, must be able to scale while still being accurate;                 consider possibility of transfer learning

    

    - Conclusion: For now , Use media pipe as it uses blazepose whcih was built with real time in mind

2. Find an Environment to develop on
   

