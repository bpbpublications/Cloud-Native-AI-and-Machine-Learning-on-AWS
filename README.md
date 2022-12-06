# Cloud Native AI and Machine Learning on AWS

This repo is a companion to the book **Cloud Native AI and Machine Learning on AWS, by BPB Publications** available for purchase both as a print version and an e-book here https://bpbonline.com/, <>

The absorption of ML and AI into existing business processes is pretty successful. Data professionals and cloud engineers are eyeing solutions with cloud migration as part of the digital transformation strategy. This book will present the readers with how data developers, data scientists, and cloud engineers can seamlessly drive the entire ML and AI on AWS, making maximum use of various AWS machine learning and AI services. In this book, we will create data lakes, prepare and train ML models, automate MLOps, prepare for maximum data reusability and reproducibility, and various other tasks of successful AI deployments.

This book covers use-cases demonstrating effective use of AWS AI/ML services. Readers will learn to leverage massive scale computing, manage large data lakes, train ML and AI models, deploy them into production, and monitor the performance of ML applications. The book also covers how readers can use the pre-trained models across various applications such as image recognition, automated data extraction, detection of images/videos, identifying anomalies, and more. Throughout the book, we use AWS capabilities such as Amazon SageMaker, Amazon AI Services, frameworks such as Pytorch or TensorFlow.
This book is divided into 12 chapters across three parts, namely **Part 1 - Know your data**, **Part 2 - Whose model is it anyway**, and **Part 3 - To API or not to API**. The first 4 chapters belong to Part 1, chapters 5 to 9 cover Part 2, and the remaining chapters cover Part 3. You will first read how ML and AI evolved in the last two decades, understand the foundational concepts of computational learning, and dive deep into what a ML workflow is and how the various stages in the workflow come together to help design, build and deploy a reliable, scalable and efficient solution to meet the most popular requirements for AI and ML today. You will learn by doing, and will be walking through python code samples, Jupyter notebooks, the AWS Management Console and APIs to build your solution through the various stages of the ML workflow. The chapter details are listed below.

**Chapter 1** covers the evolution of ML and AI in the last couple of decades, and an introduction to the ML workflow that enterprises use today to build world-class ML applications. We will follow this with an introduction to the AWS AI/ML stack and briefly delve into some of the major services that address key stages of the ML workflow. These are the services that we will cover in the rest of this book.

**Chapter 2** will introduce the importance of data and its role in building ML applications. We will learn why “data is the new oil” and learn to leverage data to unleash the tremendous potential in using ML to transform enterprises. We will look at the various ways data can be collected, harvested, curated and stored in a S3 Data Lake in AWS, the different options to analyze and make sense of the data, and finally prepare it for ML training and inference. We will follow step by step instructions in executing these tasks using easy to follow python code examples, Amazon SageMaker Jupyter notebooks, AWS Lambda and more.

**Chapter 3** covers one of the most important aspects of designing a ML solution which is feature engineering. Features define the inputs and the output of the ML model and will have to be considered very carefully as they can directly influence the success of the model predictions. In this chapter, you will learn what features are, why they are important, how to select the features that matter, and different techniques for collection, preparation and usage. We will learn with comprehensive coding examples, how to apply feature engineering techniques for different ML domains and problem types. Finally, we will use AWS Glue to automate the feature engineering tasks.

**Chapter 4** covers how to build a highly optimized collection of data pipelines using a combination of analytics and ML to harvest what we need for model training at scale but without the overhead of having to deal with large data volumes. We will show you with coding instructions how to build your own data pipelines for different types of ML use cases.

**Chapter 5** discusses choices in algorithm selection when designing ML models. If you want to run deep learning you use neural networks but that’s not a given. So, what are algorithms and neural nets? And how do you decide what to use? Why? What’s the difference between the two anyway? Learn how to build powerful predictive models harnessing the power of Math and Science with detailed code examples in this chapter.   

**Chapter 6** will cover model training. By this time in the book, you know your ML problem, you know your data, you have decided what type of training you need to do and have the algorithm or the neural net ready. It’s now time to see what happens when the rubber hits the road. For your specific ML problem, you first have to define the metric you have to evaluate your model against, and then iterate through a combination of model training and tuning to reach or exceed that metric. In this chapter, we will see with actual code examples how to build, train, tune, and evaluate your ML model using Amazon SageMaker, Jupyter notebooks and Python code samples.

**Chapter 7** will cover AutoML techniques including advanced ML automation that is in high demand and becoming increasingly mainstream using Amazon SageMaker Autopilot and Amazon SageMaker Canvas. You will learn how to use SageMaker Canvas with its point and click visual interface and SageMaker Autopilot under the hood to automate the entire ML workflow all at the click of a button. We will also spend some time reviewing the notebooks automatically generated by SageMaker Autopilot to understand how the ML workflow was executed.  

**Chapter 8** covers model deployment strategies. By this time, you have already completed model training and are ready to use it to make predictions. You will learn how to predict at scale in real-time and also run batch predictions for high volume accumulated datasets. You will understand what needs to be considered when making deployment decisions, and what are some of the cloud- based deployment strategies to maximize efficiency and minimize costs.

**Chapter 9** covers model inference design and implementation. You will learn considerations for how your model endpoint will be used, what is the scale it needs to support, and how you can build containers with model libraries to serve inference requests. You will learn how to do all of this in the most cost-effective way and at scale.

**Chapter 10** covers sensory cognition AWS AI services. By this time in the book, you would have gained comprehensive knowledge and experience in building and deploying powerful ML models that operate at massive scale to solve diverse challenges across industries. In this chapter we will pivot from ML to AI to understand how we can leverage the AWS AI services. Using just an API call that provides ready-made intelligence for a variety of common use cases, we will build end-to-end solutions in a fraction of the time it took us to build ML workflows on our own.

**Chapter 11** covers AWS AI services for industrial automation. You now understand how to use AWS AI service API calls to run powerful models for common sensory cognition use cases, and you will continue in this chapter to explore some of these AI services that are hugely popular in the area of industrial automation specifically in predictive maintenance, and time series forecasting

**Chapter 12** covers MLOps. You are now an expert in knowing and applying AI/ML with AWS for your enterprise use cases. You know how to approach, design, build and deploy AI and ML solutions. But perhaps the most important step is learning how to prepare it for production deployment, and setting up an automated CI/CD pipeline for faster go-to-market cycles across your business analyst, development, data scientist and operations team. In this chapter we will use Amazon SageMaker pipelines and the SageMaker data science SDK to learn how to build end-to-end MLOps pipelines and in the process also learn some best practices for ML model development and deployment.

## About the Authors

**Premkumar Rangarajan** is a Principal AI/ML specialist solutions architect at Amazon Web Services and has previously authored the book Natural Language Processing with AWS AI services. He has 26 years of experience in the IT industry in a variety of roles, including delivery lead, integration specialist, and enterprise architect. He helps enterprises of all sizes adopt AI and ML, and in his spare time dabbles as a guest lecturer helping students shape their careers. He can be reached at https://www.linkedin.com/in/premkr/

**David Bounds** is a Senior Solutions Architect at Amazon Web Services based out of Atlanta, Georgia.  With more than 25 years in IT ranging from front-line support to Site Reliability Engineering, David has a focus on operationalization of workloads.  He has an unrelenting passion for bringing AI/ML tools and capabilities to engineers of all experience levels and backgrounds.  When he is not iterating over haiku-generation models, he runs, works on his 3-D printer, or watches movies with his boxer, Darby.  He is preferential to action movies. He can be reached at https://www.linkedin.com/in/davidbbounds/
