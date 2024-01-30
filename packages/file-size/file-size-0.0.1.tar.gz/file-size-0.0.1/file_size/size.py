import os

def file_size(file_path):
    try:
        size_b = os.path.getsize(file_path)
        size_bits = size_b * 8
        size_kb = size_b / 1024
        size_mb = size_kb / 1024
        size_gb = size_mb / 1024
        size_tb = size_gb / 1024
        size_pb = size_tb / 1024
        print('*' * 60)
        print(f'The file size in bits: {size_bits}b\n'
                f'The file size in Bytes: {size_b}B\n'
                f'The file size in Kilobytes: {size_kb:.2f}KB\n'
                f'The file size in Megabytes: {size_mb:.2f}MB\n'
                f'The file size in Gigabytes: {size_gb:.3f}GB\n'
                f'The file size in Terabytes: {size_tb:.4f}TB\n'
                f'The file size in Petabytes: {size_pb:.7f}PB\n\n'
                f'File analysed path: {file_path}\n')
        print('*' * 60)

    except FileNotFoundError:
        print('*' * 60)
        print("\nThe file wasn't found\n")
        print('*' * 60)

    except Exception as e:
        print(f'An error occurred while analyzing the file: {file_path}:\n {e}')
