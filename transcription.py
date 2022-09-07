f = open("/Users/michaeltu/Downloads/rosalind_rna (3).txt","r")

sequence = f.read()
f.close()
sequence = sequence.replace("T", "U")

answer = open("transcription_answer.txt", "w")
answer.write(sequence)
answer.close()