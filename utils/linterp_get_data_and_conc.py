import numpy as np

import sys

def main(file):
    data = open(file, "r").read().split("\n")
    labels = []
    Ni = []
    Pb = []

    for line in data:
        if not line.strip():
            continue
        parts = line.split()
        if len(parts) < 3:
            continue
        label_str, ni_str, pb_str = parts[0], parts[1], parts[2]

        def parse_value(s):
            if "/" in s:
                num, den = s.split("/")
                return float(num) / float(den)
            return float(s)
        
        labels.append(label_str)
        Ni.append(parse_value(ni_str))
        Pb.append(parse_value(pb_str))

    # Optionally, convert lists to numpy arrays:
    labels = np.array(labels)
    Ni = np.array(Ni)
    Pb = np.array(Pb)
    print(labels, Ni, Pb)

    Ni -= Ni[0]
    Pb -= Pb[0]
    
    label_blocks = [labels[i:3+i] for i in range(1, len(labels),3)]
    Ni_blocks = [Ni[i:3+i] for i in range(1, len(labels),3)]
    Pb_blocks = [Pb[i:3+i] for i in range(1, len(labels),3)]

    for i, block in enumerate(Ni_blocks):
        print(f"Ni block {i+1}:")
        print(block)



if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print("Please give one argument!")
    else:
        main(sys.argv[1])
    