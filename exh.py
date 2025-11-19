from yogi import *
from dataclasses import dataclass

@dataclass
class tipus_de_cotxes:
    id_tipus: int
    num_cotxes: int
    millores: list[int]

@dataclass
class millora:
    id_millora: int
    c_e: int           # Per cada n_e cotxes puc millorar c_e cotxes
    n_e: int



def llegir_la_entrada():
    """Llegeix la entrada del programa i retorna els valors que li pertoca"""
    
    c, m, k = read(int), read(int), read(int)

    cotxes_millorats: list[int] = []      #Es el nombre Ce, cotxes amb millora que es poden posar per cada Ne cotxes que passen per la estació
    cotxes_passats: list[int] = []        #Es el nombre Ne referenciat a sobre

    llista_millores: list[millora] = []     
    llista_tipus_de_cotxes: list[tipus_de_cotxes] = []

    for _ in range(m):
        cotxes_millorats.append(read(int))
    
    for _ in range(m):
        cotxes_passats.append(read(int))
    
    for i in range(m):
        llista_millores.append(millora(i, cotxes_millorats[i], cotxes_passats[i]))

    for _ in range(k):
        llista_tipus_de_cotxes.append(tipus_de_cotxes(read(int), read(int), [read(int) for _ in range(m)]))

    return c, m, k, llista_millores, llista_tipus_de_cotxes


def generar_solucions_exh(counts):
    t = len(counts)                   # nombre de tipus
    resultat = set()                  # usem un set per evitar duplicats
    
    def backtrack(actual, restants):
        if sum(restants) == 0:       # ja no queden cotxes
            resultat.add(tuple(actual))  # guardem com a tuple per ser hashable
            return

        for tipus in range(t):
            if restants[tipus] > 0:
                noves_restants = list(restants)
                noves_restants[tipus] -= 1
                backtrack(actual + [tipus], noves_restants)  # ara actual és una llista

    backtrack([], counts)
    return [list(r) for r in resultat]  # convertim tuples de nou a llista



def main() -> None:
    c, m, k, llista_millores, llista_tipus_de_cotxes = llegir_la_entrada()

    quantitats_cotxes = [tipus.num_cotxes for tipus in llista_tipus_de_cotxes]

    solucions = generar_solucions_exh(quantitats_cotxes)

    print(solucions, len(solucions))





if __name__ == "__main__":
    main()
