🐘 Wildlife Detection Dataset
Source
Roboflow Public Dataset: tiger-elephant-boar

License: CC BY 4.0 (Creative Commons Attribution 4.0 International)

Dataset Details
Classes: Tiger, Elephant, Wild Boar

Format: YOLO format annotations

Split: Train/Valid/Test (pre-split by Roboflow)

📥 How to Download & Use
Option 1: Manual Download (Easiest)
Visit: https://universe.roboflow.com/hbz-syqzm/tiger-elephant-boar

Click "Download" button

Select "YOLO v8" format

Extract ZIP to data/roboflow_dataset/ folder

Option 2: Python API (Automated)
python
# Install: pip install roboflow
from roboflow import Roboflow

# Download dataset
rf = Roboflow(api_key="your-free-api-key")  # Get from Roboflow
project = rf.workspace("hbz-syqzm").project("tiger-elephant-boar")
dataset = project.version(1).download("yolov8")
🏗️ Folder Structure After Download
text
data/roboflow_dataset/
├── train/
│   ├── images/          # Training images
│   └── labels/          # YOLO annotation files (.txt)
├── valid/               # Validation images & labels
├── test/                # Test images & labels
└── data.yaml           # Dataset configuration file
🔧 Integration with This Project
After downloading, update your paths in code:

yaml
# In data.yaml or your config:
path: ./data/roboflow_dataset
train: train/images
val: valid/images
test: test/images
📝 License Compliance
✅ This dataset is publicly available under CC BY 4.0

✅ Attribution given to original uploader

✅ Commercial use allowed with attribution

✅ Modifications allowed with attribution

License Link: https://creativecommons.org/licenses/by/4.0/

⚠️ Note
The actual dataset files are NOT included in this repository due to size.
Users must download them from Roboflow using the instructions above.

Last Updated: December 2025 | MCA Final Year Project