from namecounter import NameCounter


def main():
    namecount = NameCounter("../data/index.txt")
    counter = namecount.find_single("Stephanie Stone", sim_thresh=0.5)
    print(f"Number of occurence: {counter}")


if __name__ == "__main__":
    main()
