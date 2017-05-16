import lmdb
import cv2
import numpy as np

caffe_root = '../../fixed-point-ssd-new/alpha-caffe/'
import sys
sys.path.insert(0, caffe_root + 'python')
import caffe
from caffe.proto import caffe_pb2

lmdb_env = lmdb.open('umdface_test_lmdb', readonly=True)
lmdb_txt = lmdb_env.begin()
lmdb_cur = lmdb_txt.cursor()
datum = caffe_pb2.AnnotatedDatum()
#datum = caffe_pb2.Datum()
# print type(datum)
# print isinstance(datum, Iterable)
# print hasattr(datum.datum, '__iter__')

for key, value in lmdb_cur:
    datum.ParseFromString(value)
    label = datum.datum.label
    data = caffe.io.datum_to_array(datum.datum)
    image = data.transpose(1, 2, 0)
    cv2.imshow('cv2.jpg', image)
    cv2.waitKey(0)
    # print datum.label
#    print type(datum)
#    for data in datum.datum
#        print data.label
    #print datum.datum.label
#    print datum.datum.float_data
    #data = caffe.io.datum_to_array(datum.datum)
    #print datum.type
    #image = data.transpose(1, 2, 0)
    #cv2.imshow('cv2.jpg', image)
    #cv2.waitKey(0)

cv2.destroyAllWindows()
lmdb_env.close()
