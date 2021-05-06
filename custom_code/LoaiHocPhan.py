# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

import custom_code.TenHocPhan


def loai_hoc_phan(module):
    module_type = {'QP001': 'Bắt buộc',
                   'TN033': 'Bắt buộc',
                   'TN034': 'Bắt buộc',
                   'TN001': 'Bắt buộc',
                   'ML009': 'Bắt buộc',
                   'CT101': 'Bắt buộc',
                   'KL001': 'Bắt buộc',
                   'TN010': 'Bắt buộc',
                   'TN012': 'Bắt buộc',
                   'XH023': 'Tự chọn',
                   'XH004': 'Tự chọn',
                   'ML010': 'Bắt buộc',
                   'TC001': 'Tự chọn',
                   'CT172': 'Bắt buộc',
                   'CT103': 'Bắt buộc',
                   'TN002': 'Bắt buộc',
                   'XH024': 'Tự chọn',
                   'XH005': 'Tự chọn',
                   'ML006': 'Bắt buộc',
                   'CT173': 'Bắt buộc',
                   'CT180': 'Bắt buộc',
                   'CT174': 'Bắt buộc',
                   'CT176': 'Bắt buộc',
                   'XH025': 'Tự chọn',
                   'XH026': 'Tự chọn',
                   'ML011': 'Bắt buộc',
                   'CT178': 'Bắt buộc',
                   'CT237': 'Bắt buộc',
                   'CT187': 'Bắt buộc',
                   'CT182': 'Tự chọn',
                   'CT183': 'Tự chọn',
                   'CT175': 'Bắt buộc',
                   'CT181': 'Tự chọn',
                   'CT184': 'Tự chọn',
                   'CT112': 'Bắt buộc',
                   'CT109': 'Bắt buộc',
                   'CT269': 'Tự chọn',
                   'CT236': 'Tự chọn',
                   'CT311': 'Bắt buộc',
                   'CT332': 'Bắt buộc',
                   'CT171': 'Bắt buộc',
                   'CT428': 'Bắt buộc',
                   'CT271': 'Bắt buộc',
                   'CT221': 'Bắt buộc',
                   'CT202': 'Bắt buộc',
                   'CT179': 'Bắt buộc',
                   'ML007': 'Tự chọn',
                   'XH028': 'Tự chọn',
                   'XH014': 'Tự chọn',
                   'XH011': 'Tự chọn',
                   'XH012': 'Tự chọn',
                   'CT335': 'Bắt buộc',
                   'CT466': 'Bắt buộc',
                   'CT222': 'Bắt buộc',
                   'CT233': 'Bắt buộc',
                   'CT206': 'Tự chọn',
                   'CT251': 'Tự chọn',
                   'CT207': 'Tự chọn',
                   'CT235': 'Tự chọn',
                   'CT212': 'Tự chọn',
                   'CT450': 'Bắt buộc',
                   'CT593': 'Tự chọn',
                   'CT468': 'Tự chọn',
                   'CT272': 'Tự chọn',
                   'CT273': 'Tự chọn',
                   'CT338': 'Tự chọn',
                   'CT274': 'Tự chọn',
                   'CT223': 'Tự chọn',
                   'CT211': 'Tự chọn',
                   'CT275': 'Tự chọn',
                   'CT224': 'Tự chọn',
                   'CT231': 'Tự chọn'}
    if module in module_type.keys():
        return module + " (" + custom_code.TenHocPhan.ten_hoc_phan(module) + ") là học phần " + module_type[module]
    else:
        return module + " không có trong chương trình đào tạo"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(loai_hoc_phan('CT332'))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
