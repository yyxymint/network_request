ff = open('gtex_dataset.txt','r')

chrom_strand_gene={}

total_acceptor=0

for line in ff:
    gene, paralog , chrom, strand, s, e, ll, rr = line.split('\t')
    rr=rr[:-1]
    
    if chrom not in chrom_strand_gene:
        chrom_strand_gene[chrom]={}
    
    if strand not in chrom_strand_gene[chrom]:
        chrom_strand_gene[chrom][strand]={}
    
    if gene not in chrom_strand_gene[chrom][strand]:
        chrom_strand_gene[chrom][strand][gene]=[s,e,set(),set(),set()]
        
        for l in ll.split(',')[:-1]:
            chrom_strand_gene[chrom][strand][gene][2].add(int(l))
        for r in rr.split(',')[:-1]:
            chrom_strand_gene[chrom][strand][gene][3].add(int(r))
            
            
    if strand=='+':
        total_acceptor+=len(chrom_strand_gene[chrom][strand][gene][3])
        
    else:
        total_acceptor+=len(chrom_strand_gene[chrom][strand][gene][2])
total_acceptor








# ======================================================================================================================================








def sen_with_tab(uu):
    ret=''
    for i in uu:
        ret+=str(i)+'\t'
    return ret[:-1]


in_gene=0
out_gene=0
f=open('gtex_iff_colaseq_bp_fix.txt','w')

for chrom in chrom_strand_gene.keys():
    for strand in chrom_strand_gene[chrom].keys():
        for gene in chrom_strand_gene[chrom][strand].keys():
            
            
            jn_sta = chrom_strand_gene[chrom][strand][gene][0]
            jn_end = chrom_strand_gene[chrom][strand][gene][1]

            exn_sta = ''
            exn_end = ''
            

            chrom_strand_gene[chrom][strand][gene][2]=list(chrom_strand_gene[chrom][strand][gene][2])
            chrom_strand_gene[chrom][strand][gene][3]=list(chrom_strand_gene[chrom][strand][gene][3])
            
            
            
            chrom_strand_gene[chrom][strand][gene][2].sort()
            chrom_strand_gene[chrom][strand][gene][3].sort()


            for p in chrom_strand_gene[chrom][strand][gene][2]:
                exn_sta+=str(p)+','

            for p in chrom_strand_gene[chrom][strand][gene][3]:
                exn_end+=str(p)+','
                

            rr = sen_with_tab([gene,0,chrom,strand,jn_sta,jn_end,exn_sta,exn_end])

            f.write(rr+'\n')
        
f.close()

