# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

# from rasa.shared.core.events import Restarted
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
# from rasa_sdk.events import SlotSet
# from rasa_sdk.events import AllSlotsReset
import custom_code.MonTienQuyet
import custom_code.TenHocPhan
import custom_code.LoaiHocPhan
import custom_code.MaHocPhan


# Tên học phần
# ModulesCode = {'QP00*' : 'Giáo dục quốc phòng',
#                'TN033' : 'Tin học căn bản',
#                'TN034' : 'TT.Tin học căn bản',
#                'TN001' : 'Vi – Tích phân A1',
#                'ML009' : 'Những nguyên lý cơ bản của CN Mác-Lênin 1',
#                'CT101' : 'Lập trình căn bản A',
#                'KL001' : 'Pháp luật đại cương',
#                'TN010' : 'Xác suất thống kê',
#                'TN012' : 'Đại số tuyến tính & Hình học',
#                'XH023' : 'Anh văn căn bản 1',
#                'XH004' : 'Pháp văn căn bản 1',
#                'ML010' : 'Những nguyên lý cơ bản của CN Mác-Lênin 2',
#                'TC---' : 'Giáo dục thể chất 1, 2, 3',
#                'CT172' : 'Toán rời rạc',
#                'CT103' : 'Cấu trúc dữ liệu',
#                'TN002' : 'Vi – Tích phân A2',
#                'XH024' : 'Anh văn căn bản 2',
#                'XH005' : 'Pháp văn căn bản 2',
#                'ML006' : 'Tư tưởng Hồ Chí Minh',
#                'CT173' : 'Kiến trúc máy tính',
#                'CT180' : 'Cơ sở dữ liệu',
#                'CT174' : 'Phân tích & thiết kế thuật toán',
#                'CT176' : 'Lập trình hướng đối tượng',
#                'XH025' : 'Anh văn căn bản 3',
#                'XH006' : 'Pháp văn căn bản 3',
#                'ML011' : 'Đường lối CM của ĐCSVN',
#                'CT178' : 'Nguyên lý hệ điều hành',
#                'CT237' : 'Nguyên lý hệ quản trị cơ sở dữ liệu',
#                'CT187' : 'Nền tảng công nghệ thông tin',
#                'CT182' : 'Ngôn ngữ mô hình hóa ',
#                'CT183' : 'Anh văn chuyên môn CNTT-1',
#                'CT175' : 'Lý thuyết đồ thị',
#                'CT181' : 'Hệ thống thông tin doanh nghiệp',
#                'CT184' : 'Anh văn chuyên môn CNTT-2',
#                'CT112' : 'Mạng máy tính',
#                'CT109' : 'Phân tích & thiết kế HTTT',
#                'CT269' : 'Hệ quản trị CSDL Oracle',
#                'CT236' : 'Hệ quản trị CSDL trên Windows',
#                'CT311' : 'Phương pháp nghiên cứu khoa học',
#                'CT332' : 'Trí tuệ nhân tạo',
#                'CT171' : 'Nhập môn công nghệ phần mềm',
#                'CT428' : 'Lập trình Web',
#                'CT271' : 'Niên luận cơ sở - CNTT',
#                'CT221' : 'Lập trình mạng',
#                'CT202' : 'Nguyên lý máy học',
#                'CT179' : 'Quản trị hệ thống',
#                'ML007' : 'Logic học đại cương',
#                'XH028' : 'Xã hội học đại cương',
#                'XH014' : 'Văn bản & lưu trữ đại cương',
#                'XH011' : 'Cơ sở văn hóa Việt Nam',
#                'XH012' : 'Tiếng Việt thực hành',
#                'CT335' : 'Thiết kế & cài đặt mạng',
#                'CT466' : 'Niên luận - CNTT',
#                'CT222' : 'An toàn hệ thống',
#                'CT233' : 'Điện toán đám mây',
#                'CT206' : 'Phát triển ứng dụng trên Linux',
#                'CT251' : 'Phát triển ứng dụng trên Windows',
#                'CT207' : 'Phát triển phần mền mã nguồn mở',
#                'CT235' : 'Quản trị mạng trên MS Windows',
#                'CT212' : 'Quản trị mạng',
#                'CT450' : 'Thực tập thực tế - CNTT',
#                'CT593' : 'Luận văn tốt nghiệp – CNTT',
#                'CT468' : 'Tiểu luận – CNTT',
#                'CT272' : 'Thương mại điện tử - CNTT',
#                'CT273' : 'Giao diện người – máy',
#                'CT338' : 'Mạng không dây di động',
#                'CT274' : 'Lập trình cho các thiết bị di động',
#                'CT223' : 'Quản lý dự án phần mềm',
#                'CT211' : 'An ninh mạng',
#                'CT275' : 'Công nghệ Web',
#                'CT224' : 'Công nghệ J2EE',
#                'CT231' : 'Lập trình song song'}

