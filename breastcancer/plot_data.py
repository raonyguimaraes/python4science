
import matplotlib.pyplot as plt

vcffile = open('brca1.vcf','r')

colors = {
	'A':'red',
	'C':'yellow',
	'G':'green',
	'T':'blue',
}

genotypes_dict = {
	'0|0':'red',
	'0|1':'yellow',
	'1|0':'green',
	'1|1':'blue',
}

individuals_genotypes = {}
#example
#individuals_genotypes['NA2647']['182635271'] = colors['']

#get individuals names

for line in vcffile:
	if line.startswith('#CHROM'):
		individuals = line.strip().split('\t')[9:]
		# for individual in individuals:
		# 	individuals_genotypes[individual] = {}
	if not line.startswith('#'):
		row = line.strip().split('\t')
		pos = row[1]
		genotypes = row[9:]
		for k, individual in enumerate(individuals):
			# print k, individual
			# individuals_genotypes[individual][pos] = genotypes_dict[genotypes[k]]
			plt.scatter(pos, k, c=genotypes_dict[genotypes[k]])


		
		


# from numpy.random import rand


# for color in ['red', 'green', 'blue']:
#     n = 750
#     x, y = rand(2, n)
#     scale = 200.0 * rand(n)
#     plt.scatter(x, y, c=color, s=scale, label=color,
#                 alpha=0.3, edgecolors='none')

plt.legend()
plt.grid(True)

plt.show()
