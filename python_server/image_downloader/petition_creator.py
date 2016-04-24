import xml.etree.cElementTree as xml_maker
import string_constants as constants

class petition_maker():

    def __init__(self, image_type, date, EPSG_code, resolution, save_format):
        self.petition = constants.GIBIS_URL_HEAD + image_type + constants.GIBIS_URL_DEF + "/" + date + "/" + constants.EPSG_code + "_" + resolution + "/" + constants.GIBIS_URL_NAME + save_format

    def GeneraPetition(self, level, levelX, levelY, origin, EPSG_code, bands):
        root = xml_maker.Element("GDAL_WMS")
        service = xml_maker.SubElement(root, "Service", name = "TMS")
        url = xml_maker.SubElement(service, "ServerUrl").text = self.petition
        window = xml_maker.SubElement(root, "DataWindow")
        ulx = xml_maker.SubElement(window, "UpperLeftX").text = -180.0
        uly = xml_maker.SubElement(window, "UpperLeftY").text = 90
        lrx = xml_maker.SubElement(window, "LowerRightX").text = 360.0
        lry = xml_maker.SubElement(window, "LowerRightY").text = -198
        tileL = xml_maker.SubElement(window, "TileLevel").text = level
        tileCX = xml_maker.SubElement(window, "TileCountX").text = levelX
        tileCX = xml_maker.SubElement(window, "TileCountY").text = levelY
        YOrigin = xml_maker.SubElement(window, "YOrigin").text = origin
        proyection = xml_maker.SubElement(root, "Projection").text = EPSG_code
        sizeX = xml_maker.SubElement(root, "BlockSizeX").text = 512
        sizeY = xml_maker.SubElement(root, "BlockSizeY").text = 512
        bamds = xml_maker.SubElement(root, "BandsCount").text = bands

        xml_petition = xml_maker.ElementTree(root)
        xml_petition.write("petition.xml")
