import os

# 定义多语言支持
LANGUAGES = {
    "en": {
        "welcome": "--- YoLang Editor ---",
        "options": "\nOptions:\n1. Open a .yl file\n2. Edit a .yl file\n3. Save a .yl file\n4. Run YoLang code\n5. Change Language\n6. Exit",
        "choice": "Enter your choice: ",
        "open_file": "Enter the YoLang file name to open (.yl): ",
        "file_not_found": "Error: File not found.",
        "file_opened": "File '{filename}' opened successfully.",
        "save_file": "Enter the file name to save as (.yl): ",
        "file_saved": "File saved as '{filename}'.",
        "edit_prompt": "Enter new content below (type ':wq' to save and exit):",
        "run_code": "Running YoLang code...",
        "no_file_opened": "Error: No file opened.",
        "no_file_to_save": "Error: No file to save.",
        "exit": "Exiting YoLang Editor.",
        "invalid_choice": "Invalid choice. Please try again.",
        "change_language": "Available languages: en(English), zh-cn(Chinese). Enter language code: ",
        "language_changed": "Language changed to English.",
    },
    "zh-cn": {
        "welcome": "--- YoLang 编辑器 ---",
        "options": "\n选项:\n1. 打开 .yl 文件\n2. 编辑 .yl 文件\n3. 保存 .yl 文件\n4. 运行 YoLang 代码\n5. 切换语言\n6. 退出",
        "choice": "请输入你的选择: ",
        "open_file": "请输入要打开的 YoLang 文件名 (.yl): ",
        "file_not_found": "错误: 文件未找到。",
        "file_opened": "文件 '{filename}' 打开成功。",
        "save_file": "请输入要保存的文件名 (.yl): ",
        "file_saved": "文件已保存为 '{filename}'。",
        "edit_prompt": "在下方输入新内容 (输入 ':wq' 保存并退出):",
        "run_code": "正在运行 YoLang 代码...",
        "no_file_opened": "错误: 未打开任何文件。",
        "no_file_to_save": "错误: 没有文件可保存。",
        "exit": "正在退出 YoLang 编辑器。",
        "invalid_choice": "无效的选择，请重试。",
        "change_language": "可用语言: en(英文), zh-cn（中文）。请输入语言代码: ",
        "language_changed": "语言已切换为zh-cn。",
    }
}

# 默认语言
current_language = "en"

def translate(key, **kwargs):
    """根据当前语言获取翻译"""
    return LANGUAGES[current_language][key].format(**kwargs)

def run_yolang_code(code):
    """运行 YoLang 代码的简单解释器"""
    if "textshow(" in code:
        start_index = code.index("textshow(") + 9
        end_index = code.index(")", start_index)
        content = code[start_index:end_index]
        text = input('show text: ')
        print(text)
    elif "numbershow()" in code:
        num1 = input('show number: ')
        print(eval(num1))
    elif "textinput(" in code:
        start_index = code.index("textinput(") + 10
        end_index = code.index(")", start_index)
        prompt = code[start_index:end_index]
        result = input(prompt)
        print(result)
    else:
        print("Error: Unknown YoLang Command.")

def open_file():
    """打开一个 .yl 文件"""
    filename = input(translate("open_file"))
    if not filename.endswith(".yl"):
        print("Error: Please provide a .yl file.")
        return None
    if not os.path.exists(filename):
        print(translate("file_not_found"))
        return None
    with open(filename, "r") as file:
        content = file.read()
    print(translate("file_opened", filename=filename))
    return content, filename

def save_file(content, filename=None):
    """保存到 .yl 文件"""
    if not filename:
        filename = input(translate("save_file"))
        if not filename.endswith(".yl"):
            filename += ".yl"
    with open(filename, "w") as file:
        file.write(content)
    print(translate("file_saved", filename=filename))

def edit_file(content):
    """编辑文件内容"""
    print("Current content:")
    print(content)
    print("\n" + translate("edit_prompt"))
    new_content = []
    while True:
        line = input()
        if line == ":wq":
            break
        new_content.append(line)
    return "\n".join(new_content)

def change_language():
    """切换语言"""
    global current_language
    new_language = input(translate("change_language"))
    if new_language in LANGUAGES:
        current_language = new_language  
        print(translate("language_changed", language=LANGUAGES[new_language]["welcome"]))
    else:
        print(translate("invalid_choice"))  

def main():
    print(translate("welcome"))
    while True:
        print(translate("options"))
        choice = input(translate("choice"))
        
        if choice == "1":
            result = open_file()
            if result:
                content, filename = result
        elif choice == "2":
            if 'content' in locals():
                content = edit_file(content)
            else:
                print(translate("no_file_opened"))
        elif choice == "3":
            if 'content' in locals():
                save_file(content, filename if 'filename' in locals() else None)
            else:
                print(translate("no_file_to_save"))
        elif choice == "4":
            if 'content' in locals():
                print(translate("run_code"))
                run_yolang_code(content)
            else:
                print(translate("no_file_opened"))
        elif choice == "5":
            change_language()
        elif choice == "6":
            print(translate("exit"))
            break
        else:
            print(translate("invalid_choice"))

if __name__ == "__main__":
    main()