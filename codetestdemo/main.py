from namecounter import NameCounter


def main():
    namecount = NameCounter("C:/Users/Edward/Downloads/project.edwardhidayat/TestMe-SI213116-Ex/data/index.txt")
    counter = namecount.find_single("I Gede Teguh Satya Dharma", sim_thresh=0.5)
    print(f"Number of occurence: {counter}")


if __name__ == "__main__":
    main()
