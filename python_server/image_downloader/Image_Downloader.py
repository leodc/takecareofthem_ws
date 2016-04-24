import petition_creator as creator
import os

class scene_obtainer():
    def __init__(self, image_type, date, EPSG_code, resolution, save_format):
        self.creator  = creator.petition_maker(image_type, date, EPSG_code, resolution, save_format)

    def GetImage(bounds, high, width, xml_file, output_name):
        image_path = "../images/"
        os.system("gdal_translate -of GTiff -outsize " + high + " " + width + "-projwin" + bounds[0] + " " + bounds[1] + " " + bounds[2] + " " + bounds[3] +  " " + xml_file + " " + image_path + output_name)
