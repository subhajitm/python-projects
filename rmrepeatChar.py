class remove_repeat():
    def remover(self, array):
        mask = 0
        output = []
        for c in array:
            t = 1
            t = t << c
            if mask & t:
                continue
            else:
                output.append(c)
                mask = mask | t
        return output

def main():
    array = [2,3,5,1,3,2,6,7,3,4,6,5,2,13,13,1,4,106,255,255,4600,4600,10200,4600]
    rr = remove_repeat()
    print rr.remover(array)

if __name__ == "__main__":
    main()
