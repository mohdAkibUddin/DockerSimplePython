from rng import generateRandomNumber


def main():
    print("This program generates a random number between a minimum and maximum")
    minimum = int(input("Enter a minimum number, then hit enter: "))
    maximum = int(input("Enter a minimum number, then hit enter: "))
    randomNumber = generateRandomNumber(minimum, maximum)
    print(randomNumber)


if __name__ == "__main__":
    main()