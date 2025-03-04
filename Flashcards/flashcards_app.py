#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random as rd
import os
import time
import pandas as pd


# In[2]:


selection = 0


# In[3]:


def title_message():
    print("""
   __                                            
   \ \  __ _ _ __   __ _ _ __   ___  ___  ___    
    \ \/ _` | '_ \ / _` | '_ \ / _ \/ __|/ _ \   
 /\_/ / (_| | |_) | (_| | | | |  __/\__ \  __/   
 \___/ \__,_| .__/ \__,_|_| |_|\___||___/\___|   
            |_|                                  
   ___ _           _                       _     
  / __\ | __ _ ___| |__   ___ __ _ _ __ __| |___ 
 / _\ | |/ _` / __| '_ \ / __/ _` | '__/ _` / __|
/ /   | | (_| \__ \ | | | (_| (_| | | | (_| \__ \\
\/    |_|\__,_|___/_| |_|\___\__,_|_|  \__,_|___/
                                                 
    """)


# In[4]:


def goodbye_messsage():
    print("""
 __                                           _ 
/ _\ __ _ _   _  ___  _ __   __ _ _ __ __ _  / \\
\ \ / _` | | | |/ _ \| '_ \ / _` | '__/ _` |/  /
_\ \ (_| | |_| | (_) | | | | (_| | | | (_| /\_/ 
\__/\__,_|\__, |\___/|_| |_|\__,_|_|  \__,_\/   
          |___/                                     
    """)


# In[5]:


def dictionary_title():
    print("""
  ___ ___ ___ _____ ___ ___  _  _   _   _____   __
 |   \_ _/ __|_   _|_ _/ _ \| \| | /_\ | _ \ \ / /
 | |) | | (__  | |  | | (_) | .` |/ _ \|   /\ V / 
 |___/___\___| |_| |___\___/|_|\_/_/ \_\_|_\ |_|  
                                                      
    """)


# In[6]:


def complete_title():
    print("""
   ___                      _      _         _ 
  / __\___  _ __ ___  _ __ | | ___| |_ ___  / \\
 / /  / _ \| '_ ` _ \| '_ \| |/ _ \ __/ _ \/  /
/ /__| (_) | | | | | | |_) | |  __/ ||  __/\_/ 
\____/\___/|_| |_| |_| .__/|_|\___|\__\___\/   
                     |_|                       
    """)


# In[7]:


def excellent_title():
    print("""
   __              _ _            _   
  /__\_  _____ ___| | | ___ _ __ | |_ 
 /_\ \ \/ / __/ _ \ | |/ _ \ '_ \| __|
//__  >  < (_|  __/ | |  __/ | | | |_ 
\__/ /_/\_\___\___|_|_|\___|_| |_|\__|
                                      
 __    __           _      _          
/ / /\ \ \___  _ __| | __ / \         
\ \/  \/ / _ \| '__| |/ //  /         
 \  /\  / (_) | |  |   </\_/          
  \/  \/ \___/|_|  |_|\_\/            
                                          
    """)


# In[8]:

records_df = pd.read_csv("recordbook.csv", names=["deck", "questions", "time_seconds", "time_str"])

def print_records(df):
    print("===============================")
    print("         Record Book")
    print("===============================")
    for index, row in df.iterrows():
        print("Deck: ", row['deck'])
        print("    Questions: ", row['questions'])
        print("    Record: ", row['time_str'])
        print()
        
def validate_input_data(input_prompt: str, data_type: int, answer_range: list = None):
    error_flag = False

    if type(input_prompt) != str:
        raise Exception("Error: Input prompt needs to be a string.")
        error_flag = True
        
    if type(data_type) != int:
        raise Exception("Error: Data type needs to be a string.")
        error_flag = True

    if answer_range is not None:
        if type(answer_range) != list or len(answer_range) != 2:
            raise Exception("Error: The answer_range needs to be a list (2) ints in length.")
            error_flag = True
            
        else:
            if type(answer_range[0]) != int:
                raise Exception("Error: The lower limit of the answer_range needs to be an int.")
                error_flag = True
            if type(answer_range[1]) != int:
                raise Exception("Error: The upper limit of the answer_range needs to be an int.")
                error_flag = True
            if type(answer_range[0]) == int and type(answer_range[1]) == int :            
                if answer_range[0] > answer_range[1]:
                    raise Exception("Error: The lower limit of the answer_range list needs to be less than the higher limit.")
                    error_flag = True

    input_flag = False
    while input_flag == False:
        answer = input(input_prompt)

        ## data_types:
        ## 0 = str
        ## 1 = int
        if data_type == 0:
            if type(answer) == str:
                input_flag = True
                
        elif data_type == 1:
            try:
                answer = int(answer)
                if answer_range is not None:
                    if answer_range[0] <= answer <= answer_range[1]:
                        input_flag = True
                    else:
                        print("Input does not fall within specified range.  Check answer_range parameter input.")

                else:
                    input_flag = True
                
            except:
                print("Input cannot be converted to an int.  Check datatype parameter input.")

    return answer


