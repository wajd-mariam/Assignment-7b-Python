#!/usr/bin/env python3

# Created by: Wajd Mariam
# Created on: December 2019
# This program translates words from Pig Latin and back.


def pig_latin_translate(word_1):
    # this function
    ay = "ay"
    way = "way"

    # assigning the first letter of the string to a variable.
    first_letter = word_1[0]
    first_letter = str(first_letter)
    first_letter = first_letter.upper()

    # if statement to check if the first letter is a consonant or vowels.
    if first_letter is "B" or "C" or "D" or "F" or "G" or "H" or "J" \
                       or "K" or "L" or "M" or "N" or "Q" or "R" or "S" \
                       or "T" or "V" or "W" or "X":
        length_of_word = len(word_1)
        remove_first_letter = word_1[1:length_of_word]
        final_word = remove_first_letter + first_letter + ay
    if first_letter is "A" or "E" or "I" or "O" or "U":
        length_of_word = len(word_1)
        remove_first_letter = word_1[1:length_of_word]
        final_word = remove_first_letter + way

    return final_word


def english_translate(word_2):
    # removing the last two letters of the pig latin word ("ay")
    remove_ay_word = word_2[:-2]
    length_of_word_2 = len(remove_ay_word)
    last_letter = remove_ay_word[length_of_word_2 - 1]
    word = remove_ay_word[:-1]
    final_word = last_letter + word

    return final_word


def main():
    # this function gets input from the user.
    # description to user.
    print("This program translates words from Pig Latin and back!")
    print("")

    # while true loop
    try:
        question = input("Do you want to translate to Pig Latin (y/n): ")
        if question.upper() == "Y" or question.upper() == "YES":
            english_word = input("Enter word to translate to Pig Latin: ")
            # calling function to translate to pig latin
            pig_latin = pig_latin_translate(english_word)
            # output
            print("")
            print("The translation to Pig Latin is {}".format(pig_latin))
        elif question.upper() == "N" or question.upper() == "NO":
            pig_latin_word = input("Enter word to translate to English: ")
            # calling function to translate to english
            english = english_translate(pig_latin_word)
            # output
            print("")
            print("The translation to English is {}".format(english))
        else:
            print("")
            print("Invalid answer.Please try again.")
            print("")
    except Exception:
        print("Invalid input.Please try again.")


if __name__ == "__main__":
    main()
