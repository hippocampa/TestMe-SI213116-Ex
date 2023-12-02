from namecounter import NameCounter


def main():
    namecount = NameCounter("TestMe-SI213116-Ex\data\index.txt")
    counter = namecount.find_single("I Putu Ananta Putra Astika", sim_thresh=0.8)
    print(f"Number of occurence: {counter}")


if __name__ == "__main__":
    main()
