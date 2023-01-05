class Node:
    def __init__(self,data,priority) -> None:
        self._data = data
        self._priority = priority
        self._next = None
        self._prev = None

class PQSTugas:
    def __init__(self) -> None:
        self._head = None
        self._tail = None
        self._size = 0

    def isEmpty(self) -> bool:
        return self._data == 0
        
    def printAll(self) -> None:
    #isi kode anda
        pass
    def _addHead(self, newNode) -> None:
    #isi kode anda
        pass
    def _addTail(self, newNode) -> None:
    #isi kode anda
        pass
    def _addMiddle(self, newNode) -> None:
    #isi kode anda
        pass

    def add(self, data, priority) -> None:
        self._add = data
        self._penting == priority < data

    def remove(self) -> None:
        self._data.pop() == None

    def removePriority(self, priority) -> None:
    #isi kode anda
        pass

if __name__ == "__main__":
 tugasKu = PQSTugas()
 tugasKu.add("StrukDat",1)
 tugasKu.add("Menyapu", 5)
 tugasKu.add("Cuci Baju", 4)
 tugasKu.add("Beli Alat Tulis", 3)
 tugasKu.add("Cuci Sepatu", 4)
 tugasKu.printAll()
 tugasKu.remove()
 tugasKu.printAll()
 tugasKu.removePriority(2)
 tugasKu.removePriority(4)
 tugasKu.printtAll()