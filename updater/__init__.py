import updater

def updater_main():
    try:
        updater.start()
    except Error:
        print("Updater failed.")

# The Upader starts here
if __name__ == '__main__':
    updater_main()



