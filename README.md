
create New virtual Environment
''' bash
Conda create -n wineQA python=3.9 -y
'''

Activate virtual Environment
''' bash
Conda activate wineQA 
'''

Created a requirements.txt file

install the requirements.txt file
''' bash
pip install -r requirements.txt

download data from 
https://drive.google.com/drive/folders/18zqQiCJVgF7uzXgfbIJ-04zgz1ItNfF5?usp=sharing

Pushing code and data to remote repository
git init

dvc init

dvc add data_given/winequality.csv --  Ensures data is not uploaded to git

git add .

git commit -m

dvc repro: this runs the stages in the dvc.yaml file.It checks if the content in the dependecies have changed

dvc metrics show: This shows the list of your hyper parameters and its metrics
dvc metrics diff: This shows the difference between various paramters and metrics