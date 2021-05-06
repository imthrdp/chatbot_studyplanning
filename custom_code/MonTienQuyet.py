# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def hoc_phan_tien_quyet(module):
    # Tên học phần
    module_code = {'QP001': 'Giáo dục Quốc phòng',
                   'TN033': 'Tin học căn bản',
                   'TN034': 'TT.Tin học căn bản',
                   'TN001': 'Vi – Tích phân A1',
                   'ML009': 'Những nguyên lý cơ bản của CN Mác-Lênin 1',
                   'CT101': 'Lập trình căn bản A',
                   'KL001': 'Pháp luật đại cương',
                   'TN010': 'Xác suất thống kê',
                   'TN012': 'Đại số tuyến tính & Hình học',
                   'XH023': 'Anh văn căn bản 1',
                   'XH004': 'Pháp văn căn bản 1',
                   'ML010': 'Những nguyên lý cơ bản của CN Mác-Lênin 2',
                   'TC001': 'Giáo dục thể chất 1, 2, 3',
                   'CT172': 'Toán rời rạc',
                   'CT103': 'Cấu trúc dữ liệu',
                   'TN002': 'Vi – Tích phân A2',
                   'XH024': 'Anh văn căn bản 2',
                   'XH005': 'Pháp văn căn bản 2',
                   'ML006': 'Tư tưởng Hồ Chí Minh',
                   'CT173': 'Kiến trúc máy tính',
                   'CT180': 'Cơ sở dữ liệu',
                   'CT174': 'Phân tích & thiết kế thuật toán',
                   'CT176': 'Lập trình hướng đối tượng',
                   'XH025': 'Anh văn căn bản 3',
                   'XH026': 'Pháp văn căn bản 3',
                   'ML011': 'Đường lối CM của ĐCSVN',
                   'CT178': 'Nguyên lý hệ điều hành',
                   'CT237': 'Nguyên lý hệ quản trị cơ sở dữ liệu',
                   'CT187': 'Nền tảng công nghệ thông tin',
                   'CT182': 'Ngôn ngữ mô hình hóa',
                   'CT183': 'Anh văn chuyên môn CNTT-1',
                   'CT175': 'Lý thuyết đồ thị',
                   'CT181': 'Hệ thống thông tin doanh nghiệp',
                   'CT184': 'Anh văn chuyên môn CNTT-2',
                   'CT112': 'Mạng máy tính',
                   'CT109': 'Phân tích & thiết kế HTTT',
                   'CT269': 'Hệ quản trị CSDL Oracle',
                   'CT236': 'Hệ quản trị CSDL trên Windows',
                   'CT311': 'Phương pháp nghiên cứu khoa học',
                   'CT332': 'Trí tuệ nhân tạo',
                   'CT171': 'Nhập môn công nghệ phần mềm',
                   'CT428': 'Lập trình Web',
                   'CT271': 'Niên luận cơ sở - CNTT',
                   'CT221': 'Lập trình mạng',
                   'CT202': 'Nguyên lý máy học',
                   'CT179': 'Quản trị hệ thống',
                   'ML007': 'Logic học đại cương',
                   'XH028': 'Xã hội học đại cương',
                   'XH014': 'Văn bản & lưu trữ đại cương',
                   'XH011': 'Cơ sở văn hóa Việt Nam',
                   'XH012': 'Tiếng Việt thực hành',
                   'CT335': 'Thiết kế & cài đặt mạng',
                   'CT466': 'Niên luận - CNTT',
                   'CT222': 'An toàn hệ thống',
                   'CT233': 'Điện toán đám mây',
                   'CT206': 'Phát triển ứng dụng trên Linux',
                   'CT251': 'Phát triển ứng dụng trên Windows',
                   'CT207': 'Phát triển phần mền mã nguồn mở',
                   'CT235': 'Quản trị mạng trên MS Windows',
                   'CT212': 'Quản trị mạng',
                   'CT450': 'Thực tập thực tế - CNTT',
                   'CT593': 'Luận văn tốt nghiệp – CNTT',
                   'CT468': 'Tiểu luận – CNTT',
                   'CT272': 'Thương mại điện tử - CNTT',
                   'CT273': 'Giao diện người – máy',
                   'CT338': 'Mạng không dây di động',
                   'CT274': 'Lập trình cho các thiết bị di động',
                   'CT223': 'Quản lý dự án phần mềm',
                   'CT211': 'An ninh mạng',
                   'CT275': 'Công nghệ Web',
                   'CT224': 'Công nghệ J2EE',
                   'CT231': 'Lập trình song song'}

    # Học phần tiên quyết của 'ML010' là 'ML009'
    modules_prerequisite = {'ML010': 'ML009',
                            'CT103': 'CT101',
                            'TN002': 'TN001',
                            'XH024': 'XH023',
                            'XH005': 'XH004',
                            'ML006': 'ML010',
                            'CT180': 'CT103',
                            'CT174': 'CT103',
                            'CT176': 'CT101',
                            'XH025': 'XH024',
                            'XH006': 'XH005',
                            'ML011': 'ML006',
                            'CT178': 'CT173',
                            'CT183': 'XH025',
                            'CT175': 'CT103',
                            'CT184': 'CT183',
                            'CT112': 'CT178',
                            'CT109': 'CT180',
                            'CT271': '>=80TC',
                            'CT221': 'CT112',
                            'CT335': 'CT112',
                            'CT466': '>=100TC',
                            'CT233': 'CT112',
                            'CT206': ['CT176', 'CT180'],
                            'CT251': ['CT176', 'CT180'],
                            'CT207': 'CT101',
                            'CT235': 'CT112',
                            'CT212': 'CT112',
                            'CT450': '>=120TC',
                            'CT593': '>=120TC',
                            'CT468': '>=120TC',
                            'CT274': 'CT176',
                            'CT223': 'CT171',
                            'CT224': 'CT176'}

    try:
        result = 'Học phần tiên quyết của học phần {0} là học phần {1}'.format(module_code[module], module_code[
            modules_prerequisite[module]])
        return result
    except BaseException:
        try:
            result = 'Học phần tiên quyết của môn ' + module_code[module] + ' là các học phần sau đây:'
            for mod in modules_prerequisite[module]:
                result = result + '\n' + module_code[mod]
            return result
        except BaseException:
            try:
                result = 'Điều kiện tiên quyết của học phần {0} là tích lũy {1}'.format(module_code[module],
                                                                                        modules_prerequisite[
                                                                                            module])
                return result
            except BaseException:
                try:
                    result = 'Học phần {0} không có môn tiên quyết'.format(module_code[module])
                    return result
                except BaseException:
                    result = 'Không tồn tại học phần {0} trong kế hoạch học tập cho sinh viên CNTT'.format(
                        module)
                    return result
    return result


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
    # print(hoc_phan_tien_quyet('QP001'))
    # print(hoc_phan_tien_quyet('TN033'))
    # print(hoc_phan_tien_quyet('TN034'))
    # print(hoc_phan_tien_quyet('TN001'))
    # print(hoc_phan_tien_quyet('ML009'))
    # print(hoc_phan_tien_quyet('CT101'))
    # print(hoc_phan_tien_quyet('KL001'))
    # print(hoc_phan_tien_quyet('TN010'))
    # print(hoc_phan_tien_quyet('TN012'))
    # print(hoc_phan_tien_quyet('XH023'))
    # print(hoc_phan_tien_quyet('XH004'))
    # print(hoc_phan_tien_quyet('ML010'))
    # print(hoc_phan_tien_quyet('TC001'))
    # print(hoc_phan_tien_quyet('CT172'))
    # print(hoc_phan_tien_quyet('CT103'))
    # print(hoc_phan_tien_quyet('TN002'))
    # print(hoc_phan_tien_quyet('XH024'))
    # print(hoc_phan_tien_quyet('XH005'))
    # print(hoc_phan_tien_quyet('ML006'))
    # print(hoc_phan_tien_quyet('CT173'))
    # print(hoc_phan_tien_quyet('CT180'))
    # print(hoc_phan_tien_quyet('CT174'))
    # print(hoc_phan_tien_quyet('CT176'))
    # print(hoc_phan_tien_quyet('XH025'))
    # print(hoc_phan_tien_quyet('XH026'))
    # print(hoc_phan_tien_quyet('ML011'))
    # print(hoc_phan_tien_quyet('CT178'))
    # print(hoc_phan_tien_quyet('CT237'))
    # print(hoc_phan_tien_quyet('CT187'))
    # print(hoc_phan_tien_quyet('CT182'))
    # print(hoc_phan_tien_quyet('CT183'))
    # print(hoc_phan_tien_quyet('CT175'))
    # print(hoc_phan_tien_quyet('CT181'))
    # print(hoc_phan_tien_quyet('CT184'))
    # print(hoc_phan_tien_quyet('CT112'))
    # print(hoc_phan_tien_quyet('CT109'))
    # print(hoc_phan_tien_quyet('CT269'))
    # print(hoc_phan_tien_quyet('CT236'))
    # print(hoc_phan_tien_quyet('CT311'))
    # print(hoc_phan_tien_quyet('CT332'))
    # print(hoc_phan_tien_quyet('CT171'))
    # print(hoc_phan_tien_quyet('CT428'))
    # print(hoc_phan_tien_quyet('CT271'))
    # print(hoc_phan_tien_quyet('CT221'))
    # print(hoc_phan_tien_quyet('CT202'))
    # print(hoc_phan_tien_quyet('CT179'))
    # print(hoc_phan_tien_quyet('ML007'))
    # print(hoc_phan_tien_quyet('XH028'))
    # print(hoc_phan_tien_quyet('XH014'))
    # print(hoc_phan_tien_quyet('XH011'))
    # print(hoc_phan_tien_quyet('XH012'))
    # print(hoc_phan_tien_quyet('CT335'))
    # print(hoc_phan_tien_quyet('CT466'))
    # print(hoc_phan_tien_quyet('CT222'))
    # print(hoc_phan_tien_quyet('CT233'))
    # print(hoc_phan_tien_quyet('CT206'))
    # print(hoc_phan_tien_quyet('CT251'))
    # print(hoc_phan_tien_quyet('CT207'))
    # print(hoc_phan_tien_quyet('CT235'))
    # print(hoc_phan_tien_quyet('CT212'))
    # print(hoc_phan_tien_quyet('CT450'))
    # print(hoc_phan_tien_quyet('CT593'))
    # print(hoc_phan_tien_quyet('CT468'))
    # print(hoc_phan_tien_quyet('CT272'))
    # print(hoc_phan_tien_quyet('CT273'))
    # print(hoc_phan_tien_quyet('CT338'))
    # print(hoc_phan_tien_quyet('CT274'))
    # print(hoc_phan_tien_quyet('CT223'))
    # print(hoc_phan_tien_quyet('CT211'))
    # print(hoc_phan_tien_quyet('CT275'))
    # print(hoc_phan_tien_quyet('CT224'))
    # print(hoc_phan_tien_quyet('CT231'))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
