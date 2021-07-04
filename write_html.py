import os


def generate_single(image_id, image_in, label, ours,ours_epoch_1000,
                                  ours_epoch_2000,ours_epoch_3000,ours_epoch_4000,ours_epoch_5000):
    message = """
<h2>%s. </h2>
<center><table border="1">
<COLGROUP>
<COL width="100"><COL width="100"><COL width="100">
<THEAD>
<tr>
<td><center><b>Input<b></center><a href="%s" title="Input" class="thickbox"><img src="%s"width="300" height="149" alt="Sorry, No Display!" border="0"/></a></td>
<td><center><b>Annotation<b></center><a href="%s" title="Kinect" class="thickbox"><img src="%s"width="300" height="149" alt="Sorry, No Display!" border="0"/></a></td>
<td><center><b>Ours<b></center><a href="%s" title="Ours" class="thickbox"><img src="%s"width="300" height="149" alt="Sorry, No Display!" border="0"/></a></td>
<td><center><b>Ours_epoch_1000<b></center><a href="%s" title="Ours_epoch_1000" class="thickbox"><img src="%s"width="300" height="149" alt="Sorry, No Display!" border="0"/></a></td>
<td><center><b>Ours_epoch_2000<b></center><a href="%s" title="Ours_epoch_2000" class="thickbox"><img src="%s"width="300" height="149" alt="Sorry, No Display!" border="0"/></a></td>
<td><center><b>Ours_epoch_3000<b></center><a href="%s" title="Ours_epoch_3000" class="thickbox"><img src="%s"width="300" height="149" alt="Sorry, No Display!" border="0"/></a></td>
<td><center><b>Ours_epoch_4000<b></center><a href="%s" title="Ours_epoch_4000" class="thickbox"><img src="%s"width="300" height="149" alt="Sorry, No Display!" border="0"/></a></td>
<td><center><b>Ours_epoch_5000<b></center><a href="%s" title="Ours_epoch_5000" class="thickbox"><img src="%s"width="300" height="149" alt="Sorry, No Display!" border="0"/></a></td>
<td><ce
<tr>
</tr>
</table></center>

    """ % (image_id, image_in, image_in, label, label, ours, ours,ours_epoch_1000,ours_epoch_1000,
                                  ours_epoch_2000,ours_epoch_2000,ours_epoch_3000,ours_epoch_3000,
                                  ours_epoch_4000,ours_epoch_4000,ours_epoch_5000,ours_epoch_5000)
    return message


image_path = 'leftImg8bit/val/frankfurt/'
id_path = 'gtFine/val/frankfurt/'
path = './aachen_24_input'
val_input_path = './aachen_24_input/'
val_annotation_path = './aachen_24_label/'
ours_path = './train_aachen_24_batch_24_bicubic/color/'
ours_epoch_1000_path = './train_aachen_24_batch_12_unique_single_scale_resize_epoch_1000/color/'
ours_epoch_2000_path = './train_aachen_24_batch_12_unique_single_scale_resize_epoch_2000/color/'
ours_epoch_3000_path = './train_aachen_24_batch_12_unique_single_scale_resize_epoch_3000/color/'
ours_epoch_4000_path = './train_aachen_24_batch_12_unique_single_scale_resize_epoch_4000/color/'
ours_epoch_5000_path = './train_aachen_24_batch_12_unique_single_scale_resize_epoch_5000/color/'
# ours_resized_path = './train_aachen_24_batch_24_bicubic/color/'
# ours_resized_epoch_1000_path = './train_aachen_24_batch_24_epoch_1000/color/'
file_path = './train_aachen24_single_scale.html'
f = open(file_path, 'w')
l = os.listdir(path)
s = ''
# for file in l:
#     s += '\n'
#     s += image_path + file + ' '
#     temp = file.replace('leftImg8bit','gtFine_labelIds')
#     s += id_path + temp
#     break

# image_id = 0
# for folder in l:
#     deep_path = os.path.join(path,folder)
#     deep_l = os.listdir(deep_path)
#     for file in deep_l:
#         image_id += 1
#         image_in = val_input_path + folder + '/' + file
#         temp = file.replace('leftImg8bit','gtFine_color')
#         label = val_annotation_path + folder + '/' + temp
#         ours = ours_path + file
#         ours_resized = ours_resized_path + file
#         single_html = generate_single(image_id,image_in,label,ours,ours_resized)
#         s += single_html
# f.write(s)
image_id = 0
for file in l:
    image_id += 1
    image_in = val_input_path + file
    temp = file.replace('leftImg8bit', 'gtFine_color')
    label = val_annotation_path + temp
    ours = ours_path + file
    ours_epoch_1000 = ours_epoch_1000_path + file
    ours_epoch_2000 = ours_epoch_2000_path + file
    ours_epoch_3000 = ours_epoch_3000_path + file
    ours_epoch_4000 = ours_epoch_4000_path + file
    ours_epoch_5000 = ours_epoch_5000_path + file
    # ours_resized = ours_resized_path + file
    # ours_resized_epoch_1000 = ours_resized_epoch_1000_path + file
    single_html = generate_single(image_id, image_in, label, ours,ours_epoch_1000,
                                  ours_epoch_2000,ours_epoch_3000,ours_epoch_4000,ours_epoch_5000)
    s += single_html

head = """<html><head><title>Cityscapes-visualization</title>
<script language="javascript" type="text/javascript" src="javascript/jquery.js"></script>
<link rel="stylesheet" href="css/thickbox.css" type="text/css" media="screen" /></head>
<body>
<script language="javascript" type="text/javascript" src="javascript/thickbox.js"></script>
<center><h1>Cityscapes result</h1></center>"""

tail = """


</body>
</html>
"""

s = head + s + tail

f.write(s)
