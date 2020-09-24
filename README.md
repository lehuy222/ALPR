1. Kết quả
- Vehicle Detection: 
+ Accuracy > 95%
    + Vấn đề chưa xử lý: Chưa bắt được những frame ảnh chỉ chụp 1 phần đuôi xe, đặc biệt là xe máy
- Plate Detection: 
+ Accuracy > 95% trên data chụp ảnh xe cộ dưới hầm (1k4 ảnh), 80% trên data tổng hợp trên google (200 ảnh)
+ Vấn đề chưa xử lý: Không bắt được biển quá xa và thi thoảng fail với biển xe máy quá gần(biển chiếm hơn 30% ảnh)
- Plate classification: 
+ Accuracy > 98% với biển dài và >99% với biển vuông
+ Vấn đề chưa xử lý: Xử dụng phương pháp khác để xử lý biển 2 dòng bởi việc cắt đôi biển phụ thuộc hết vào ảnh Detect Plate.
- OCR: 
+ Accuracy: 91%
+ Vấn đề chưa xử lý: Thêm data để đạt kết quả cao hơn (Không có ký tự khó) 

