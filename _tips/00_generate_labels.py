#!/usr/bin/python
import os
import sys
import csv

if len(sys.argv) != 4 :
    print 'Usage: ' + sys.argv[0] + ' image_dir csv_file output_file'
    sys.exit()
else :
    image_dir = sys.argv[1]
    csv_file = sys.argv[2]
    output_file = sys.argv[3]

out_f = open(output_file, 'w')

with open(csv_file, 'r') as f :
    f_csv = csv.DictReader(f)
    for row in f_csv :
        file_name = row['FILE']
        xmin = float(row['FACE_X'])
        ymin = float(row['FACE_Y'])
        xmax = xmin + float(row['FACE_WIDTH'])
        ymax = ymin + float(row['FACE_HEIGHT'])
        image_file_path = image_dir + '/' + file_name
        if os.path.exists(image_file_path) and os.path.isfile(image_file_path) :
            anno_txt = '1 ' + str(xmin) + ' ' + str(ymin) + ' ' + str(xmax) + ' ' + str(ymax)
            anno_file_path = image_dir + '/' + file_name + '.txt'
            with open(anno_file_path, 'w') as txt_f :
                txt_f.write(anno_txt)
            out_txt = image_file_path + ' ' + anno_file_path + '\n'
            out_f.write(out_txt)

out_f.close()
