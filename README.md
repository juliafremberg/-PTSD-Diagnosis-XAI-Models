# PTSD-Diagnosis-XAI-Models
Project Description
PTSD-Diagnosis-XAI-Models is a comprehensive project aimed at developing machine learning models for detecting and diagnosing Post-Traumatic Stress Disorder (PTSD) using Explainable AI (XAI) techniques. The project focuses on addressing demographic imbalances through synthetic data generation and enhancing model transparency and performance. The project is organized into several key components, each contained within specific directories.

Subpopulation Filtering
This module is responsible for filtering the dataset to create subpopulations based on demographic attributes such as age and gender. By isolating these subpopulations, we ensure that the data used for training and evaluation accurately reflects the diversity of the target population. This step is crucial for understanding the specific characteristics of different demographic groups and mitigating biases in the dataset.

Preprocessing Data
The preprocessing data module handles the initial cleaning and preparation of the raw dataset. This involves standardizing text, removing inconsistencies, and extracting relevant features from the data. Preprocessing is a critical step to ensure that the data fed into the machine learning models is of high quality and suitable for analysis.

Cymo
The cymo directory includes tools and scripts from Exaia Technologies’ Cymo software, which is used for extracting and analyzing linguistic features from the dataset. Cymo provides advanced capabilities for feature extraction, enabling detailed analysis of the linguistic characteristics that distinguish PTSD-affected individuals from control groups.

Synthetic Data Generation
This module focuses on generating synthetic data to balance the representation of underrepresented groups within the dataset. By using advanced generative models, synthetic data is created to enhance the demographic diversity of the training set, thereby improving the fairness and accuracy of the machine learning models.

Shallow ML Model
The shallow-ml-model directory contains implementations of machine learning models with relatively simple architectures. These models serve as a baseline for comparison against more complex models. They are used to quickly test and validate various hypotheses and preprocessing steps, providing a foundation for further refinement.

Visualization
The visualization module includes scripts and tools for creating visual representations of the data and the results of the analysis. This can include charts, graphs, and other visual aids that help in interpreting the performance of the models and the effectiveness of the synthetic data generation. Visualization is key for communicating findings and ensuring the transparency of the model’s decisions.
