# rule_based_chatbox.py

# Bắt đầu chatbot - Lời chào + Vòng lặp chính

while True:
    # Chào người dùng
    user_input = input("Hãy chat gì đó với tôi: ").lower().strip()

    if user_input in ["thoát", "exit", "quit"]:
        print("Cảm ơn bạn đã trò chuyện. Hẹn gặp lại!")
        break

    # Chào người dùng
    if user_input == "hi":
        print("Xin chào quý khách! Tôi có thể giúp gì cho quý khách?")
    elif user_input == "hello":
        print("Xin chào, bạn cần tôi giúp gì không?")
    else:
        print(f"Tôi chưa hiểu câu hỏi '{user_input}', nhưng tôi có thể hỗ trợ bạn.")
    print("---------------------------------------------------------------------")
    print("[Tư vấn mua hàng, Tra cứu bảo hành, Hỗ trợ kỹ thuật, Thoát]")

    # Chọn chức năng chính (lặp lại đến khi hợp lệ hoặc thoát)
    while True:
        main_choice = input("Vui lòng chọn một trong các mục trên: ").lower().strip()

        if main_choice == "":
            print("Bạn chưa nhập chức năng nào. Vui lòng chọn lại.")
            continue
        elif main_choice in ["thoát", "exit", "quit"]:
            print("Cảm ơn bạn đã trò chuyện. Hẹn gặp lại!")
            exit()

        # -------------------------------------------
        # Tư vấn mua hàng
        elif main_choice == "tư vấn mua hàng":
            while True:
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
                if more != "có":
                    break
            print("Cảm ơn quý khách đã mua hàng!")
            print("---------------------------------------------------------------------")
            break

        # -------------------------------------------
        # Tra cứu bảo hành
        elif main_choice == "tra cứu bảo hành":
            while True:
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
                    continue

                more = input("Bạn có muốn tra cứu thêm không? (có/không): ").lower().strip()
                if more != "có":
                    break
            print("Cảm ơn quý khách đã sử dụng dịch vụ bảo hành!")
            print("---------------------------------------------------------------------")
            break

        # -------------------------------------------
        # Hỗ trợ kỹ thuật
        elif main_choice == "hỗ trợ kỹ thuật":
            while True:
                print("Quý khách cần hỗ trợ Cài đặt hay Sửa chữa ạ?")
                print("[Cài đặt, Sửa chữa]")
                support = input("Nhập lựa chọn: ").lower().strip()

                if support == "cài đặt":
                    print("Bạn đã chọn hỗ trợ Cài đặt.")
                elif support == "sửa chữa":
                    print("Bạn đã chọn hỗ trợ Sửa chữa.")
                else:
                    print("Lựa chọn không hợp lệ.")
                    continue

                more = input("Bạn có cần hỗ trợ kỹ thuật gì thêm không? (có/không): ").lower().strip()
                if more != "có":
                    break
            print("Cảm ơn quý khách đã sử dụng dịch vụ kỹ thuật!")
            print("---------------------------------------------------------------------")
            break

        # -------------------------------------------
        # Nhập sai chức năng
        else:
            print("Chức năng bạn chọn không có trong danh sách.")
            print("---------------------------------------------------------------------")
            print("Tôi có thể giúp bạn với các chức năng sau:")
            print("[Tư vấn mua hàng, Tra cứu bảo hành, Hỗ trợ kỹ thuật, Thoát]")
            print("---------------------------------------------------------------------")
