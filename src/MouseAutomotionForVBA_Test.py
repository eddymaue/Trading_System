# MouseAutomotionForVBA_Test.py

import sys

if __name__ == "__main__":
    # Chemin complet du fichier de positions
    file_path = r"C:\Users\eddym\PycharmProjects\pythonProject\BoursePlacerSurGraphiqueListeSymbolFromClipBoard\MouseRecorderData\MousePutSymbol4Chart.txt"

    # Simuler des symboles de test
    test_symbols = "AAPL MSFT GOOGL AMZN"

    # Construire les arguments comme le ferait VBA
    args = [
        r"C:\Users\eddym\PycharmProjects\pythonProject\BoursePlacerSurGraphiqueListeSymbolFromClipBoard\MouseAutomotionForVBA.py",
        file_path,
        "0",  # pas de confirmation
        "0",  # pas de click position original
        test_symbols
    ]

    # Appeler le script avec ces arguments
    print("Test avec les symboles:", test_symbols)
    sys.argv = args

    # Exécuter le script principal
    exec(open(args[0]).read())