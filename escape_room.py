from colorama import Fore, Back
import cv2

answer = 'abcde'
new_line="\n==>"
n_fails = 0
hints = [
    f"{Back.LIGHTWHITE_EX} {Fore.BLACK} La longueur du mot de passe est 5. {Back.RESET} {Fore.RESET}",
    f"{Back.LIGHTWHITE_EX} {Fore.BLACK} Le mot de passe est uniquement composé de lettres. {Back.RESET} {Fore.RESET}",
    f"{Back.LIGHTWHITE_EX} {Fore.BLACK} La première lettre du mot de passe est <a>. {Back.RESET} {Fore.RESET}",
    f"{Back.LIGHTWHITE_EX} {Fore.BLACK} La toisième lettre du mot de passe est <c>. {Back.RESET} {Fore.RESET}"
]

def get_hint():
    while True:
        hint = input(f"Vous avez décidé de prendre un indice.\nVous avez le droit d'obtenir maximum 4 indices différents au total.\nEntrez un numéro entre {Fore.LIGHTBLUE_EX} 1 {Fore.RESET} et {Fore.LIGHTBLUE_EX} 4 {Fore.RESET} pour obtenir un indice.\n==>")
        print()
        if (hint == "1" or hint == "2" or hint == "3" or hint == "4"):
            print(f"Voici l'indice {hint}:\n{hints[int(hint)-1]}")
            print()
            break
        else:
            print("Le numéro que vous avez entré n'est pas valide.")
            print()

def ending():
    # Load the video
    cap = cv2.VideoCapture('simple_name.mp4')

    # Check if video opened successfully
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    # Read and display frame by frame
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break

        cv2.imshow('Frame', frame)

        # Press 'q' to quit
        if cv2.waitKey(1) == ord('q'):
            break

    # When everything done, release the video capture object
    cap.release()
    cv2.destroyAllWindows()
    

while True:
    obtained=input("Veuillez entrer le mot de passe:\n==>")
    print()
    if (obtained.lower().strip() == answer):
        ending()
        break
    else:
        n_fails += 1
        if (n_fails == 3 or n_fails >= 3):
            confirmation = input(f"Raté, le code que vous avez rentré n'est pas correct.\nBesoin d'un coup de pouce? Entrez {Fore.LIGHTGREEN_EX} oui {Fore.RESET} pour avoir un indice, entrez {Fore.LIGHTRED_EX} non {Fore.RESET} dans le cas contraire.\n==>")
            print()
            while True:
                if (confirmation.lower().strip() == "oui"):
                    get_hint()
                    break
                elif (confirmation.lower().strip() == "non"):
                    print("Pas de problèmes!")
                    print()
                    break
                else: 
                    confirmation = input(f"Votre réponse n'est pas valide. Veuillez entrer {Fore.LIGHTGREEN_EX} oui {Fore.RESET} pour avoir un indice, {Fore.LIGHTRED_EX} non {Fore.RESET} dans le cas contraire.\n==>")
                    print()
        else: 
            print("Raté, le code que vous avez rentré n'est pas correct...\n")
        