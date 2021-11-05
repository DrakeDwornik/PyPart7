from typing import Dict

mode_dict = {
    1: "admin",
    2: "user"
}

admin_options_dict = {
    1: "Add a language",
    2: "update a language",
    3: "exit admin mode"
}

# Populate this dictionary with at least two languages.
# Use integers for keys and strings for values.
# Example: Key = 1. Value = 'English'.
lang_dict = {
    1: 'English',
    2: 'Spanish',
    3: 'Portuguese'
}

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'What is your name?'.
name_prompt_dict = {
            1: 'What is your name?',
            2: '¿Cómo te llamas?',
            3: 'Qual é o seu nome?'
        }

# Populate this dictionary with appropriate prompts that correspond with the ids from lang_dict.
# Example: Key = 1. Value = 'Hello'.
greetings_dict = {
            1: 'Hello',
            2: 'Hola',
            3: 'Olá'
        }


def print_options(options_dict: Dict[int, str], ) -> None:
    """
    Given a dictionary, this functions iterates through the values and prints them out.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language
    :return: None
    """
    print("Please choose an option below: ")
    for number, option in options_dict.items():
        print(f"{number}: {option}")


def options_input() -> int:
    """
    This function prompts the user for a language choice.

    :return: An integer representing the language choice made by the user
    """
    # valid_choice = False
    # while valid_choice is False:
    try:
        chosen_option = input()
        chosen_option = int(chosen_option)
    except:
        chosen_option = chosen_option

    return chosen_option


def option_choice_is_valid(options: Dict[int, str], option_choice: int) -> bool:
    """
    This method determines if the choice the user made is valid.

    :param lang_options: A dictionary
    Keys are integers representing a language id
    Values are strings representing the name of a language

    :param lang_choice: An integer representing the value the user selected
    :return: A boolean representing the validity of the lang_choice
    """
    valid_choice = False
    for number in options.keys():
        if number == option_choice:
            valid_choice = True
    return valid_choice


def get_name_input(name_prompt_options: Dict[int, str], lang_choice: int) -> str:
    """
    This method takes in a dictionary and a key. It returns the value in the dictionary that has a key corresponding to
    the lang_choice parameter.

    :param name_prompt_options: A dictionary where the key is an integer representing an id and the value is a prompt
    in the users chosen language
    :param lang_choice: The language the user has chosen
    :return:
    """
    return name_prompt_options[lang_choice]


def name_input(name_prompt: str) -> str:
    """
    This function takes in a string and uses it to prompt the user for their name.

    :param name_prompt: A string in the user's chosen language that asks them for their name
    :return: The user's response when asked for their name
    """
    result = input()
    return result


def greet(name: str, greetings_options: Dict[int, str], lang_choice: int) -> None:
    """
    Using the parameters provided, this function greets the user.

    :param name: The name the user provided
    :param greetings_options: A dictionary where the key is an integer representing a greeting and the value is a string
    with a greeting in the user's chosen language
    :param lang_choice: The language the user has chosen.
    :return:
    """
    print(f"{greetings_options[lang_choice]} {name}")

def admin_mode_select():
    print_options(admin_options_dict)

    chosen_admin_mode = options_input()
    while option_choice_is_valid(admin_options_dict, chosen_admin_mode) is False:
        print("Invalid selection. Try again.")
        chosen_admin_mode = options_input()
    return chosen_admin_mode

def


if __name__ == '__main__':
    print_options(mode_dict)
    chosen_mode = options_input()
    while option_choice_is_valid(mode_dict, chosen_mode) is False:
        print("Invalid selection. Try again.")
        chosen_mode = options_input()
    while chosen_mode == 1:
        admin_type = admin_mode_select()
        if admin_type == 1:
            add_a_language()
        elif admin_type == 2:
            update_a_language()
        elif admin_type == 3:
            chosen_mode = 2



    print_options(lang_dict)
    chosen_lang = options_input()
    while option_choice_is_valid(lang_dict, chosen_lang) is False:
        print("Invalid selection. Try again.")
        chosen_lang = options_input()
    print(get_name_input(name_prompt_dict, chosen_lang))
    selected_prompt = f"{get_name_input(name_prompt_dict, chosen_lang)} \n"
    chosen_name = name_input(selected_prompt)
    greet(chosen_name, greetings_dict, chosen_lang)
