from functions.get_files_info import get_files_info

def print_results(working_directory: str, directory: str = "."):
    result = get_files_info(working_directory, directory)
    print(f'Result for "{directory}":')
    print(result)

print_results("calculator", ".")
print_results("calculator", "pkg")
print_results("calculator", "/bin")
print_results("calculator", "../")
