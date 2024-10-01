  def obsah_obdelniku():
    a = int(input("Zadej stranu A="))
    b= int(input("Zadej stranu B="))
    if a or b > 0:
        c = a*b
        print(f"Obsah obdelníku o stranach A={a}, B={b} je {c}")
    else: print("chyba")

obsah_obdelniku()