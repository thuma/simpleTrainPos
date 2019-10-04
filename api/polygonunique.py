import json

with open('kommunarray.geojson','r') as original:
    with open('kommunarrayu.geojson','w') as newfile:
        for line in original.readlines():
            data = json.loads(line)
            cords = data["geometry"]["coordinates"][0]
            done = []
            final = []
            for cord in cords:
                if str(cord[0])+str(cord[1]) not in done:
                    final.append(cord)
                done.append(str(cord[0])+str(cord[1]))
            final.append(cords[0])
            data["geometry"]["coordinates"][0] = final
            newfile.write(json.dumps(data)+"\n")

