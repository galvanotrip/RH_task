**NAME**

	test_task.py - script that searches matches for provided regular expression in provided file(s) name.
	
**SYNOPSIS**

	test_task.py -rf[u|c|m] REGEXSP FILE... 

**DESCRIPTION**

	Read provided file(s) and compare with provided Regular Expression and then print matched lines.
	
	If no OPTIONS are supplied, will be requested to provide the needful information.
	Files must be in the same directory as the script.
	
**OPTIONS**
	
	-r, --regex	
			Read Regular Expression from REGEXSP
			Wihtout REGEXP, no results will provided
	
	-f, --file
			Read File(s) name(s) from FILE
			With wrong File name will shown 'No such file or directory' message.


	
	-u, --underscore
			Prints '^' under the matching text
	
	-c, --color
			Highlight matching text
			Works with linux only.
	
	-m, --machine
			Generate machine readable output in format: file_name:no_line:start_pos:matched_text
				  
**EXIT STATUS**

		0      Successful program execution.

		2      One of the arguments was not matched.

		3     At least one of the pages/files/keywords didn't exist or wasn't matched.

				  
**EXAMPLES**

        - test_task.py -rfu \d my_file my_file2
	
		my_file 4  # line 4 123
		                  ^ ^^^
		my_file 5  test 123
		                ^^^
		my_file 6  test_123
		                ^^^
		my_file2 7  # line 7 test for file2
		                   ^              ^
	
	- test.py -fr \d   my_file my_file#
		my_file 4 # line 4 123
		my_file 5 test 123
		my_file 6 test_123
		Error:  No such file or directory : "my_file#"

	test.py -fra \d   my_file my_file2
		Error:  option -a not recognized

	test.py --file --regex --underscore \d   my_file my_file2
		my_file 4  # line 4 123
		                  ^ ^^^
		my_file 5  test 123
		                ^^^
		my_file 6  test_123
		                ^^^
		my_file2 7  # line 7 test for file2
		                   ^              ^
