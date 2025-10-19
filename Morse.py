print("Conditions :\n"
      "1. Only use letters and numbers.\n"
      "2. Only use dots and dashes.\n"
      "3. Only use spaces between words in text.\n"
      "4. Use space to separate the letters and '/' to separate words in Morse code.\n"
      "5. Only spaces to separate words in text file.\n")

a = input("Enter text or Morse code: ").strip()

lt1 = [' ','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
       '0','1','2','3','4','5','6','7','8','9','.','?',"'",'!','/','(',')','&',':',';','=','+','-','_','"','$','@']

lt2 = ['/', '.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', 
       '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..',
       '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.',
       '.-.-.-', '..--..', '.----.', '-.-.--', '-..-.', '-.--.', '-.--.-', '.-...', '---...', '-.-.-.', '-...-', 
       '.-.-.', '-....-', '..--.-', '.-..-.', '...-..-', '.--.-.']

while True:
    a = input("Enter text or Morse code : ").strip()
    if a.lower() == "exit":
        print("Program exited.")
        break
    olt = []

    is_morse = all(c in '.-/ ' for c in a)
    is_text = all(c.upper() in lt1 for c in a)

    if is_morse:
        words = a.split('/')
        for word in words:
            letters = word.strip().split(' ')
            for letter in letters:
                if letter:
                    if letter in lt2:
                        olt.append(lt1[lt2.index(letter)])
                    else:
                        olt.append('?')
            olt.append(' ')
        print(''.join(olt).strip())

    elif is_text:
        a = a.upper()
        for char in a:
            if char == ' ':
                olt.append('/')
            else:
                if char in lt1:
                    olt.append(lt2[lt1.index(char)])
                else:
                    olt.append('?')
        print(' '.join(olt))
    else:
        print("Invalid input! Please enter valid text or Morse code.")
        