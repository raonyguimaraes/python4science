import os
from cogent.db.ensembl import HostAccount, Genome


if 'ENSEMBL_ACCOUNT' in os.environ:
    host, username, password = os.environ['ENSEMBL_ACCOUNT'].split()
    account = HostAccount(host, username, password)
else:
    account = None

human = Genome('human', Release=75, account=account)

gene_symbols = ['brca1', 'brca2']

genomes1k_url = 'ftp://ftp.1000genomes.ebi.ac.uk/vol1/ftp/release/20130502'

for gene_symbol in gene_symbols:
    print gene_symbol
    genes = human.getGenesMatching(Symbol=gene_symbol)
    for gene in genes:
        print gene.Location.CoordName
        print gene.Location.Start, gene.Location.End
        command = './breastcancer/programs/htslib/tabix -h \
        %s/ALL.chr%s.phase3_shapeit2_mvncall_integrated_v5a.20130502.genotypes.vcf.gz \
        %s:%s-%s > breastcancer/%s.vcf' % (genomes1k_url, gene.Location.CoordName, gene.Location.CoordName, gene.Location.Start, gene.Location.End, gene_symbol)
        print command
        #os.system(command)
        size = gene.Location.End - gene.Location.Start
        print 'Size', size
        print gene.Location.Strand
#brca2 = human.getGeneByStableId(StableId='ENSG00000139618')
#transcript = brca2.CanonicalTranscript
#print transcript


#get a single snp
#snp = list(human.getVariation(Symbol='rs34213141'))[0]
