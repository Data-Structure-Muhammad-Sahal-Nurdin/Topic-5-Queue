from linkedliststack import Stack


# Fungsi reverse_queue() membalik urutan elemen-elemen dalam
# queue yang diberikan sebagai argument.
def reverseQueue(q):
    # [1] Buat sebuah stack sementara untuk menyimpan elemen-elemen queue yang ditukar
    stack = []

    # [2] Keluarkan semua elemen dari queue dan masukkan ke dalam stack.
    while len(q) > 0:
        stack.append(q.dequeue())

    # [3] Keluarkan semua elemen dari stack dan kembalikan ke dalam queue
    while len(stack) > 0:
        q.enqueue(stack.pop())





