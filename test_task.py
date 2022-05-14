#!/usr/bin/python3

# It is using 'Chain of responsibility' pattern

import sys
import getopt
import re

argv = sys.argv  # argv[0] is a script path and name


def read_file(file):
    with open(file, "r") as file:
        file_data = file.read().split('\n')
    return file_data


def f_arg_check(opts):
    for opt, arg in opts:
        if opt == '-f' or opt == '--files':
            return args_regex_file[1:]
    file_name= input('\nPlease type File(s) names you want to check.\n'
                      'Names should be separated with space: ')

    return file_name.split(' ')


def r_arg_check(opts):
    for opt, arg in opts:
        if opt == '-r' or opt == '--regex':
            return args_regex_file[0]

    regex = input('\nPlease type Regular expression you want to check: ')
    return regex


def match_pos(regex, text_line):
    regex_sav = re.compile(regex)
    iterator = regex_sav.finditer(text_line)
    match_pos_list = []
    for match in iterator:
        match_pos_list.append(match.span())
    return match_pos_list


def colorise_matches(text_line, pos):
    first_pos = 0
    print(answer_line, end='')
    for start_pos, end_pos in pos:
        print(text_line[first_pos:start_pos], end='')
        print('\x1b[6;30;42m' + text_line[start_pos:end_pos] + '\x1b[0m', end='')  # linux only
        first_pos = end_pos
    print(text_line[first_pos:])
    return text_line


def machine_output(pos):
    print(f'{file}:{line_num + 1}', end='')
    for start_pos, end_pos in pos:
        matched_text = text_line[start_pos:end_pos]
        print(f':{start_pos}:{matched_text}', end='')
    print()


def underscore_matches(pos):
    print(answer_line, text_line)
    output = ' ' * (len(answer_line) + 1)
    for i in range(len(text_line)):
        for start_pos, end_pos in pos:
            if start_pos <= i <= (end_pos - 1):
                output += '^'
                break
        else:
            output += ' '
    print(output)


try:
    opts, args_regex_file = getopt.getopt(argv[1:], "rfucm",
                                          ['regex', 'files', 'underscore', 'color', 'machine'])

except getopt.GetoptError as err:
    print('Error: ', err)  # output example:  "option -a not recognized"
    sys.exit(2)

regex = r_arg_check(opts)
for file in f_arg_check(opts):
    try:
        text_list = read_file(file)
        for line_num in range(len(text_list)):

            text_line = text_list[line_num]

            pos = match_pos(regex, text_line)
            if pos == []:  # if there are(is) no matches in line.
                continue
            else:
                answer_line = f'{file} {line_num + 1} '

            for opt, arg in opts:
                if opt in ('-c', '--color'):
                    colorise_matches(text_line, pos)
                    break

                elif opt in ('-m', '--machine'):
                    machine_output(pos)
                    break

                elif opt in ('-u', '--underscore'):
                    underscore_matches(pos)
                    break

            else:
                print(answer_line + text_line)

    except Exception as exc:
        print('Error: ', exc.args[1], f': "{file}"', )
        sys.exit(3)
#print('Execution finished.')
sys.exit(0)
