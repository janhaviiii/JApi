# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import click

@click.command()
@click.option('--directory', '-d', help="Directory name", default="Backend")
@click.option('--subdirectory', '-s', help="Sub-Directory name", default="Base")
@click.option('--append', '-a', default=False, is_flag=True)
@click.option('--class_name', '-c', help="Class name", default=None)
@click.option('--user_id', '-uid', help="UserId", default="id")
@click.option('--init', '-i', default=False, is_flag=True)
@click.option('--json_path', '-j', help="Json Path", default=None)
def print_hi(directory, subdirectory, init, append, class_name, user_id, json_path):
        if init:
            print(f'{directory}')
            print(f'{subdirectory}')

        if append:
            if json_path is None:
                print(f'Provide JsonPath with --append using --json_path option')
                return
            if class_name is None:
                class_name = json_path.split('/')[-1].split('.')[0]
            print(json_path)
            print(f'{class_name}')
            print(f'{user_id}')




if __name__ == '__main__':
    print_hi()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
