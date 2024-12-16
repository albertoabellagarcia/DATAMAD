import shapefile
# import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

import matplotlib.pyplot as plt

# Path to the shapefile
dat_dir = './'
# shp_file_base = 'IDEM_MA_FISIOGRAFIA_50M.zip'
# shp_file_base = 'IDEM_MA_PISOS_BIOCLIMA.zip'
# shp_file_base = "IDEM_MA_EDAR.zip"
# shp_file_base = "IDEM_MA_AREAS_RECREA.zip"
# shp_file_base = "IDEM_BTA_10M_NOMGEO_PUN_11.zip"
# shp_file_base = "IDEM_URB_HOJAS_10000.zip"
shp_file_base = "IDEM_BTA_10M_SERVINST_POL_11.zip"
# Read the shapefile
sf = shapefile.Reader(dat_dir + shp_file_base, encoding='iso-8859-1')

# Print the number of shapes imported
print('Number of shapes imported:', len(sf.shapes()))

# Extract the shapes and their records
shapes = sf.shapes()
records = sf.records()

# Plot the shapes
# plt.figure()
for shape in shapes:
    x = [i[0] for i in shape.points]
    y = [i[1] for i in shape.points]
    plt.plot(x, y)

plt.show()