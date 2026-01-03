
# Real-Time Wild Animal Detection and Alert System Using Machine Learning

## Project Overview
Wild animal intrusion into human settlements is a serious issue in forest-covered regions like Wayanad, Kerala, leading to loss of human life, crop damage, and economic loss. Existing solutions such as electric fencing are often ineffective and unsafe.

This project implements a real-time automated system that detects wild animals using computer vision and deep learning, triggers species-specific deterrent responses, and sends instant alerts to concerned authorities.

## Objectives
- Detect wild animals (Elephant, Tiger, Wild Boar) from video input in real-time
- Trigger species-specific sound and light deterrents upon detection
- Send automated alerts via WhatsApp/SMS to authorized personnel
- Reduce human-animal conflict using a non-harmful, automated system

## Technical Implementation
- **Programming Language**: Python 3.8+
- **Deep Learning Model**: YOLOv8 (Ultralytics implementation)
- **Machine Learning Approach**: Supervised Learning with Transfer Learning
- **Detection Framework**: Real-time object detection using PyTorch backend

## System Architecture
1. **Video Input Capture**: OpenCV processes live video feed
2. **Object Detection**: YOLOv8 model processes frames for animal detection
3. **Response Trigger**: 
   - Species-specific deterrent activation (sound/light)
   - Alert notification via Twilio API
4. **Alert Management**: One-time alert per video to prevent notification spam

## Animal Classes Detected
The system is trained to detect three primary wildlife species:
- Elephant
- Tiger  
- Wild Boar

## Dataset
- **Source**: Roboflow Public Dataset (CC BY 4.0 License)
- **Total Images**: Approximately 1,800 labeled images
- **Split Ratio**: 70% Training, 20% Validation, 10% Testing
- **Annotation Format**: YOLOv8 compatible bounding boxes

## Deterrent System
| Animal      | Sound Response      | Light Response        |
|-------------|---------------------|----------------------|
| Elephant    | Drum / Bee sounds   | Red + White strobe   |
| Tiger       | Siren / Dog bark    | White strobe         |
| Wild Boar   | Alarm sound         | White + Green strobe |

*Deterrent responses are based on documented animal behavior studies and are non-harmful.*

## Alert System
- **Platform**: Twilio API for WhatsApp/SMS delivery
- **Behavior**: Single alert per video session to avoid notification overload
- **Content**: Includes detected animal name and confidence score
- **Recipients**: Configurable list of authorized contacts

## Model Performance
- **Precision**: ~89%
- **Recall**: ~85%
- **Mean Average Precision (mAP)**: ~88%
- **Training**: 11-100 epochs using transfer learning from COCO pretrained weights

## Technical Features
- **Real-time Processing**: 15-30 FPS depending on hardware
- **Low-light Handling**: Brightness enhancement and histogram equalization
- **Modular Design**: Separate modules for detection, deterrents, and alerts
- **Configuration Management**: Environment variables for API keys and settings

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- Git

### Installation Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/wild-animal-detection.git
   cd wild-animal-detection
Install dependencies:

bash

pip install -r requirements.txt

Configure environment variables:


Copy .env.example to .env


Add your Twilio API credentials:

text

TWILIO_ACCOUNT_SID=your_account_sid

TWILIO_AUTH_TOKEN=your_auth_token

TWILIO_FROM=your_twilio_number

TWILIO_TO=target_phone_number

Download the dataset (if training):

Visit: https://universe.roboflow.com/hbz-syqzm/tiger-elephant-boar

Download in YOLOv8 format

Extract to data/roboflow_dataset/

Running the System

bash

python src/detection.py

Project Structure

text

wild-animal-detection/

├── src/                    # Source code

│   ├── detection.py       # Main detection script

│   ├── alert_system.py    # Twilio alert integration

│   └── deterrents.py      # Sound/light deterrent controls

├── data/                  # Dataset documentation

│   └── README.md          # Dataset instructions

├── models/                # Trained model weights

├── requirements.txt       # Python dependencies

├── .env.example          # Environment template

├── .gitignore            # Git ignore rules

└── README.md             # This file

**Limitations**

Night detection accuracy requires additional training on infrared/thermal datasets

Limited to three animal classes in current implementation

Dependent on camera quality and environmental conditions

Twilio free tier has message limits

**Future Enhancements**

Integration with thermal/IR cameras for night detection

Mobile application dashboard for real-time monitoring

Hardware deployment using Raspberry Pi with connected deterrent devices

Multi-camera support with cloud-based processing

GPS-based location tagging in alerts

**Academic Context**

This project was developed as part of the Master of Computer Applications (MCA) program, demonstrating practical application of machine learning and computer vision concepts to real-world environmental challenges.

**Testing & Validation**

The system has been validated on sample wildlife videos with the following outcomes:

Correct animal detection and species identification

Appropriate deterrent activation based on detected species

Successful alert delivery via configured channels

No false positives for non-target animals/objects

**License**

This project is available for academic and educational purposes. The dataset used is licensed under CC BY 4.0.

**Contact**

For questions or collaboration inquiries, please contact:

Name: Shaheer Ali S B

Email: alishaheer272002@gmail.com

GitHub: https://github.com/shaheer-ali-sb

Last Updated: December 2025

