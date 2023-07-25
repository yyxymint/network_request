def sen_with_tab(uu):
    ret=''
    for i in uu:
        ret+=str(i)+'\t'
    return ret[:-1]


f=open('mercer_bp_dataset.txt','w')

for chrom in by_chr_strand_gene.keys():
    for strand in by_chr_strand_gene[chrom].keys():
        for gene in by_chr_strand_gene[chrom][strand].keys():
            jn_sta = by_chr_strand_gene[chrom][strand][gene][0]
            jn_end = by_chr_strand_gene[chrom][strand][gene][1]

            exn_sta = ''
            exn_end = ''

            by_chr_strand_gene[chrom][strand][gene][2].sort()

            for p in by_chr_strand_gene[chrom][strand][gene][2]:
                exn_sta+=str(p)+','

            for p in by_chr_strand_gene[chrom][strand][gene][2]:
                exn_end+=str(p)+','

            rr = sen_with_tab([gene,0,chrom,strand,jn_sta,jn_end,exn_sta,exn_end])

            f.write(rr+'\n')
        
f.close()
