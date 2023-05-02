'''def threeSum( nums):
	"""
	:type nums: List[int]
	:rtype: List[List[int]]
	"""
	ans = []
	nums.sort()
	for i in range(len(nums)-2):
		a = nums[i]
		start = i + 1
		end = len(nums) - 1
		while start < end:
			b = nums[start]
			c = nums[end]
			if a + b + c == 0:
				if [a, b, c] not in ans:
					ans.append([a, b, c])
				start += 1
				end -= 1
			elif a + b + c > 0:
				end -= 1
			else:
				start += 1
	return ans 

nums = [-1,0,1,2,-1,-4]
s = threeSum(nums)
print(s)'''


'''def max(l):
    if not l:
        return None
    else:
        res = l[0]
        for i in range(1,len(l)):
            if l[i]>res:
            	res  = l[i]
        return res
		
            
l = [12,20,24,23,12,10,8]
s = max(l)
print(s)'''
             

'''def arrayequal(a,b):
    	
    for i in range(1,len(a)):
        for i in range(1,len(b)):
            if a[i] == b[i]:
                return True
            else:
                return False
	
        
n = int(input("enter value: "))

a = list(map(int, input(" ").split()))
b = list(map(int, input(" ").split()))
print(a,b)
x =  sorted(a)
y = sorted(b)   
print(x,y)      
s = arrayequal(x,y)
print(s)              




def check(A,B):
    
    x =  sorted(A)
    y = sorted(B)   
    
    
    for i in range(1,len(A)):
        for i in range(1,len(B)):
            if x[i] == y[i]:
                return True
            else:
                return False
	
        
N = int(input("enter value: "))

U = list(map(int, input(" ").split()))
V = list(map(int, input(" ").split()))


s = check(U,V)
print(s) '''



import json
import os
import time
import webbrowser
import sys
import re


def handleWindows(extra_seconds):
    print("OS : Windows")
    local_settings = r"{}\Balsamiq\Balsamiq Wireframes\LocalSettings.json".format(os.getenv('APPDATA'))
    print("Reading from {}".format(local_settings))
    with open(local_settings) as reader:
        json_data = json.load(reader)
    json_data['DefaultSelectionColorRGBA'] = int(time.time()) + extra_seconds
    print("Writing to {}".format(local_settings))
    with open(local_settings, 'w') as outfile:
        json.dump(json_data, outfile)


def handleMacos(trial_days_left=30, debug_mode=False):
    print("OS : macOS")
    print("Debug Mode: " + str(debug_mode))

    def dump_debug(start_func, end_func, content_func, new_func):
        print("function start line: {}".format(start_func))
        print("function end line: {}".format(end_func))
        print("function content:")
        print(content_func)
        print("new function content:")
        print(new_func)

    editor_macos = "/Applications/Balsamiq Wireframes.app/Contents/Resources/editor-macos.js"
    editor_macos_test = r"C:\Users\housi\Desktop\Balsamiq\editor-macos-test.js"
    if debug_mode:
        editor_macos = editor_macos_test
    print(editor_macos)
    if not os.path.exists(editor_macos):
        print("editor-macos.js NOT FOUND!")
        exit(0)
    get_trial_days_left_pattern = re.compile(r"\s*function\s+getTrialDaysLeftFromNativeData\(\w+\)\s*{")
    func_start_line = -1
    func_end_line = -1
    found_a_match = False
    function_content = ""
    with open(editor_macos, encoding="utf8") as reader:
        line_number = 0
        # it starts at 1 because w have already matched one '{'
        curly_braces_balance = 1
        for line in reader.readlines():
            line_number += 1
            if not found_a_match:
                match = get_trial_days_left_pattern.match(line)
                if match is not None:
                    found_a_match = True
                    func_start_line = line_number
                    # TODO what if the start line is also the end line, One-Liner function

            else:
                curly_braces_balance += line.count("{")
                curly_braces_balance -= line.count("}")
                if curly_braces_balance == 0:
                    function_content = function_content + line
                    func_end_line = line_number
                    break
            if func_start_line != -1:
                function_content = function_content + line

    body = "return {};".format(trial_days_left)
    new_function_signature = "\nfunction getTrialDaysLeftFromNativeData(nativeData) {\n\t" + body + "\n}\n\n"

    if debug_mode:
        dump_debug(func_start_line, func_end_line, function_content, new_function_signature)

    with open(editor_macos, encoding="utf8") as reader:
        lines = reader.readlines()

    # The first -1 to make it base 0 and the second one refers to the previous index
    index = (func_start_line - 1) - 1
    leading_count = 0
    # Removing leading blank lines before the function definition
    while not lines[index].strip():
        lines.pop(index)
        index -= 1
        leading_count += 1

    # The start and end indexes will change after removing the leading blank lines
    func_start_line -= leading_count
    func_end_line -= leading_count

    # Removing trailing blank lines after the function end
    index = func_end_line
    while not lines[index].strip():
        lines.pop(index)

    # Removing the old function
    for i in range(func_end_line - func_start_line + 1):
        lines.pop(func_start_line - 1)

    # Replacing it with the new function
    lines.insert(func_start_line - 1, new_function_signature)

    # Writing changes back to file
    with open(editor_macos, "w", encoding="utf8") as f:
        lines = "".join(lines)
        f.write(lines)


print("IMPORTANT! please make sure to close Balsamiq before proceeding or the script won't have any effect")
years = int(input("How many years of trial do you want :) "))

if sys.platform.startswith("win"):
    handleWindows(years * 365 * 24 * 60 * 60)
elif sys.platform.startswith("darwin"):
    handleMacos(years * 365)
else:
    print("Sorry, operating system not supported")
    exit(0)

print("****************************************************************")
print("* Congratulations! You gained {} days of trial".format(years * 365))
print("* Please don't forget to leave a star ✭")
print("****************************************************************")
print("https://gist.github.com/HoussemNasri/c09e55e0e5f451aa10f8621a6680ba28")
webbrowser.open("https://gist.github.com/HoussemNasri/c09e55e0e5f451aa10f8621a6680ba28")
input("Press ENTER to exit")