# Loại học phần bắt buộc hoặc tự chọn
# ModulesType = {'QP00*' : 'Bắt buộc',
#                'TN033' : 'Bắt buộc',
#                'TN034' : 'Bắt buộc',
#                'TN001' : 'Bắt buộc',
#                'ML009' : 'Bắt buộc',
#                'CT101' : 'Bắt buộc',
#                'KL001' : 'Bắt buộc',
#                'TN010' : 'Bắt buộc',
#                'TN012' : 'Bắt buộc',
#                'XH023' : 'Tự chọn',
#                'XH004' : 'Tự chọn',
#                'ML010' : 'Bắt buộc',
#                'TC---' : 'Tự chọn',
#                'CT172' : 'Bắt buộc',
#                'CT103' : 'Bắt buộc',
#                'TN002' : 'Bắt buộc',
#                'XH024' : 'Tự chọn',
#                'XH005' : 'Tự chọn',
#                'ML006' : 'Bắt buộc',
#                'CT173' : 'Bắt buộc',
#                'CT180' : 'Bắt buộc',
#                'CT174' : 'Bắt buộc',
#                'CT176' : 'Bắt buộc',
#                'XH025' : 'Tự chọn',
#                'XH006' : 'Tự chọn',
#                'ML011' : 'Bắt buộc',
#                'CT178' : 'Bắt buộc',
#                'CT237' : 'Bắt buộc',
#                'CT187' : 'Bắt buộc',
#                'CT182' : 'Tự chọn ',
#                'CT183' : 'Tự chọn',
#                'CT175' : 'Bắt buộc',
#                'CT181' : 'Tự chọn',
#                'CT184' : 'Tự chọn',
#                'CT112' : 'Bắt buộc',
#                'CT109' : 'Bắt buộc',
#                'CT269' : 'Tự chọn',
#                'CT236' : 'Tự chọn',
#                'CT428' : 'Bắt buộc',
#                'CT271' : 'Bắt buộc',
#                'CT221' : 'Bắt buộc',
#                'CT202' : 'Bắt buộc',
#                'CT179' : 'Bắt buộc',
#                'ML007' : 'Tự chọn',
#                'XH028' : 'Tự chọn',
#                'XH014' : 'Tự chọn',
#                'XH011' : 'Tự chọn',
#                'XH012' : 'Tự chọn',
#                'CT335' : 'Bắt buộc',
#                'CT466' : 'Bắt buộc',
#                'CT222' : 'Bắt buộc',
#                'CT233' : 'Bắt buộc',
#                'CT206' : 'Tự chọn',
#                'CT251' : 'Tự chọn',
#                'CT207' : 'Tự chọn',
#                'CT235' : 'Tự chọn',
#                'CT212' : 'Tự chọn',
#                'CT450' : 'Bắt buộc',
#                'CT593' : 'Tự chọn',
#                'CT468' : 'Tự chọn',
#                'CT272' : 'Tự chọn',
#                'CT273' : 'Tự chọn',
#                'CT338' : 'Tự chọn',
#                'CT274' : 'Tự chọn',
#                'CT223' : 'Tự chọn',
#                'CT211' : 'Tự chọn',
#                'CT275' : 'Tự chọn',
#                'CT224' : 'Tự chọn',
#                'CT231' : 'Tự chọn'}
#
# Học phần tiên quyết của 'ML010' là 'ML009'
# ModulesPrerequisite =  {'ML010' : 'ML009',
#                'CT103' : 'CT101',
#                'TN002' : 'TN001',
#                'XH024' : 'XH023',
#                'XH005' : 'XH004',
#                'ML006' : 'ML010',
#                'CT180' : 'CT103',
#                'CT174' : 'CT103',
#                'CT176' : 'CT101',
#                'XH025' : 'XH024',
#                'XH006' : 'XH005',
#                'ML011' : 'ML006',
#                'CT178' : 'CT173',
#                'CT183' : 'XH025',
#                'CT175' : 'CT103',
#                'CT184' : 'CT183',
#                'CT112' : 'CT178',
#                'CT109' : 'CT180',
#                'CT271' : '>=80TC',
#                'CT221' : 'CT112',
#                'CT335' : 'CT112',
#                'CT466' : '>=100TC',
#                'CT233' : 'CT112',
#                'CT206' : ['CT176', 'CT180'],
#                'CT251' : ['CT176', 'CT180'],
#                'CT207' : 'CT101',
#                'CT235' : 'CT112',
#                'CT212' : 'CT112',
#                'CT450' : '>=120TC',
#                'CT593' : '>=120TC',
#                'CT468' : '>=120TC',
#                'CT274' : 'CT176',
#                'CT223' : 'CT171',
#                'CT224' : 'CT176'}

