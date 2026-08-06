import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    working_dir_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_dir_abs, directory))

    # Check the validity of the target directory
    valid_target_dir = os.path.commonpath([working_dir_abs, target_dir]) == working_dir_abs

    # Catch and return any erros.
    try:
        if valid_target_dir == False:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        elif valid_target_dir == True:
            if os.path.isdir(target_dir) == False:
                return f'Error: "{directory}" is not a directory'
            else:
                # BUild a return string.
                result = ""

                # if it is a valid procede.
                for each in os.listdir(target_dir):
                    result += f"  - {os.path.join(target_dir, each)}: file_size={os.path.getsize(os.path.join(target_dir, each))}, is_dir={os.path.isdir(os.path.join(target_dir, each))}\n"
                return result
    except Exception as e:
        return f"Error: {e}"