# In[9]:


def save_dict_to_txt(input_dict, input_dict_file = None):
    if input_dict_file is None:  
        save_name = validate_input_data("Save As: ", 0)
        save_name += ".txt"
        
    else:
        overwrite_option = validate_input_data("Do you want to overwrite the file? (Y/N): ", 0)       
        if overwrite_option.lower() == "y" or save_option.lower() == "yes":
            save_name = input_dict_file
        else:
            save_name = validate_input_data("Save As: ", 0)
            save_name += ".txt"

    with open(save_name, 'w') as f:  
        for key, value in input_dict.items():  
            f.write("{}: {}\n".format(key, value))
            
    print("File {} saved!".format(save_name))
    print()


# In[10]:


def select_deck():
    result_dict = {}

    files = [file for file in os.listdir() if file[-4:] == '.txt']
    files.append("Create New Deck")
    print("Flashcard Decks:")
    print()
    file_index = 0
    for file in files:
        print(str(file_index + 1)+".", file)
        file_index += 1
    print()
    deck_selection = validate_input_data("Select a deck: ", 1, [1, len(files)])
    print()
    filename = files[int(deck_selection)-1]


    if filename != files[-1]:   
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if line:  # Skip empty lines
                    key, value = line.split(":")
                    result_dict[key.strip()] = value.strip()
        return result_dict, filename
        
    else:
        dict_name = validate_input_data("Save As: ", 0)
        dict_name += ".txt"
        return result_dict, dict_name


# In[1]:


def train_dict(input_dict, dict_name, rec_df):
    
    if len(input_dict) == 0:
        print("There are no cards in the current deck.  Add some!")
        print()
        
    else:
        rand_order = rd.sample(list(input_dict.keys()), len(input_dict))
    
        incorrect = []

        start_time = time.time()
        
        for item in rand_order:
            
            print(item + ": ")
            answer = input()
    
            
            if input_dict[item].lower() != answer.lower():
                print("Not quite!")
                print("-----------")
                incorrect.append(item)
            else:
                print("Correct!")
                print("-----------")
               
        print()
        end_time = time.time()
        elapsed_seconds = int(end_time - start_time)
        # Calculate hours, minutes, and seconds
        hours, remainder = divmod(elapsed_seconds, 3600)  # 1 hour = 3600 seconds
        mins, secs = divmod(remainder, 60)  # 1 minute = 60 seconds

        time_parts = []
        if hours:
            time_parts.append(f"{hours} hrs")
        if mins:
            time_parts.append(f"{mins} mins")
        time_parts.append(f"{secs} secs")

        com_time = " ".join(time_parts)  # Join the parts into a single string
        # Format output

        complete_title()
        print("**************************")
        print("Score: ", str(round((((len(input_dict) - len(incorrect))/len(input_dict)) * 100), 2))+"%", "(",
        len(input_dict) - len(incorrect), "/", len(input_dict), ")")
        print("Completion Time: ", com_time)
        if (len(input_dict) - len(incorrect)) == len(input_dict):
            if dict_name not in rec_df['deck'].unique():
                print('***New Record!**')
                new_rec = {'deck': dict_name, 'questions': len(input_dict),
                           'time_seconds': elapsed_seconds, 'time_str': com_time}
                # Add the new row using loc (next available index)
                rec_df.loc[len(rec_df)] = new_rec
                rec_df.to_csv('recordbook.csv', index= False, header= False)

            elif elapsed_seconds < rec_df[rec_df['deck'] == dict_name]['time_seconds'].values[0]:
                print('**New Record!**')
                rec_df.loc[rec_df['deck'] == dict_name, 'questions'] = len(input_dict)
                rec_df.loc[rec_df['deck'] == dict_name, 'time_seconds'] = elapsed_seconds
                rec_df.loc[rec_df['deck'] == dict_name, 'time_str'] = com_time
                rec_df.to_csv('recordbook.csv', index= False, header= False)

        print("**************************")
        print()
    
        if len(incorrect) > 0:
            save_incorrect_option = validate_input_data("Would you like to save your incorrect words for practice? (Y/N):", 0)
            if save_incorrect_option.lower() == "y" or save_incorrect_option.lower() == "yes":
                incorrect_dict = {}
                for entry in incorrect:
                    incorrect_dict[entry] = input_dict[entry]
                save_dict_to_txt(incorrect_dict)
            
            stop_practice = False
            while stop_practice != True:
                if len(incorrect) > 0:
                    corrected = []
                    practice_incorrect = validate_input_data("Would you like to practice the ones you missed? (Y/N):", 0)
                    if practice_incorrect.lower() == "y" or practice_incorrect.lower() == "yes":           
                        for item in incorrect:
                            print(item + ": ")
                            answer = input()
                            if input_dict[item].lower() != answer.lower():
                                print("Not quite!")
                                print("Answer: ", input_dict[item])
                                print("-----------")
                            else:
                                print("Correct!")
                                print("-----------")
                                corrected.append(item)
                                
                        incorrect = [x for x in incorrect if x not in corrected]
                        
                    else:
                        stop_practice = True
                else:
                    stop_practice = True
                    excellent_title()
        else:
            excellent_title()
        


