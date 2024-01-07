from namecounter import NameCounter


def main():
    namecount = NameCounter("../data/ira.txt")
    counter = namecount.find_single("Ni Ketut Ira Permata Adi", sim_thresh=0.7)
    print(f"Number of occurence: {counter}")


if __name__ == "__main__":
    main()
