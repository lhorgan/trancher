import csv
import random
import sys

def main():
    in_filename = sys.argv[1]
    out_filename = sys.argv[2]
    tranch_size = int(sys.argv[3])

    process(in_filename, out_filename, tranch_size)

def process(filename, out_filename, tranch_size):
    with open(filename) as f:
        line_count = sum(1 for line in f)

    out_file = open(out_filename, "wb+")

    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        
        row1 = next(reader)
        print(row1)
        out_file.write(",".join(row1) + "\n")
        tags_ind = row1.index("Tags")

        tranch_count = int((line_count - 1) / tranch_size)

        for row in reader:
            curr_tags = row[tags_ind].strip('"').split(",")
            curr_tags_copy = []
            for tag in curr_tags:
                if not tag.startswith("tranch_") and len(tag) > 0:
                    curr_tags_copy.append(tag)
            curr_tags = curr_tags_copy

            curr_tags.append("tranch_" + str(random.randrange(1, tranch_count + 1)))
            tag_str = '"' + ",".join(curr_tags) + '"'
            row[tags_ind] = tag_str
            out_file.write(",".join(row) + "\n")
    
    out_file.close()

main()
