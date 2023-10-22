import re


def copy_file_with_new_number(input_file, output_file, num_copies):
    with open(input_file, 'r') as input_f:
        content = input_f.read()

        match = re.search(r'(gloey)(\d+)', content)

        if match:
            keyword = match.group(1)
            current_number = int(match.group(2))

            for copy_number in range(current_number, current_number + num_copies):
                new_number = copy_number
                updated_content = re.sub(f'{keyword}{current_number}', f'{keyword}{new_number}', content)
                output_file_copy = f'{output_file}_{copy_number}.txt'

                with open(output_file_copy, 'w') as output_f:
                    output_f.write(updated_content)
        else:
            for copy_number in range(1, num_copies + 1):
                output_file_copy = f'{output_file}_{copy_number}.txt'
                with open(output_file_copy, 'w') as output_f:
                    output_f.write(content)


if __name__ == '__main__':
    input_file = 'input.txt' # Путь к исходному файлу
    output_file = 'output' # Название копии
    num_copies = 3  # Количество копий

    copy_file_with_new_number(input_file, output_file, num_copies)