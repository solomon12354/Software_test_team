python -m venv venv
CALL .\venv\Scripts\activate
pip install -r requirement.txt
robot -d reports MovieTime.robot
deactivate