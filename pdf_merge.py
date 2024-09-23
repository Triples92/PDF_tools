

from pypdf import PdfWriter
import sys

output_name = sys.argv[1]
file1 = sys.argv[2]
file2 = sys.argv[3]
file3 = sys.argv[4] if sys.argv[4] != "None" else None
file4 = sys.argv[5] if sys.argv[5] != "None" else None
file5 = sys.argv[6] if sys.argv[6] != "None" else None
file6 = sys.argv[7] if sys.argv[7] != "None" else None

file_list = [file1,file2,file3,file4,file5,file6]
merger = PdfWriter()

for pdf in file_list:
    if pdf == None:
        pass
    else:
        merger.append(pdf)

merger.write(output_name)
merger.close()