# def HocPhanTienQuyet(moduleCode):
#     # Tên học phần
#     ModulesCode = {'QP00*': 'Giáo dục quốc phòng',
#                    'TN033': 'Tin học căn bản',
#                    'TN034': 'TT.Tin học căn bản',
#                    'TN001': 'Vi – Tích phân A1',
#                    'ML009': 'Những nguyên lý cơ bản của CN Mác-Lênin 1',
#                    'CT101': 'Lập trình căn bản A',
#                    'KL001': 'Pháp luật đại cương',
#                    'TN010': 'Xác suất thống kê',
#                    'TN012': 'Đại số tuyến tính & Hình học',
#                    'XH023': 'Anh văn căn bản 1',
#                    'XH004': 'Pháp văn căn bản 1',
#                    'ML010': 'Những nguyên lý cơ bản của CN Mác-Lênin 2',
#                    'TC---': 'Giáo dục thể chất 1, 2, 3',
#                    'CT172': 'Toán rời rạc',
#                    'CT103': 'Cấu trúc dữ liệu',
#                    'TN002': 'Vi – Tích phân A2',
#                    'XH024': 'Anh văn căn bản 2',
#                    'XH005': 'Pháp văn căn bản 2',
#                    'ML006': 'Tư tưởng Hồ Chí Minh',
#                    'CT173': 'Kiến trúc máy tính',
#                    'CT180': 'Cơ sở dữ liệu',
#                    'CT174': 'Phân tích & thiết kế thuật toán',
#                    'CT176': 'Lập trình hướng đối tượng',
#                    'XH025': 'Anh văn căn bản 3',
#                    'XH006': 'Pháp văn căn bản 3',
#                    'ML011': 'Đường lối CM của ĐCSVN',
#                    'CT178': 'Nguyên lý hệ điều hành',
#                    'CT237': 'Nguyên lý hệ quản trị cơ sở dữ liệu',
#                    'CT187': 'Nền tảng công nghệ thông tin',
#                    'CT182': 'Ngôn ngữ mô hình hóa ',
#                    'CT183': 'Anh văn chuyên môn CNTT-1',
#                    'CT175': 'Lý thuyết đồ thị',
#                    'CT181': 'Hệ thống thông tin doanh nghiệp',
#                    'CT184': 'Anh văn chuyên môn CNTT-2',
#                    'CT112': 'Mạng máy tính',
#                    'CT109': 'Phân tích & thiết kế HTTT',
#                    'CT269': 'Hệ quản trị CSDL Oracle',
#                    'CT236': 'Hệ quản trị CSDL trên Windows',
#                    'CT311': 'Phương pháp nghiên cứu khoa học',
#                    'CT332': 'Trí tuệ nhân tạo',
#                    'CT171': 'Nhập môn công nghệ phần mềm',
#                    'CT428': 'Lập trình Web',
#                    'CT271': 'Niên luận cơ sở - CNTT',
#                    'CT221': 'Lập trình mạng',
#                    'CT202': 'Nguyên lý máy học',
#                    'CT179': 'Quản trị hệ thống',
#                    'ML007': 'Logic học đại cương',
#                    'XH028': 'Xã hội học đại cương',
#                    'XH014': 'Văn bản & lưu trữ đại cương',
#                    'XH011': 'Cơ sở văn hóa Việt Nam',
#                    'XH012': 'Tiếng Việt thực hành',
#                    'CT335': 'Thiết kế & cài đặt mạng',
#                    'CT466': 'Niên luận - CNTT',
#                    'CT222': 'An toàn hệ thống',
#                    'CT233': 'Điện toán đám mây',
#                    'CT206': 'Phát triển ứng dụng trên Linux',
#                    'CT251': 'Phát triển ứng dụng trên Windows',
#                    'CT207': 'Phát triển phần mền mã nguồn mở',
#                    'CT235': 'Quản trị mạng trên MS Windows',
#                    'CT212': 'Quản trị mạng',
#                    'CT450': 'Thực tập thực tế - CNTT',
#                    'CT593': 'Luận văn tốt nghiệp – CNTT',
#                    'CT468': 'Tiểu luận – CNTT',
#                    'CT272': 'Thương mại điện tử - CNTT',
#                    'CT273': 'Giao diện người – máy',
#                    'CT338': 'Mạng không dây di động',
#                    'CT274': 'Lập trình cho các thiết bị di động',
#                    'CT223': 'Quản lý dự án phần mềm',
#                    'CT211': 'An ninh mạng',
#                    'CT275': 'Công nghệ Web',
#                    'CT224': 'Công nghệ J2EE',
#                    'CT231': 'Lập trình song song'}
#     # Loại học phần bắt buộc hoặc tự chọn
#     ModulesType = {'QP00*': 'Bắt buộc',
#                    'TN033': 'Bắt buộc',
#                    'TN034': 'Bắt buộc',
#                    'TN001': 'Bắt buộc',
#                    'ML009': 'Bắt buộc',
#                    'CT101': 'Bắt buộc',
#                    'KL001': 'Bắt buộc',
#                    'TN010': 'Bắt buộc',
#                    'TN012': 'Bắt buộc',
#                    'XH023': 'Tự chọn',
#                    'XH004': 'Tự chọn',
#                    'ML010': 'Bắt buộc',
#                    'TC---': 'Tự chọn',
#                    'CT172': 'Bắt buộc',
#                    'CT103': 'Bắt buộc',
#                    'TN002': 'Bắt buộc',
#                    'XH024': 'Tự chọn',
#                    'XH005': 'Tự chọn',
#                    'ML006': 'Bắt buộc',
#                    'CT173': 'Bắt buộc',
#                    'CT180': 'Bắt buộc',
#                    'CT174': 'Bắt buộc',
#                    'CT176': 'Bắt buộc',
#                    'XH025': 'Tự chọn',
#                    'XH006': 'Tự chọn',
#                    'ML011': 'Bắt buộc',
#                    'CT178': 'Bắt buộc',
#                    'CT237': 'Bắt buộc',
#                    'CT187': 'Bắt buộc',
#                    'CT182': 'Tự chọn ',
#                    'CT183': 'Tự chọn',
#                    'CT175': 'Bắt buộc',
#                    'CT181': 'Tự chọn',
#                    'CT184': 'Tự chọn',
#                    'CT112': 'Bắt buộc',
#                    'CT109': 'Bắt buộc',
#                    'CT269': 'Tự chọn',
#                    'CT236': 'Tự chọn',
#                    'CT428': 'Bắt buộc',
#                    'CT271': 'Bắt buộc',
#                    'CT221': 'Bắt buộc',
#                    'CT202': 'Bắt buộc',
#                    'CT179': 'Bắt buộc',
#                    'ML007': 'Tự chọn',
#                    'XH028': 'Tự chọn',
#                    'XH014': 'Tự chọn',
#                    'XH011': 'Tự chọn',
#                    'XH012': 'Tự chọn',
#                    'CT335': 'Bắt buộc',
#                    'CT466': 'Bắt buộc',
#                    'CT222': 'Bắt buộc',
#                    'CT233': 'Bắt buộc',
#                    'CT206': 'Tự chọn',
#                    'CT251': 'Tự chọn',
#                    'CT207': 'Tự chọn',
#                    'CT235': 'Tự chọn',
#                    'CT212': 'Tự chọn',
#                    'CT450': 'Bắt buộc',
#                    'CT593': 'Tự chọn',
#                    'CT468': 'Tự chọn',
#                    'CT272': 'Tự chọn',
#                    'CT273': 'Tự chọn',
#                    'CT338': 'Tự chọn',
#                    'CT274': 'Tự chọn',
#                    'CT223': 'Tự chọn',
#                    'CT211': 'Tự chọn',
#                    'CT275': 'Tự chọn',
#                    'CT224': 'Tự chọn',
#                    'CT231': 'Tự chọn'}
#     # Học phần tiên quyết của 'ML010' là 'ML009'
#     ModulesPrerequisite = {'ML010': 'ML009',
#                            'CT103': 'CT101',
#                            'TN002': 'TN001',
#                            'XH024': 'XH023',
#                            'XH005': 'XH004',
#                            'ML006': 'ML010',
#                            'CT180': 'CT103',
#                            'CT174': 'CT103',
#                            'CT176': 'CT101',
#                            'XH025': 'XH024',
#                            'XH006': 'XH005',
#                            'ML011': 'ML006',
#                            'CT178': 'CT173',
#                            'CT183': 'XH025',
#                            'CT175': 'CT103',
#                            'CT184': 'CT183',
#                            'CT112': 'CT178',
#                            'CT109': 'CT180',
#                            'CT271': '>=80TC',
#                            'CT221': 'CT112',
#                            'CT335': 'CT112',
#                            'CT466': '>=100TC',
#                            'CT233': 'CT112',
#                            'CT206': ['CT176', 'CT180'],
#                            'CT251': ['CT176', 'CT180'],
#                            'CT207': 'CT101',
#                            'CT235': 'CT112',
#                            'CT212': 'CT112',
#                            'CT450': '>=120TC',
#                            'CT593': '>=120TC',
#                            'CT468': '>=120TC',
#                            'CT274': 'CT176',
#                            'CT223': 'CT171',
#                            'CT224': 'CT176'}
#     try:
#         result = 'Học phần tiên quyết của học phần {0} là học phần {1}'.format(ModulesCode[moduleCode], ModulesCode[
#             ModulesPrerequisite[moduleCode]])
#     except:
#         result = ''
#         try:
#             result = 'Học phần tiên quyết của môn ' + ModulesCode[moduleCode] + ' là các học phần sau đây:'
#             for mod in ModulesPrerequisite[moduleCode]:
#                 result = result + '\n' + ModulesCode[mod]
#         except:
#             result = ''
#             try:
#                 result = 'Điều kiện tiên quyết của học phần {0} là tích lũy {1}'.format(ModulesCode[moduleCode],
#                                                                                         ModulesPrerequisite[moduleCode])
#             except:
#                 result = ''
#                 try:
#                     result = 'Học phần {0} không có môn tiên quyết'.format(ModulesCode[moduleCode])
#                 except:
#                     result = 'Không tồn tại học phần {0} trong kế hoạch học tập của sinh viên CNTT'.format(
#                         moduleCode)
#     return result


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_hello_world"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Hello World!")

        return []


