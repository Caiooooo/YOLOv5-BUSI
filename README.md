# Breast Image Ultrasound Image (BUSI) to YOLOv5 Pretrained Model

This repository contains the necessary scripts to preprocess Breast Image Ultrasound Images (BUSI) into a format suitable for training with YOLOv5. Additionally, it provides a pre-trained YOLOv5 model for detecting features in BUSI images.

## Getting Started

To get started, follow these steps:

### 1. Install Requirements

Make sure you have all the necessary dependencies installed. You can do this by running:

```bash
pip install -r requirements.txt
```

### 2. Data Preprocessing

Run the code provided in `data/train.ipynb` to preprocess the BUSI images into a format compatible with YOLOv5 training.

### 3. Start Training

Once the data preprocessing is complete, you can start training the YOLOv5 model using the preprocessed data. Refer to the YOLOv5 documentation for training instructions.

### 4. Evaluate and Fine-tune

After training, evaluate the model's performance and fine-tune as needed to achieve the desired results.

## Starting a Web Server

If you have access to the internet, you can also start a web server using the provided code in `WebStarter`. This can be useful for various purposes such as hosting the pre-trained model for inference or serving visualizations of the BUSI images.

## Contribution

Contributions are welcome! Feel free to submit issues or pull requests to improve this repository.

## License

This project is licensed under the [GNU Affero General Public License Version 3](LICENSE). Feel free to use and modify it according to your needs.