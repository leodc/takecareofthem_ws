import bounds
import coordinate as coor
import nodo
import math
import cv2

INF = -1000

def MakeGrid(Bounds, rows, cols):
    x_increment = (Bounds[0].GetUL.GetLng() - Bounds[1].GetUL.GetLng()) / cols
    y_increment = (Bounds[1].GetUL.GetLat() - Bounds[3].GetDR.GetLat()) / rows
    current = Bounds[0].GetUL
    nodes = []

    for i in range(0, rows):
        lat_next = current.GetLat() + y_increment
        nodes.append([])
        for j in range(0, cols):
            lng_next = current.GetLng() + x_increment
            node = nodo.Nodo(lat_next / 2, lng_next / 2, 0)
            nodes[j].append(node)
            current = coor.Coordinate(current.GetLat(), lng_next)
        current = coor.Coordinate(lat_next, current.GetLng())

    return nodes


def CoorsDistance(Coord_1, Coord_2):
    lat_1 = Coord_1.GetLat() * math.pi / 180
    lon_1 = Coord_1.GetLng() * math.pi / 180
    lat_2 = Coord_2.GetLat() * math.pi / 180
    lon_2 = Coord_2.GetLng() * math.pi / 180
    distance = 6378.137 * math.acos(math.cos(lat_1) * math.cos(lat_2) * math.cos((lon_2 - lon_1)) + math.sin(lat_1) * math.sin(lat_2))
    return distance


def SetRoadsWeigts(nodes):
    line = CoorsDistance(nodes[0][0], nodes[0][1])
    diag = CoorsDistance(nodes[0][0], nodes[1][1])
    road_values = []
    counter = len(nodes) - 1
    Branching(line, diag, road_values, counter)


def Branching(line, diag, road_values, count):
    if(count > 0):
        return
    road_values[count].append([line, line, diag, diag])
    for i in range(0, count):
        Branching(line, diag, road_values, count - 1)


def CoorsToPixel(Bounds, image):
    dif_lat =



