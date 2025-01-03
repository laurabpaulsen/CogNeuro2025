# Code for the EEG lab
This repository contains all the coding exercises for the EEG lab. All code was tested using Coder Python version 1.86.1 on uCloud. 

## Overview
This folder holds the notebooks to use during the EEG lab. Additionally, the following files are included:
- `setup_env.sh`: This is a bash script that sets up a virtual environment for the project. It installs the necessary packages and saves them in a folder called `env`.
- `env_to_jupyter.sh`: This is a bash script that installs the virtual environment as a kernel in Jupyter notebooks. This is necessary to be able to run the notebooks using the virtual environment.
- `requirements.txt`: This file lists the packages that are installed in the virtual environment.



## Setting up virtual environment
To avoid having to install the needed packages every time a new uCloud run is initialised, we will use a virtual environment. This is a way to create a Python environment that is independent of the system Python installation and it is saved in a folder, which means that you can just activate it everytime you start a new run.


Navigate to the `EEG_LAB` folder and run the following command in the terminal:

```
bash setup_env.sh
```

You will notice a new folder called `env` has been created. This is the virtual environment. To activate it, run the following command:

```
source env/bin/activate
```

This is useful when running .py scripts, but since we will be using Jupyter notebooks, we need to install the virtual environment as a kernel. To do this, run the following command:

```
bash env_to_jupyter.sh
```


## MNE tutorial - Monday

### 1. Create virtual environment
The first step today is to create a virtual environment. Follow the instruction in the [README.md](#setting-up-virtual-environment) file one step up in the EEG folder.

### 2. (Optional) Python brush-up
I have created a notebook with a few exercises to brush up on your Python skills. I have included things that I found especially relevant in terms of understanding the syntax used when working with EEG data using the `MNE-python` package. Additionally there is an introduction to working with 3-dimensional arrays in Numpy. I recommend you scroll through the notebook and determine determine whether you want to spend time on it or not.

The notebook is called [00-python_brush_up.ipynb](00-python_brush_up.ipynb) and is located in the this folder.

### 3. Preprocessing  EEG data
The next step is to preprocess EEG data, which we will go through using the [01-EEG_preprocessing.ipynb](01-EEG_preprocessing.ipynb) notebook. This notebook will guide you through the steps of loading EEG data and preprocessing it. I recommend you sit in small groups and talk through the exercises as you go along. 

Remember to ask questions if you get stuck or if you are unsure about something, either code or theory related. Additionally MNE has a very good [documentation](https://mne.tools/stable/index.html) that you can use to look up functions and methods. Getting familiar with the documentation is a good idea, as it is a big help if you choose to work with EEG data for your exam project.

### 4. Epoching the EEG data
After preprocessing the data, the next step is to epoch the data. This is done in the [02-EEG_epochs.ipynb](02-EEG_epochs.ipynb) notebook. 

### 5. Analysing EEG data (first steps)
The remainder of today should be spend going through the [03-EEG_analysis.ipynb](03-EEG_analysis.ipynb) notebook. This notebook will guide you through some of the first steps of analysing EEG data by plotting!

## Analysis of data from FaceWord experiment - Tuesday, Wednesday and Thursday
See assignment on Brightspace!


## Analysis of data from your own experiments - Friday

### 1. Preprocess and epoch your own data
The first step is to preprocess your own data. You can find inspiration in the notebooks from monday. Also note that loading in the data is a bit different, as you will have to load in your own data. You can use the following code:
```
# path to the data
path = "xxxxxxxxx.vhdr"

raw = mne.io.read_raw_brainvision(path, preload=True)
```

If you are stuck I have created skeleton notebook for another course that guides the preprocessing step by step. You can find it [here](https://github.com/laurabpaulsen/LaCoBra-E23/blob/main/EEG-analysis/EEG_analysis.ipynb).

#### Preprocessing checklist
- [ ] Load in the data
- [ ] Set the montage
- [ ] Remove bad channels
- [ ] Re-reference the data (common average reference)
- [ ] Filter the data
- [ ] Epoch the data 
    - [ ] Set the time window for the epochs
    - [ ] Identify the events
    - [ ] Baseline correction
    - [ ] Set a threshold for rejecting epochs
- [ ] Downsample the data


Additonal preprocessing could include ICA.



### 2. Sanity checks (optional)
After preprocessing the data, it is a good idea to do some sanity checks. Which sanity checks you can do depends on the experimental design of your experiment. However, some general ideas could be to:
* Check that there is a response when visual stimuli are presented by plotting the evoked response to visual stimuli (maybe focusing on the occipital electrodes)
* Check that there is a response when auditory stimuli are presented by plotting the evoked response to auditory stimuli.

Showing that there is a response to the stimuli is a good first step to show that the data is of reasonable quality, and that the preprocessing has been done correctly.

### 3. Comparing conditions (analysis and statistical tests)
After preprocessing the next step is to play around with analysis of your own data. I have preprocessed some data and made it available to you on uCloud for the purpose of demonstatring the three types of analysis. If you want to run the notebooks make sure to add the `EEG_lab` folder to your uCloud run. It is FaceWord data from last years EEG course from 3 participants. 

The idea is that you can use the notebooks in this folder as inspiration for your own analysis. Have a chat in the group about what analysis might be relevant for your data and research question. When you reach this point call Laura over to have a little chat about what you want to do and how to proceed!

The notebooks available are:

- **windowed_mean_subject_lvl.ipynb & windowed_mean_group_lvl.ipynb :** These notebooks introduce the concept of a windowed mean, where two conditions are compared by taking the mean of the signal in a certain time window in relevant sensors and comparing the means. This includes some basic plotting and statistical testing using a t-test.

- **clusterbased_permutation.ipynb:** This notebook shows how to do a cluster-based permutation test. 

- **decoding.ipynb:** This notebook shows how to do a decoding analysis using a linear discriminant analysis (LDA). Do not start of looking at this notebook! It is beyond the scope of the course, but if you conducted a windowed mean analysis and the permutation test, you can play around with it. The notebook introduces decoding both at individual time points, but also shows how to investigate the temporal generalisation of decoders trained at one time point and tested at another time points.


Note however, that there are many other ways to analyse your data - I am more than happy to brainstorm with you about what might be relevant for your data and research question. 






