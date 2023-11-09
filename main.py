import app.download


def main():
    app.download.get_target_path(input(f'\n[+] Выберите варианты загрузки:\n\t[1] Загрузить видео\n'
                                       f'\t[2] Загрузить видео из списка\n\t[3] Загрузить плейлист\n\t[4] Выход\n\t>>> '))


if __name__ == "__main__":
    main()
