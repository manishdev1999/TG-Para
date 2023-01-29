import common as common_function
import settings as setting


dataFromExcel = common_function.read_excel(
    setting.file_name, setting.setting_sheet)
print(dataFromExcel)

#itterate over the dataFrame and process the data for results

