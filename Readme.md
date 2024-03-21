# AAI Labs Data Science Task

This task contains jupyter notebook and flask-api for data analysis.

## 1. Jupyter Notebook Part

All notebooks related to data analysis are stored in the `notebooks` folder.

### Analysis Notebook

The main analysis notebook is named `analysis_notebook.ipynb`. This notebook contains tasks related to data analysis.

To run the cells in this notebook:

make sure to install python in your machine and run below commands in your termninal

1. `pip install notebook`

2. Navigate to the `notebooks` folder and open `analysis_notebook.ipynb`.

3. Install required libraries:
run below command in your termninal
- `pip install pandas numpy matplotlib scikit-learn`

4. Run cells in the notebook
- Remember to run the cells in order, as earlier cells may define variables used in subsequent ones.

5. All the outputs from the notebook will be saved in the outputs folder E.g PNG files

## 2. HTTP API development Part
All files related to the task are stored in the `web ` folder.

### API development

All the endpoints are found in `app.py` file. This files contains endpoint related to predicting GDP per capita for each continens.

To run the file:

make sure to install python in your machine and run below commands in your termninal

1. `pip install flask`

2. Navigate to the `web` folder and open `app.py`.

3. Run file by
run below command in your terminal
- `python app.py`
and the server will run then go to localhost:8000/predict_gdp by using postman to test the endpoint.

- When we test the endpoints, it should be based in the order of top features that are produced in the analysis_notebook file in the 6th cell for each continent

- For example to test for europe, we should provide our json like below, only using WEO subject codes 
`{
    "LE": 0,
    "NGSD_NGDP": 15.746,
    "PCPIEPCH": 3,
    "PCPIPCH": 2.93,
    "TM_RPCH": 4.355,  
    "continent": "Europe"
}`

4. The test file is found in the web folder and the file name is test.py.
To run the test file, run below code to the terminal
`python test.py`