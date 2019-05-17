# Stock-inquiry-robot
This program can be used to query information about stocks.<br>
You can open "stock inquery robot.mp4" to see what is look like when the program is running.<br>
And "chaboot_data.py" is the main program file.<br>
You can also open "MIT Remote Research Report.pdf" or "MIT Remote Research Report.docx" to see the details of the whole project, either of them is my report.<br>

![image](https://github.com/chesschan/Stock-inquiry-robot/blob/master/stock%20inquery%20robot.gif)<br>
## Installation Instructions
There are few online packages need to be installed for this project<br>

### Python
My python version is "python 3.6.6".<br>
You can install python 3.6.6 from https://www.python.org/downloads/<br>

### sklearn_crfsuite
You can install "sklearn_crfsuite" by running the code below:<br>
pip install sklearn_crfsuite<br>

### Install "requeirment.txt"
You can install this file by running the following code:<br>
pip install -r requeirment.txt<br>

### Rasa-NLU
#### Prerequisites
Make sure the Microsoft VC++ Compiler is installed, so python can compile any dependencies. You can get the compiler from: https://visualstudio.microsoft.com/visual-cpp-build-tools/<br>
Download the installer and select VC++ Build tools in the list.<br>

Setting up Rasa NLU<br>

#### Stable (Recommended)
The recommended way to install Rasa NLU is using pip which will install the latest stable version of Rasa NLU:<br>

pip install rasa_nlu<br>
#### Latest (Most recent github)
If you want to use the bleeding edge version you can get it from github:<br>

git clone https://github.com/RasaHQ/rasa_nlu.git<br>
cd rasa_nlu<br>
pip install -r requirements.txt<br>
pip install -e .<br>

Rasa NLU has different components for recognizing intents and entities, most of these will have some additional dependencies. When you train your model, Rasa NLU will check if all required dependencies are installed and tell you if any are missing.<br>

#### For more installation information
Go to https://rasa.com/docs/nlu/installation/<br>

### iexfinance
Setting up iexfinance<br>
#### From PyPI with pip (latest stable release):
$ pip3 install iexfinance<br>
#### From development repository (dev version):
If you want to use the bleeding edge version you can get it from github:<br>

$ git clone https://github.com/addisonlynch/iexfinance.git
$ cd iexfinance<br>
$ python3 setup.py install<br>
For more installation information Go to https://github.com/addisonlynch/iexfinance<br>

### spacy
#### Setting up iexfinance
conda install -c conda-forge spacy=2.0.11<br>
python -m spacy download en_core_web_md<br>
### wxpy
#### Setting up wxpy
wxpy support Python 3.4-3.6, and 2.7 version To ensure the package can be installed in different Python version Replace pip in the commond below to pip3 or pip2<br>

#### From PyPI with pip:
pip install -U wxpy<br>

#### For more installation information
Go to https://wxpy.readthedocs.io/zh/latest/#<br>

## operating instructions
1.Download all files in a same folder.<br>
2.You run the file called "chaboot_data.py".<br> 
3.An QR code will created automatically, use your Wechat to scan the QR code and log in.<br>
4.Now, your Wechat will turn to the Stock-inquery-robot, and others can inpuery stock information by chatting with you on Wechat.
