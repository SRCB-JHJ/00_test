import os
import shutil


def main() -> None:

    folder = './SV_800_equis/blender_generated/'
    equi_dir = './SV_800_equis/equis'
    corner_dir = './SV_800_equis/corners'
    houses = os.listdir(folder)
    for house in houses:
        path_house = os.path.join(folder, house)
        cameras = os.listdir(path_house)
        for camera in cameras:
            path_camera = os.path.join(path_house, camera)
            equi_path = os.path.join(path_camera, 'generate_room_from_json.jpg')
            equi_new_path_and_name = os.path.join(equi_dir, house + '_c' + camera + '_' + 'generate_room_from_json.jpg')
            corner_path = os.path.join(path_camera, 'corners_on_image.txt')
            corner_new_path_and_name = os.path.join(corner_dir, house + '_c' + camera + '_' + 'corners_on_image.txt')
            shutil.copy(equi_path, equi_new_path_and_name)
            shutil.copy(corner_path,corner_new_path_and_name)


if __name__ == '__main__':
    main()
