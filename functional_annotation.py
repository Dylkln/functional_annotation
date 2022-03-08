import glob
import gzip
import os
import argparse
import subprocess


def arguments():
    """
    set arguments
    """

    parser = argparse.ArgumentParser()

    # Mandatory arguments
    parser.add_argument("-i", "--interproscan_launcher", dest="interproscan_launcher",
                        type=str, required=True,
                        help="The path to interproscan .sh launcher")
    parser.add_argument("-p", "--protein_directory", dest="proteins",
                        type=str, required=True,
                        help="The path to directory containing all protein sequence files")
    parser.add_argument("-a", "--annotation", dest="annotation",
                        type=str, required=False, default=None,
                        help="the path to the directory where you want the annotation stored")

    return parser.parse_args()


def read_file(file):
    if file.endswith(".gz"):
        with gzip.open(file, "rt") as f:
            for line in f:
                yield line.strip()
    else:
        with open(file, "r") as f:
            for line in f:
                yield line.strip()


def get_files(path):
    return glob.glob(f"{path}/*")


def rewrite_file_with_header(an_file, f_an_file):
    header = "peptides\tmd5_seq_digest\tlength\t \
    database\tidentifiant\tfunction_tool\t""start\tend\tevalue\tT\tdate\t \
    interproscan\tfunction_interproscan\tinterproscan_member1\tinterproscan_member2"
    with open(f_an_file, "w") as fo:
        print(header, file=fo)
        for line in read_file(an_file):
            print(line, file=fo)

    os.remove(an_file)


def run_interproscan(file, i_launcher, a_directory):
    cmd = [i_launcher, "-f", "tsv", "-dra", "-iprlookup", "-goterms", "-appl",
           "Gene3D,HAMAP,PANTHER,Pfam,PIRSF,PRINTS,ProSiteProfiles,ProSitePatterns,SMART,"
           "SUPERFAMILY,TIGRFAM",
           "-d", a_directory, "-T", f"{a_directory}/tmp/", "-i", file]
    subprocess.call(cmd)
    an_file = a_directory + file.split("/")[-1] + ".tsv"
    f_an_file = an_file.split(".")[0] + "_annotations"
    rewrite_file_with_header(an_file, f_an_file)


def main():
    args = arguments()

    files = get_files(args.proteins)
    for file in files:
        run_interproscan(file, args.interproscan_launcher, args.annotation)


if __name__ == '__main__':
    main()
