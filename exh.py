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
    c_e = int           # Per cada n_e cotxes puc millorar c_e cotxes
    n_e = int



def llegir_la_entrada():
    """Llegeix la entrada del programa i retorna els valors que li pertoca"""
    
    C, M, K = read(int), read(int), read(int)

    cotxes_millorats: list[millora] = []      #Es el nombre Ce, cotxes amb millora que es poden posar per cada Ne cotxes que passen per la estació
    cotxes_passats: list[int] = []        #Es el nombre Ne referenciat a sobre

    llista_millores: list[millora] = []     
    llista_tipus_de_cotxes: list[tipus_de_cotxes] = []

    for _ in range(M):
        cotxes_millorats.append(read(int))
    
    for _ in range(M):
        cotxes_passats.append(read(int))
    
    for i in range(M):
        llista_millores.append[millora(i, cotxes_millorats[i], cotxes_passats[i])]

    for _ in range(K):
        llista_tipus_de_cotxes.append(tipus_de_cotxes(read(int), read(int), [read(int) for _ in range(M)]))

    return C, M, K, llista_millores, llista_tipus_de_cotxes






def main() -> None:




if __name__ == "__main__":
    main()


#SOC LA PAULA SOC SUPER LLESTA I SUPER GUAPA MIREUME SOC LA PAULA HO PROMETO