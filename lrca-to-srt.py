import json
import argparse
from pathlib import Path
import time

parser = argparse.ArgumentParser(__file__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("-f", "--file", type=str, default="file.lrca", help="Project file")
args = parser.parse_args() # either manually input the VPR filename here or pass it as a command line argument

lrca_path = Path(args.file)
srt_path = lrca_path.with_suffix(".srt")
srt_num = 1

time.sleep(0.5)
print(f"Loaded {lrca_path}.")
time.sleep(1)
print(f"Converting to .srt format...")

with open(lrca_path, mode="r", encoding="utf-8") as f:
    data = json.load(f) # load-then-close

srt = ''

for x in range(1000):
    try:
        project = data["project"]["tracks"][x]["clips"]
        for y in range(1000):
            start_string = ''
            end_string = ''
            text_string = ''
            str_start_min = ''
            str_start_sec = ''
            str_start_ms = ''
            try:
                for clips in str(project[y]["startTime"]):
                    start_string = start_string + clips
                for clips in str(project[y]["endTime"]):
                    end_string = end_string + clips
                for clips in str(project[y]["text"]):
                    text_string = text_string + clips
                start_float = round(float(start_string),3)
                end_float = round(float(end_string),3)

                start_minute = int(start_float / 60)
                start_second = start_float % 60
                start_second = int(start_second / 1)
                start_mili = int(round((start_float % 1 * 1000), 0))

                if int(start_minute / 10) == 0:
                    str_start_min = str(0) + str(start_minute)
                else:
                    str_start_min = str(start_minute)

                if int(start_second / 10) == 0:
                    str_start_sec = str(0) + str(start_second)
                else:
                    str_start_sec = str(start_second)
                
                if int(start_mili / 10) == 0:
                    str_start_ms = str(0) + str(start_mili)
                else:
                    str_start_ms = str(start_mili)

                if int(start_mili / 100) == 0:
                    str_start_ms = str(0) + str_start_ms

                end_minute = int(end_float / 60)
                end_second = end_float % 60
                end_second = int(end_second / 1)
                end_mili = int(round((end_float % 1 * 1000), 0))

                if int(end_minute / 10) == 0:
                    str_end_min = str(0) + str(end_minute)
                else:
                    str_end_min = str(end_minute)

                if int(end_second / 10) == 0:
                    str_end_sec = str(0) + str(end_second)
                else:
                    str_end_sec = str(end_second)
                
                if int(end_mili / 10) == 0:
                    str_end_ms = str(0) + str(end_mili)
                else:
                    str_end_ms = str(end_mili)

                if int(end_mili / 100) == 0:
                    str_end_ms = str(0) + str_end_ms
                
                srt = srt + str(srt_num) + "\n00:" + str_start_min + ":" + str_start_sec + "," + str_start_ms + " --> 00:" + str_end_min + ":" + str_end_sec + "," + str_end_ms + "\n" + text_string + "\n\n"
                srt_num = srt_num + 1
            except Exception as e:
                pass
    except Exception as e:
        pass

with open(srt_path, mode="w", encoding="utf-8") as f:
    f.write(srt)

time.sleep(5)
print(f"Output .srt to {srt_path}.")
time.sleep(1)
print("Press any key to exit.")
input()