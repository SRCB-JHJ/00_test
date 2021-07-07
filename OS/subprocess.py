import subprocess
import pathlib

def main() -> None:
    # hyper paremeters
    OUTPUT_DIR = '--output_dir=SV_800_equis'
    WIDTH = '--width=1024'
    HEIGHT = '--height=512'
    # path of floorplan json files
    json_dir = pathlib.Path('./SV_800_jsons/jsons')
    # looping for floorplan jsons
    for json_path in json_dir.glob('*.json'):
        # render images
        blender_cmd = ['blender', '-b', '-P', './blender/scripts/generate_room_from_json.py', '--']
        layout: str = '--layout='
        layout += str(json_path)
        blender_cmd.append(layout)
        blender_cmd.append(OUTPUT_DIR)
        blender_cmd.append(WIDTH)
        blender_cmd.append(HEIGHT)
        subprocess.run(blender_cmd)
        # make corner coordinates
        python_cmd = ['python', './floorplan/src/cghouse/make_horizonnet.py',]
        python_cmd.append(layout)
        python_cmd.append(OUTPUT_DIR)
        python_cmd.append(WIDTH)
        python_cmd.append(HEIGHT)
        subprocess.run(python_cmd)
        
        
if __name__ == '__main__':
    main()
