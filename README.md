# project-MUGI
This project serves as a long term process that will assist in me learning various machine learning topics as well as bring to fruition a passion project. I envision MUGI as an end product to be a computer vision based appliation made to assist athletes specifically martial artist in tracking form, biases, competetion analysis and feedback. Below you can find a ongoing log of my work , progress, topics learned, and personal thoughts.

__Work So Far(2/10/24)__

- collect data in the form of artificially generated videos courtesy of infinityAI, self recorded videos as well as well as imagees, and chopped up videos derived from youtube.
- store movements as timeseries in csv for consideration in training
- created a model pipeline to train on aftermentioned data

__Results (2/10/24)__

- Naive approach with pipeline yieled bad results when it comes to strikes.
   - two possibilities: need more data or approach is just plain wrong
- Naive approach with pipeline yields decent results when it comes to identifying excercises

__Learned (2/10/24)__

- How to create and work with pipelines
- extracting and cleaning data pertinant to task

__Next steps (2/10/24)__

- Get more familiar with Timeseries
- Pivot approach to RNN for strikes and simply collecting more data for compouind excercises 
- posssible approaches 
      - look at angles between joints instead of entire motion
      - identify 'positive' and 'negative' movement within action in question and train based on those criterias
  
   

