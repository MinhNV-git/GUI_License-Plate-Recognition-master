# License-Plate-Recognition
Phương pháp mình giới thiệu lần này bao gồm 4 bước: <br>

* Xác định vùng chứa biển số xe sử dụng **Yolo Tiny v3** 
* Sử dụng thuật toán segment để tách từng kí tự trên biển số xe
* Xây dựng một model CNN để phân loại các kí tự(characters classification)
* Định dạng lại biển số xe xác định biển số xe gồm một hay hai dòng.

## Install environments
* Cài python Python 3.7.6rc1 để có thể cài môi trường

* pip install -r requirements.txt

* python main.py --image_path=link_to_image 

* python main.py --image_path=C:\Users\Admin\Desktop\Giang\DoAn\Viblo\License-Plate-Recognition-master\samples\4_55378.jpg

Tuy nhiên, nó vẫn có một số nhược điểm::worried:

* Khi ảnh đầu vào bị đặt một góc quá nghiên thì một vài kí tự sẽ bị nhầm dòng. Có một cách giải quyết là dùng một mạng transformer xoay ảnh nghiêng về ảnh thẳng.
* Đôi khi bị nhận dạng nhầm giữa 8 và B, 0 và D
*  Hoạt động kém khi bức ảnh quá mờ

## Sử dụng GUI
   * Chọn btn 'Input' để chọn ảnh cần xử lý
   * Chọn btn 'Xử lý' để nhận diện biển số, chú ý chờ cho đến khi có ảnh hiện ở bên phải giao diện là ảnh đã được xử lý
