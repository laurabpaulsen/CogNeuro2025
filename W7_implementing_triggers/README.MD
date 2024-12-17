# Preparing your own experiment for EEG
The plan for today is to introduce triggers into your own experiments for EEG.

1. livecoding session, slowly building an experimental script similar to the one found in the [simple_visual/experiment.py](simple_visual/experiment.py) file. 
2. Begin implementing triggers into your own experiments taking inspiration from the code provided in this directory.


## Experiment checklist
- [ ] The experiment takes 10-15 minutes to run
- [ ] All the paths are relative to the script running the experiment (See this [link](https://desktop.arcgis.com/en/arcmap/10.6/tools/supplement/pathnames-explained-absolute-relative-unc-and-url.htm) for further explanation)
- [ ] All paths are defined using `os` or `Pathlib`ensure that the correct slash is used to separate directory names based on the operating system. See example below:
    ```python
    import os

    savepath = os.path.join("data", "behavioural_data.csv")
    image_sad_path = os.path.join("stimuli", "sad_face.png")
    ```

- [ ] All necessary files for the experiment are in a single folder, either on GitHub or on a USB stick for easy download to the experimental computer
- [ ] The triggers used are between 1 and 256 (trigger 0 does not work!!)
- [ ] The experiment contains many repetitions of each condition to allow averaging over many trials for analysis
- [ ] The triggers.py script must be at same path as your experimental script 