class ActionModulesType(Action):

    def name(self) -> Text:
        return "action_modules_type"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            module_code = tracker.latest_message['entities'][0]['value']
            text = custom_code.LoaiHocPhan.loai_hoc_phan(module_code)
            dispatcher.utter_message(text)
        except:
            dispatcher.utter_message(text='Tạm thời chưa thể trả lời cho bạn được, thông cảm nhé')

        return []


class ActionModulesName(Action):

    def name(self) -> Text:
        return "action_modules_name"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        try:
            module_code = tracker.latest_message['entities'][0]['value']
            text = custom_code.TenHocPhan.ten_hoc_phan(module_code)
            dispatcher.utter_message(text)
        except:
            dispatcher.utter_message(text='Tạm thời chưa thể trả lời cho bạn được, thông cảm nhé')

        return []


class ActionModulesPrerequisite(Action):

    def name(self) -> Text:
        return "action_modules_prerequisite"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # module_code = tracker.latest_message['entities'][0]['value']
        try:
            module_code = tracker.latest_message['entities'][0]['value']
            text = custom_code.MonTienQuyet.hoc_phan_tien_quyet(module_code)
            dispatcher.utter_message(text)
        except:
            #     module_code = tracker.get_slot('modulesCode')
            #     SlotSet('modulesCode', module_code)
            dispatcher.utter_message(text='Tạm thời chưa thể trả lời cho bạn được, thông cảm nhé')
        return []

class ActionModulesCode(Action):

    def name(self) -> Text:
        return "action_modules_code"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # module_code = tracker.latest_message['entities'][0]['value']
        try:
            module_name = tracker.latest_message['entities'][0]['value']
            text = module_name + ' có mã học phần là ' + custom_code.MaHocPhan.ma_hoc_phan(module_name)
            dispatcher.utter_message(text)
        except:
            #     module_code = tracker.get_slot('modulesCode')
            #     SlotSet('modulesCode', module_code)
            dispatcher.utter_message(text='Tạm thời chưa thể trả lời cho bạn được, thông cảm nhé')
        return []

# class ActionModulesType(Action):
#
#     def name(self) -> Text:
#         return "action_modules_type"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text='Text from action_modules_type')
#
#         return []
