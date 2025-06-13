# rule_based_chatbot.py

# Bắt đầu chatbot - Lời chào
user_input = input("Hãy chat gì đó với tôi: ").lower().strip()

# Chào người dùng
if user_input == "hi":
    print("Xin chào quý khách! Tôi có thể giúp gì cho quý khách?")
elif user_input == "hello":
    print("Xin chào, bạn cần tôi giúp gì không?")
    print("---------------------------------------------------------------------")
else:
    print("---------------------------------------------------------------------")
    print(f"Tôi chưa hiểu câu hỏi '{user_input}', nhưng tôi có thể hỗ trợ bạn.")

print("[Tư vấn mua hàng, Tra cứu bảo hành, Hỗ trợ kỹ thuật]")

# Chọn chức năng chính
main_choice = input("Vui lòng chọn một trong các mục trên: ").lower().strip()

# Nếu chọn sai, yêu cầu nhập lại
if main_choice not in ["tư vấn mua hàng", "tra cứu bảo hành", "hỗ trợ kỹ thuật"]:
    print("Chức năng bạn chọn không có trong danh sách.")
    print("---------------------------------------------------------------------")
    print("Tôi có thể giúp bạn với các chức năng sau:")
    print("---------------------------------------------------------------------")
    print("[Tư vấn mua hàng, Tra cứu bảo hành, Hỗ trợ kỹ thuật]")
    print("---------------------------------------------------------------------")
    main_choice = input("Vui lòng chọn lại: ").lower().strip()
    print("Chức năng của bạn hiện chưa được triển khai. Hẹn gặp bạn lần sau")

# -------------------------------------------
# Tư vấn mua hàng
if main_choice == "tư vấn mua hàng":
    print("Quý khách muốn mua sản phẩm nào ạ?")
    print("[Điện thoại, Laptop, Máy tính bảng]")
    print("---------------------------------------------------------------------")
    product = input("Nhập lựa chọn: ").lower().strip()

    if product == "điện thoại":
        print("Bạn đã chọn mua Điện thoại.")
    elif product == "laptop":
        print("Bạn đã chọn mua Laptop.")
    elif product == "máy tính bảng":
        print("Bạn đã chọn mua Máy tính bảng.")
    else:
        print("Sản phẩm không hợp lệ hoặc đã hết hàng.")

    more = input("Bạn có muốn mua thêm sản phẩm nào không? (có/không): ").lower().strip()
    if more == "có":
        print("Vui lòng chọn thêm sản phẩm:")
        print("[Điện thoại, Laptop, Máy tính bảng]")
        product2 = input("Nhập lựa chọn: ").lower().strip()

        if product2 == "điện thoại":
            print("Bạn đã chọn mua thêm Điện thoại.")
        elif product2 == "laptop":
            print("Bạn đã chọn mua thêm Laptop.")
        elif product2 == "máy tính bảng":
            print("Bạn đã chọn mua thêm Máy tính bảng.")
        else:
            print("Sản phẩm không hợp lệ hoặc đã hết hàng.")
        print("Cảm ơn quý khách đã mua hàng!")
    else:
        print("Cảm ơn quý khách đã mua hàng!")

# -------------------------------------------
# Tra cứu bảo hành
elif main_choice == "tra cứu bảo hành":
    print("Quý khách tra cứu bằng thông tin nào ạ?")
    print("[Số điện thoại, Số seri]")
    info = input("Nhập lựa chọn: ").lower().strip()

    if info == "số điện thoại":
        phone = input("Nhập số điện thoại của bạn: ").strip()
        print(f"Bạn đã tra cứu bằng Số điện thoại: {phone}")
        print("---------------------------------------------------------------------")
        print("Sau đây là thông tin bạn cần: [Thông tin bảo hành ở đây]")
    elif info == "số seri":
        seri = input("Nhập số seri sản phẩm: ").strip()
        print(f"Bạn đã tra cứu bằng Số seri: {seri}")
        print("---------------------------------------------------------------------")
        print("Sau đây là thông tin bạn cần: [Thông tin bảo hành ở đây]")
    else:
        print("Thông tin tra cứu không hợp lệ.")

    more = input("Bạn có muốn tra cứu thêm không? (có/không): ").lower().strip()
    if more == "có":
        print("Quý khách tra cứu bằng thông tin nào ạ?")
        print("[Số điện thoại, Số seri]")
        info2 = input("Nhập lựa chọn: ").lower().strip()

        if info2 == "số điện thoại":
            phone2 = input("Nhập số điện thoại: ").strip()
            print(f"Bạn đã tra cứu bằng Số điện thoại: {phone2}")
            print("---------------------------------------------------------------------")
            print("Sau đây là thông tin bạn cần: [Thông tin bảo hành ở đây]")
        elif info2 == "số seri":
            seri2 = input("Nhập số seri: ").strip()
            print(f"Bạn đã tra cứu bằng Số seri: {seri2}")
            print("---------------------------------------------------------------------")
            print("Sau đây là thông tin bạn cần: [Thông tin bảo hành ở đây]")
        else:
            print("Thông tin tra cứu không hợp lệ.")
    print("Cảm ơn quý khách đã sử dụng dịch vụ bảo hành!")

# -------------------------------------------
# Hỗ trợ kỹ thuật
elif main_choice == "hỗ trợ kỹ thuật":
    print("Quý khách cần hỗ trợ Cài đặt hay Sửa chữa ạ?")
    print("[Cài đặt, Sửa chữa]")
    support = input("Nhập lựa chọn: ").lower().strip()

    if support == "cài đặt":
        print("Bạn đã chọn hỗ trợ Cài đặt.")
    elif support == "sửa chữa":
        print("Bạn đã chọn hỗ trợ Sửa chữa.")
    else:
        print("Lựa chọn không hợp lệ.")

    more = input("Bạn có cần hỗ trợ kỹ thuật gì thêm không? (có/không): ").lower().strip()
    if more == "có":
        print("Vui lòng chọn lại:")
        print("[Cài đặt, Sửa chữa]")
        support2 = input("Nhập lựa chọn: ").lower().strip()

        if support2 == "cài đặt":
            print("Bạn đã chọn thêm hỗ trợ Cài đặt.")
        elif support2 == "sửa chữa":
            print("Bạn đã chọn thêm hỗ trợ Sửa chữa.")
        else:
            print("Lựa chọn không hợp lệ.")
    print("Cảm ơn quý khách đã sử dụng dịch vụ kỹ thuật!")
