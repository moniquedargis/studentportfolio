import GenderGuesserDict as gg
import sys

def explanation():
    print()
    print("Welcome to the python implementation of Gender Guesser.")

    while True:
        try:
            continue_or_quit = input("Would you like instructions? Enter Y or N: ")

            continue_or_quit = continue_or_quit.upper()

            if continue_or_quit not in 'YN':
                raise TypeError
            break
        except TypeError:
            print()
            print("Sorry, please choose from Y or N")

    if continue_or_quit == 'Y':
        print()
        print("Gender Guesser takes a piece of writing as input and will make a guess as to the gender of the author.")
        print("You'll be asked to input the name of the .txt file you'd like to analyze. Then, you'll be asked to identify the type of text being analyzed.")
        print()
        print("The Gender Guesser will look for words that are most commonly used by male and female authors.")
        print("Those words will then be used to determine whether the text was likely written by a male or a female author.")
        print()
        print("The Gender Guesser has 60-70% accuracy. Many factors can influence the results generated.")
        print("The Guesser will let you know whether this is a strong (more confident) or weak (less confident) guess.")
        print("Original javascript implementation, and further context for results, can be found at www.hackerfactor.com/GenderGuesser.php")
        print()

        while True:
            try:
                continue_or_quit = input("Enter Y to continue or N to quit: ")

                continue_or_quit = continue_or_quit.upper()

                if continue_or_quit not in 'YN':
                    raise TypeError
                break
            except TypeError:
                print()
                print("Sorry, please choose from Y or N")

        if continue_or_quit =='N':
            print('\n' + "Bye!")
            sys.exit()

def readtext():

    print()
    FILENAME = input("Please type the name of the file you'd like to analyze: ")

    FILENAME = FILENAME.lower()

    if ".txt" not in FILENAME:
        raise ImportError

    fvar = open (FILENAME, 'r')

    text = fvar.readline()

    allwords = []

    for aline in fvar:
        line = aline.lower()
        line = line.replace('.',' ').replace('?',' ').replace('!',' ').replace(",", ' ').replace('"',' ')
        line = line.replace('(',' ').replace(')',' ').replace('--',' ').replace('[', ' ').replace(']',' ')
        line = line.replace('_',' ').replace(" '", ' ').replace(':',' ').replace(';',' ').replace('{',' ')
        line = line.replace('}',' ').replace('—',' ').replace('”',' ').replace('“',' ').replace('’',' ')

        words = line.split()

        allwords.extend(words)

    fvar.close()

    if len(allwords) < 300:
        raise ValueError

    return allwords

def informaltest(textsample):

    FemaleInformal = 0
    MaleInformal = 0

    for iword in textsample:
        if iword in gg.InformalGenderDict:
            if gg.InformalGenderDict[iword] < 0:
                FemaleInformal = FemaleInformal + gg.InformalGenderDict[iword]
            if gg.InformalGenderDict[iword] > 0:
                MaleInformal = MaleInformal + gg.InformalGenderDict[iword]

    FemaleInformal = abs(FemaleInformal)

    if MaleInformal + FemaleInformal == 0:
        FemalePercent = 0
    else:
        FemalePercent = FemaleInformal/(MaleInformal+FemaleInformal) * 100

    if FemalePercent > 50.0:
        Guess = 'The author is likely female. '
    elif FemalePercent < 50.0:
        Guess = 'The author is likely male. '
    else:
        Guess = 'Unable to determine gender of author.'

    if FemalePercent < 60.0 and FemalePercent > 40.0:
        Confidence = 'This is a weak guess.'
    elif FemalePercent > 60.0 or FemalePercent < 40.0:
        Confidence = 'This is a strong guess.'
    else:
        Confidence = ''

    print(Guess,Confidence)

def formaltest(textsample):

    FemaleFormal = 0
    MaleFormal = 0


    for fword in textsample:
        if fword in gg.FormalGenderDict:
            if gg.FormalGenderDict[fword] < 0:
                FemaleFormal = FemaleFormal + gg.FormalGenderDict[fword]
            if gg.FormalGenderDict[fword] > 0:
                MaleFormal = MaleFormal + gg.FormalGenderDict[fword]

    FemaleFormal = abs(FemaleFormal)

    if MaleFormal + FemaleFormal == 0:
        FemalePercent = 0
    else:
        FemalePercent = FemaleFormal / (MaleFormal + FemaleFormal) * 100

    if FemalePercent > 50.0:
        Guess = 'The author is likely female. '
    elif FemalePercent < 50.0:
        Guess = 'The author is likely male. '
    else:
        Guess = 'Unable to determine gender of author.'

    if FemalePercent < 60.0 and FemalePercent > 40.0:
        Confidence = 'This is a weak guess.'
    elif FemalePercent > 60.0 or FemalePercent < 40.0:
        Confidence = 'This is a strong guess.'
    else:
        Confidence = ''

    print(Guess, Confidence)

def test_text(text_type, textsample):

    if text_type == 'F':
        print()
        formaltest(textsample)
    if text_type == 'I':
        print()
        informaltest(textsample)
    if text_type == 'U':
        print()
        print("Result if text is informal:")
        informaltest(textsample)
        print()
        print("Result if text is formal:")
        formaltest(textsample)

def main():

    explanation()

    while True:
        try:
            textsample = readtext()
            break
        except ValueError:
            print()
            print("Too few words. Try 300 words or more.")
        except ImportError:
            print()
            print("Please make sure you choose a .txt file")
        except FileNotFoundError:
            print()
            print("Sorry, that file couldn't be found. Please choose another.")

    while True:
        try:
            print()
            print("Formal texts include fiction, non-fiction, essays, news reports, etc.")
            print("Informal texts include blogs, chat messages, notes, and sometimes email.")
            print()
            text_type = input("How would you classify the text you are analyzing? Enter F for formal, I for informal, or U for unknown (will give results for both formal and informal): ")

            text_type = text_type.upper()

            if text_type not in 'FIU':
                raise TypeError
            break
        except TypeError:
            print("Sorry, please choose from F, I or U.")

    test_text(text_type, textsample)

    print()

    print("Thanks for using the Gender Guesser. Please restart to try another text.")


main()