# In[12]:


def view_dict(input_dict):
    counter = 1
    dictionary_title()
    print("(English --> Japanese)")
    print("")
    for key, value in input_dict.items():
        print(str(counter) + ". ", key, "-->", value)
        counter += 1
    print()


# In[13]:


def add_word(input_dict):
    print("Adding a word!")
    word_to_add_eng = input("What is the word in English?: ")
    word_to_add_jap = input("What is the word in Japanese?: ")
    print("---------------------------------")
    print()
    print("Adding: ", word_to_add_eng, "-->", word_to_add_jap)
    print()
    confirm = input("Is this correct? (Y/N): ")
    print()
    if confirm.lower() == "yes" or confirm.lower() == "y":
        input_dict[word_to_add_eng] = word_to_add_jap
        print("Word has been added!")
        print()
    else:
        print("Resetting!")
        print()
        add_word(input_dict)
    return input_dict


# In[14]:


def remove_word(input_dict):
    counter = 0
    print("Which word would you like to remove?")
    input_keys = list(input_dict.keys())
    for key in input_keys:
        print(str(counter+1) + "." , key, "-->", input_dict[key])
        counter += 1
    index_remove = validate_input_data("Enter the number: ", 1, [1, len(input_dict)])
    confirm_remove = input("Are you sure you want to remove {} --> {}? (Y/N): ".format(input_keys[int(index_remove)-1], input_dict[input_keys[int(index_remove)-1]]))
    if confirm_remove.lower() == "y" or confirm_remove.lower() == "yes":
        input_dict.pop(input_keys[int(index_remove)-1])
        print("Word has been removed!")
        print()
    else:
        print("Canceled removal.")
        print()
    return input_dict


# In[1]:


title_message()
values_dict, dict_file = select_deck()
print()
while int(selection) != 7:
    print("Selected Deck: ", dict_file)
    print()
    selection = validate_input_data("""Select an option:
    
    1. Train Words
    2. View Words
    3. Add Words
    4. Remove Words
    5. Change Deck
    6. View Record Book
    7. Exit
    
    """, 1, [1,7])

    print()

    ##Exit option
    if selection == 7:
        save_option = input("Would you like to save the list? (Y/N): ")
        print()
        if save_option.lower() == "y" or save_option.lower() == "yes":
            save_dict_to_txt(values_dict, dict_file)        
        goodbye_messsage()

    ##Input validation
    elif selection not in [1, 2, 3, 4, 5, 6]:
        print()
        print("Invalid selection.  Try again.")

    ##Train with the words
    elif selection == 1:
        train_dict(values_dict, dict_file, records_df)

    ##View the words
    elif selection == 2:
        view_dict(values_dict)
        
    ##Add a word
    elif selection == 3:
        values_dict = add_word(values_dict)

    ##Remove a word
    elif selection == 4:
        values_dict = remove_word(values_dict)

    ##Change Decks
    elif selection == 5:
        save_option = input("Would you like to save the current deck {}? (Y/N): ".format(dict_file))
        print()
        if save_option.lower() == "y" or save_option.lower() == "yes":
            save_dict_to_txt(values_dict, dict_file)
        values_dict, dict_file = select_deck()

    elif selection == 6:
        print_records(records_df)
