python ../../fixed-point-ssd-new/alpha-caffe/scripts/create_annoset.py --anno-type=detection \
    --label-type=txt --label-map-file=./labelmap_face.prototxt \
    --check-label --shuffle \
    ./ \
    ./test_label.txt \
    ./umdface_test_lmdb .

# --max-dim=0 --resize-width=0 --resize-height=0 --check-label --shuffle \
# --encode-type=jpg --encoded ./ \
