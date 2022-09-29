import csv

f = open('hybridQA_with_tapex_score.csv','w', newline='')
wr = csv.writer(f)
wr.writerow(['score','generated sentence','original table'])

for i in range(20):
    wr.writerow(tapex_scores[i])
f.close()
