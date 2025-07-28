import os

extensions = {}
logging = False
#EXT_TO_MOVE = ['.mp4', '.mov', '.MP4', '.GIF', '.gif']


def review(root, cmd):
    os.chdir(root)

    path_to_log = root + ' log.txt'
    log = open(path_to_log, 'w', encoding='utf8')
    log.write(root + 4 * '\n')

    for path, dirs, files in os.walk(os.getcwd()):
        for file in files:
            _, file_extension = os.path.splitext(path + '\\' + file)
            file_ext = file_extension.lower()
            if file_ext in extensions.keys():
                extensions[file_ext].append(path + '\\' + file)
            else:
                extensions[file_ext] = [path + '\\' + file]

    log.write('extensions: \n')
    for key in extensions.keys():
        log.write(f'{key} - {len(extensions[key])}\n')
    log.write('\n' * 3)
    for key in extensions.keys():
        print(f'{key} amount = {len(extensions[key])}\n')
        log.write(f'{key} amount = {len(extensions[key])}\n\n')
        for file in extensions[key]:
            print(file)
            log.write(file)
            log.write('\n')
        log.write('\n' * 3)

def lookup(root, ext, path_to_move):
    os.chdir(root)
    try:
        os.mkdir(path_to_move)
    except FileExistsError:
        print(f"Directory '{path_to_move}' already exists.")
    except PermissionError:
        print(f"Permission denied: Unable to create '{path_to_move}'.")
    except Exception as e:
        print(f"An error occurred: {e}")

    path_to_log = root + ' log.txt'
    log = open(path_to_log, 'w', encoding='utf8')
    log.write(root + 4 * '\n')

    path_to_log_mover = root + " log_mover.txt"
    log_mover = open(path_to_log_mover, 'w', encoding='utf8')
    log_mover.write(root + 4 * '\n')

    for path, dirs, files in os.walk(os.getcwd()):
        for file in files:
            _, file_extension = os.path.splitext(path + '\\' + file)
            file_ext = file_extension.lower()
            if file_ext in extensions.keys():
                extensions[file_ext].append(path + '\\' + file)
            else:
                extensions[file_ext] = [path + '\\' + file]

    log.write('extensions: \n')
    for key in extensions.keys():
        log.write(f'{key} - {len(extensions[key])}\n')
    log.write('\n' * 3)
    for key in extensions.keys():
        log.write(f'{key} amount = {len(extensions[key])}\n\n')
        for file in extensions[key]:
            log.write(file)
            log.write('\n')
        log.write('\n' * 3)

    counter = 0
    for key in extensions.keys():
        if key in ext:
            for file in extensions[key]:
                counter += 1
                to_path = path_to_move + '\\' + f'{counter} ' + file.split('\\')[-1]
                log_mover.write(f'from\t@####@{file}\n')
                log_mover.write(f'to\t\t@####@{to_path}\n')
                os.rename(file, to_path)
        else:
            continue

    log.close()
    log_mover.close()


def delookup(root, pathlog):
    os.chdir(root)
    log = open(pathlog + ' log_mover.txt', 'r', encoding='utf8')

    for line in log:
        if '@' in line:
            path_from = line.split('@####@')[-1][:-1]
            path_to = log.readline().split('@####@')[-1][:-1]
            try:
                os.rename(path_to, path_from)
            except FileNotFoundError:
                print(f'File Not Found\n{path_to}\n{path_from}')
            except PermissionError:
                print(f'Permission Error:\n{path_to}\n{path_from}')
            except Exception as e:
                print(f'Exception: {e}\n{path_to}\n{path_from}')
        else:
            continue

    log.close()


root_path = input("root path:\n")[1:-1]
path_to_move = '\\'.join(root_path.split('\\')[:-1]) + '\\.moved ' + root_path.split('\\')[-1]
choice = int(input('Actions:\n'
                   '1 - Review\n'
                   '2 - Move extensions\n'
                   '3 - Demove extensions\n'))

if choice == 1:
    cmd_out = bool(input('terminal output? 1 - yep; 0 - nope\n'))
    review(root_path, cmd_out)
elif choice == 2:
    EXT_TO_MOVE = list(input('extensions to move (format: .mp4 .gif):').split(' '))
    lookup(root_path, EXT_TO_MOVE, path_to_move)
elif choice == 3:
    delookup(path_to_move, root_path)
else:
    print('error')
