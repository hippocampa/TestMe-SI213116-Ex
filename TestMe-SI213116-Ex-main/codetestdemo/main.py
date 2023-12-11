from namecounter import NameCounter


def main():
    namecount = NameCounter("../data/index.txt")
    namecount = NameCounter("C:\Users\mades\OneDrive\Documents\Malto\!\TestMe-SI213116-Ex-main/data/index.txt")
    counter = namecount.find_single("I Gede Teguh Satya Dharma", sim_thresh=0.5)
    print(f"Number of occurence: {counter}")


if __name__ == "__main__":
    main()
