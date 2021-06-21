#TO RUN: enter in `python3 ./sort_data.py <input_file>`

import sys
from datetime import datetime

print("opening " + sys.argv[1] + "...")

inp = open(sys.argv[1], "r")

data = inp.readlines()
split_line_list = []

for line in data:
    split_line_list.append(line.split("\t"))
    
count = 1
output_file_name = sys.argv[1].replace(".txt", ".js")
print("writing to " + output_file_name + "...")
out = open(output_file_name, "w")
for person in split_line_list:
    now = datetime.now()
    output_id = "{\"ex\":"+ str(count) + ","
    output_e = output_id + "\"e\":" + str(count) + ","
    output_p = output_e + "\"p\":" + str(count) + ","
    output_l = output_p + "\"l\":\"" + person[6].replace("\"", "") + "\","
    output_f = output_l + "\"f\":\"" + person[7].replace("\"", "") + "\","
    output_dob = output_f + "\"dob\":\"\","
    output_c = output_dob + "\"c\":\"" + person[11].replace("\"", "") + "\","
    output_s = output_c + "\"s\":\"" + person[12].replace("\"", "") + "\","
    output_z = output_s + "\"z\":\"" + person[13].replace("\"", "") + "\","
    output_a1 = output_z + "\"a1\":\"" + person[9].replace("\"", "") + "\","
    output_a2 = output_a1 + "\"a2\":\"\","
    output_p1 = output_a2 + "\"p1\":\"" + person[14].replace("\"", "") + "\","
    output_p2 = output_p1 + "\"p2\":\"\","
    output_em = output_p2 + "\"em\":\"" + person[15].replace("\"", "") + "\","
    #fix with current date time
    output_d = output_em + "\"d\":\"" + now.strftime("%Y/%m/%d %H:%M:%S") + "\","
    output_g = output_d + "\"g\":\"" + person[0].replace("\"", "") + "\","
    output_pk = output_g + "\"pk\":\"" + person[16].replace("\"", "") + "\","
    output_t = output_pk + "\"t\":\"" + person[17].replace("\"", "") + "\","
    output_u = output_t + "\"u\":\"" + person[18].rstrip("\n") + "\","
    output_b = output_u + "\"b\":\"\"}"
    print(output_b, file=out)
    count += 1