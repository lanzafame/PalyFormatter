# PalyFormatter program

import xlsxwriter


# Variables input by the user
well_name = ""
vintage = ""
paly_type = ""
depth = []
zone = []
subzone = []
sample_type = []

# Variables generated by input variables
filename = paly_type + "_" + well_name + "_" + vintage + ".xlsx"
sheetname = "Paly_" + paly_type
zone_header = paly_type + "_ZONE"
subzone_header = paly_type + "_SUBZONE"
sample_type_header = paly_type + "_TYPE"
color_header = paly_type + "_COLOR"
subcolor_header = paly_type + "_SUBCOLOR"

# Create a workbook and add a worksheet
workbook = xlsxwriter.Workbook(filename, {'constant_memory': True})
worksheet = workbook.add_worksheet(sheetname)

# Text formatting
bold = workbook.add_format({'bold': 1})

# Data headers
worksheet.write('A1', 'DEPTH', bold)
worksheet.write('B1', zone_header, bold)
worksheet.write('C1', subzone_header, bold)
worksheet.write('D1', sample_type_header, bold)
worksheet.write('E1', color_header, bold)
worksheet.write('F1', subcolor_header, bold)

